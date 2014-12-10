from django.conf.urls import url

from app_emotimon import views

urlpatterns = [
    url(r'^$', views.index),
    
    url(r'^analysis$', views.analysis),
    
    url(r'^phone/store$', views.phone_store),
    url(r'^watch/store/heart$', views.watch_heart_store),
    url(r'^watch/store/acc$', views.watch_acc_store),
    
    url(r'^watch/data/heart$', views.watch_heart_data),
    url(r'^watch/data/acc$', views.watch_acc_data),
    url(r'^phone/data/mic$', views.phone_mic_data),
    url(r'^phone/data/acc$', views.phone_acc_data),
]
