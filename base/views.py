from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.filters import OrderingFilter

from base.models import CustomUser, Notification, Paiement, Reservation, Trajet, Vehicule
from base.serializers import NotificationSerializers, PaiementSerializers, ReservationSerializers, TrajetSerializers, UserSerializers, VehiculeSerializers

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializers
class TrajetViewSet(viewsets.ModelViewSet):
    queryset=Trajet.objects.all()
    serializer_class=TrajetSerializers
    filter_backends = [OrderingFilter]
    ordering_fields = ['horaire']
    
class VehiculeViewSet(viewsets.ModelViewSet):
    queryset=Vehicule.objects.all()
    serializer_class=VehiculeSerializers
    
    
class PaiementViewSet(viewsets.ModelViewSet):
    queryset=Paiement.objects.all()
    serializer_class=PaiementSerializers

class NotificationViewSet(viewsets.ModelViewSet):
    queryset=Notification.objects.all()
    serializer_class=NotificationSerializers
class userViewSet(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializers
