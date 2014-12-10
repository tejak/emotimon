from django.db import models

# Create your models here.

class SensorData(models.Model):
    # time stamp 
    timestamp = models.DateTimeField()

    # user
    user_id = models.IntegerField(null=True)
    
    # heart beat
    heartbeat_pts = models.TextField(null=True)
    heartbeat_avg = models.FloatField(null=True)

    # microphone 
    mic_pts = models.TextField(null=True)
    mic_avg = models.FloatField(null=True)

    # accelerometer from watch
    acc_watch_x_pts = models.TextField(null=True)
    acc_watch_x_avg = models.FloatField(null=True)

    acc_watch_y_pts = models.TextField(null=True)
    acc_watch_y_avg = models.FloatField(null=True)
    
    acc_watch_z_pts = models.TextField(null=True)
    acc_watch_z_avg = models.FloatField(null=True)

    # accelerometer from phone
    acc_phone_x_pts = models.TextField(null=True)
    acc_phone_x_avg = models.FloatField(null=True)

    acc_phone_y_pts = models.TextField(null=True)
    acc_phone_y_avg = models.FloatField(null=True)
    
    acc_phone_z_pts = models.TextField(null=True)
    acc_phone_z_avg = models.FloatField(null=True)

    # activity 
    activity = models.IntegerField(null=True)

    # emotion
    emotion = models.IntegerField(null=True)
