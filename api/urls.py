from django.urls import path,include
from . import views
from base import views

urlpatterns = [
    # path('',views.getData),
    path('dj-rest-auth/',include('dj_rest_auth.urls')) ,
    path('get_route/', views.get_route, name='get_route'),
    path('', include('telechargementApp.urls')),
]
