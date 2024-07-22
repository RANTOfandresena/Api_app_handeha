from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse, Http404
from django.conf import settings
import os

from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from base.models import CustomUser, Notification, Paiement, Reservation, Trajet, Vehicule
from base.serializers import NotificationSerializers, PaiementSerializers, ReservationSerializers, TrajetSerializers, UserFilter, UserSerializers, VehiculeSerializers


from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializers

from django.shortcuts import render
from django.http import JsonResponse
import openrouteservice
import json
import datetime
from django.db.models import Q
from rest_framework.filters import BaseFilterBackend


class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializers
    filterset_fields=['idUser','idTrajet']#'horaire'


class TrajetViewSet(viewsets.ModelViewSet):
    queryset=Trajet.objects.all()
    serializer_class=TrajetSerializers
    filterset_fields=['lieuArrive','lieuDepart','horaire']
    search_fields=('lieuArrive','lieuDepart','horaire')
    filter_backends = [OrderingFilter]
    def get_queryset(self):
        queryset = Trajet.objects.all()
        user_id = self.request.query_params.get('idUser', None)
        print("gggggggggggggg")
        print(user_id)
        print("gggggggggggggg")
        if user_id is not None:
            queryset = queryset.filter(idUser=user_id)
        # Filtrer les trajets dont la date est expirée
        queryset = queryset.filter(horaire__gte=datetime.date.today())
        return queryset

class VehiculeViewSet(viewsets.ModelViewSet):
    queryset=Vehicule.objects.all()
    serializer_class=VehiculeSerializers
    filterset_fields=['idVehicule']
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

class CreateUserView(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Utilisateur créé avec succès'})
        return Response(serializer.errors, status=400)
def get_route(request):
    client = openrouteservice.Client(key='5b3ce3597851110001cf6248f3b777ac2d094a13abbbec85a0752240')

    # Récupérer les coordonnées de départ et d'arrivée depuis les paramètres GET
    try:
        start_lon = float(request.GET.get('lon1'))
        start_lat = float(request.GET.get('lat1'))
        end_lon = float(request.GET.get('lon2'))
        end_lat = float(request.GET.get('lat2'))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid or missing coordinates'}, status=400)

    # Coordonnées de départ et d'arrivée (longitude, latitude)
    start_coords = (start_lon, start_lat)
    end_coords = (end_lon, end_lat)

    # Effectuer une requête pour obtenir l'itinéraire
    try:
        route = client.directions(
            coordinates=[start_coords, end_coords],
            profile='driving-car',
            format='geojson'
        )
    except openrouteservice.exceptions.ApiError as e:
        return JsonResponse({'error': str(e)}, status=400)

    # Extraire les coordonnées de l'itinéraire
    route_coords = route['features'][0]['geometry']['coordinates']

    # Retourner les coordonnées en tant que réponse JSON
    return JsonResponse({'route_coords': route_coords})