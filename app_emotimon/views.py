from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time
import datetime
import app_emotimon.models as Models
import numpy

emotions = {
'afraid': 0,
'angry': 1,
'calm': 2,
'delighted': 3,
'excited': 4,
'frustrated': 5,
'glad': 6,
'gloomy' : 7,
'happy': 8,
'miserable': 9,
'sad': 10,
'satisfied': 11,
'serene': 12,
'sleepy': 13,
'tense': 14,
'tired': 15,
}
# Create your views here.

@csrf_exempt
def index(request):
    context = RequestContext(request)
    return render_to_response('app_emotimon/templates/index.html', {}, context)

@csrf_exempt
def analysis(request):
    context = RequestContext(request)

    emotion_dict = {}
    for emotion in emotions.keys():
        sensor_data = Models.SensorData.objects.filter(emotion=emotions[emotion])
        w_hr = []
        w_x = []
        w_y = []
        w_z = []
        p_m = []
        p_x = []
        p_y = []
        p_z = []
        curr = {}

        for item in sensor_data:
            if item.heartbeat_avg:
                w_hr.append(item.heartbeat_avg)
            
            if item.acc_watch_x_avg:
                w_x.append(item.acc_watch_x_avg)

            if item.acc_watch_y_avg:
                w_y.append(item.acc_watch_y_avg)

            if item.acc_watch_z_avg:
                w_z.append(item.acc_watch_z_avg)

            if item.mic_avg:
                p_m.append(item.mic_avg)

            if item.acc_phone_x_avg:
                p_x.append(item.acc_phone_x_avg)

            if item.acc_phone_y_avg:
                p_y.append(item.acc_phone_y_avg)

            if item.acc_phone_z_avg:
                p_z.append(item.acc_phone_z_avg)

        curr['w_hr'] = numpy.median(w_hr)
        curr['w_x'] = numpy.median(w_x)
        curr['w_y'] = numpy.median(w_y)
        curr['w_z'] = numpy.median(w_z)
        curr['p_m'] = numpy.median(p_m)
        curr['p_x'] = numpy.median(p_x)
        curr['p_y'] = numpy.median(p_y)
        curr['p_z'] = numpy.median(p_z)

        emotion_dict[emotion] = curr

    return render_to_response('app_emotimon/templates/analysis.html', {'analysis': emotion_dict}, context)
    #return HttpResponse(json.dumps(toRet), content_type="application/json")

@csrf_exempt
def watch_heart_data(request):
    sensor_data = Models.SensorData.objects.exclude(heartbeat_avg=None)
    heart_data = [[i.timestamp.strftime("%m/%d/%y %H:%M"), i.heartbeat_avg] for i in sensor_data]  

    resp = {'data': heart_data}
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def watch_acc_data(request):
    sensor_data = Models.SensorData.objects.exclude(acc_watch_x_avg=None, acc_watch_y_avg=None, acc_watch_z_avg=None)
    # on acc_data line below, can use i.id instead of i.timestamp for continuous data stream
    acc_data = [[i.timestamp.strftime("%m/%d/%y %H:%M"), i.acc_watch_x_avg, i.acc_watch_y_avg, i.acc_watch_z_avg] for i in sensor_data]

    resp = {'data': acc_data}
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def phone_mic_data(request):
    sensor_data = Models.SensorData.objects.exclude(mic_avg=None)
    # on mic_data line below, can use i.id instead of i.timestamp for continuous data stream
    mic_data = [[i.timestamp.strftime("%m/%d/%y %H:%M"), i.mic_avg] for i in sensor_data]  

    resp = {'data': mic_data}
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def phone_acc_data(request):
    sensor_data = Models.SensorData.objects.exclude(acc_phone_x_avg=None, acc_phone_y_avg=None, acc_phone_z_avg=None)
    # on acc_data line below, can use i.id instead of i.timestamp for continuous data stream
    acc_data = [[i.timestamp.strftime("%m/%d/%y %H:%M"), i.acc_phone_x_avg, i.acc_phone_y_avg, i.acc_phone_z_avg] for i in sensor_data]

    resp = {'data': acc_data}
    return HttpResponse(json.dumps(resp), content_type="application/json")

@csrf_exempt
def phone_store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except KeyError:
            return HttpResponse("Malformed data!")

        #User Id
        userId = data['id']

        # Datetime - to get x-axis
        datetime_str = data['date'] + " " + data['time']
        datetime = time.strftime("%Y-%m-%d %H:%M", time.strptime(datetime_str,"%m/%d/%Y %H:%M"))

	z_data = data['aziData']
        z_data_avg = sum(z_data) / len(z_data)
        
        x_data = data['pitchData']
        x_data_avg = sum(x_data) / len(x_data)
        
	y_data = data['rollData']
        y_data_avg = sum(y_data) / len(y_data)
        
	mic_data = data['micData']
        mic_data_avg = sum(mic_data) / len(mic_data)
       
        # Emotion
        try:
            emotion = emotions[data['emotion']]
        except:
            emotion = ''

        data_points = Models.SensorData.objects.filter(timestamp=datetime)
        
	if len(data_points) > 0:
            data_point = data_points[0] 
            data_point.mic_pts = repr(mic_data)
	    data_point.mic_avg = mic_data_avg
	    data_point.acc_phone_x_pts = repr(x_data)
	    data_point.acc_phone_x_avg = x_data_avg
            data_point.acc_phone_y_pts = repr(y_data)
            data_point.acc_phone_y_avg = y_data_avg
            data_point.acc_phone_z_pts = repr(z_data)
            data_point.acc_phone_z_avg = z_data_avg
            data_point.emotion = emotion
            data_point.user_id = userId
	    data_point.save()
        else: 
            data_point = Models.SensorData(timestamp=datetime, user_id=userId, emotion=emotion, mic_pts=repr(mic_data), mic_avg=mic_data_avg, acc_phone_x_pts=repr(x_data), acc_phone_x_avg=x_data_avg, acc_phone_y_pts=repr(y_data), acc_phone_y_avg=y_data_avg, acc_phone_z_pts=repr(z_data), acc_phone_z_avg=z_data_avg)
            data_point.save()
         
	return HttpResponse("Got json data %s, average z %f, average x %f, average y %f, average mic %f" % (data, z_data_avg, x_data_avg, y_data_avg, mic_data_avg))
    
    return HttpResponse('phone store it')

@csrf_exempt
def watch_heart_store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except KeyError:
            return HttpResponse("Malformed data!")

        userId = data['id']

        datetime_str = data['date'] + " " + data['timestamp']
        datetime = time.strftime("%Y-%m-%d %H:%M", time.strptime(datetime_str,"%m/%d/%Y %H:%M"))

        heart_beat = data['heart_beat']
        filtered_heart_beat = [x for x in heart_beat if x != 0]
        len_filtered = len(filtered_heart_beat)
        if len_filtered > 0:
            avg = sum(filtered_heart_beat) / len_filtered
        else:
            avg = 0

        data_points = Models.SensorData.objects.filter(timestamp=datetime)
        
	if len(data_points) > 0:
            data_point = data_points[0] 
            data_point.user_id = userId
            data_point.heartbeat_pts = repr(heart_beat)
            data_point.heartbeat_avg = avg
	    data_point.save()
        else: 
            data_point = Models.SensorData(timestamp=datetime, user_id=userId, heartbeat_pts=repr(heart_beat), heartbeat_avg=avg)
            data_point.save()

        return HttpResponse("Got json data %s, and the avg heart rate was %f, %s" % (data, avg, repr(datetime)))

    return HttpResponse('watch heart store it')

@csrf_exempt
def watch_acc_store(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except KeyError:
            return HttpResponse("Malformed data!")

        #User Id
        userId = data['id']

        # Datetime - to get x-axis
        datetime_str = data['date'] + " " + data['timestamp']
        datetime = time.strftime("%Y-%m-%d %H:%M", time.strptime(datetime_str,"%m/%d/%Y %H:%M"))

	z_data = data['aziData']
        z_data_avg = sum(z_data) / len(z_data)
        
        x_data = data['pitchData']
        x_data_avg = sum(x_data) / len(x_data)
        
	y_data = data['rollData']
        y_data_avg = sum(y_data) / len(y_data)

        data_points = Models.SensorData.objects.filter(timestamp=datetime)
        
	if len(data_points) > 0:
            data_point = data_points[0] 
	    data_point.acc_watch_x_pts = repr(x_data)
	    data_point.acc_watch_x_avg = x_data_avg
            data_point.acc_watch_y_pts = repr(y_data)
            data_point.acc_watch_y_avg = y_data_avg
            data_point.acc_watch_z_pts = repr(z_data)
            data_point.acc_watch_z_avg = z_data_avg
            data_point.user_id = userId
	    data_point.save()
        else: 
            data_point = Models.SensorData(timestamp=datetime, user_id=userId, acc_watch_x_pts=repr(x_data), acc_watch_x_avg=x_data_avg, acc_watch_y_pts=repr(y_data), acc_watch_y_avg=y_data_avg, acc_watch_z_pts=repr(z_data), acc_watch_z_avg=z_data_avg)
            data_point.save()
         
	return HttpResponse("Got json data %s, average z %f, average x %f, average y %f" % (data, z_data_avg, x_data_avg, y_data_avg))
    

    return HttpResponse('watch acc store it')
