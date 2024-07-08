from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse, Http404
from django.conf import settings
import os

from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from base.models import CustomUser, Notification, Paiement, Reservation, Trajet, Vehicule
from base.serializers import NotificationSerializers, PaiementSerializers, ReservationSerializers, TrajetSerializers, UserFilter, UserSerializers, VehiculeSerializers

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializers

class TrajetViewSet(viewsets.ModelViewSet):
    queryset=Trajet.objects.all()
    serializer_class=TrajetSerializers
    filter_backends = [OrderingFilter]

    
class VehiculeViewSet(viewsets.ModelViewSet):
    queryset=Vehicule.objects.all()
    serializer_class=VehiculeSerializers
    def get_queryset(self):
        queryset = Vehicule.objects.all()
        user_id = self.request.query_params.get('idUser', None)
        if user_id is not None:
            queryset = queryset.filter(idUser=user_id)
        return queryset
    
    
class PaiementViewSet(viewsets.ModelViewSet):
    queryset=Paiement.objects.all()
    serializer_class=PaiementSerializers

class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializers
class userViewSet(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter