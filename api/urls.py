from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.getData),
    path('dj-rest-auth/',include('dj_rest_auth.urls')) 
]
