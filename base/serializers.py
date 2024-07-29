from rest_framework import serializers
from django.contrib.auth import authenticate
from base.models import CustomUser, Notification, Paiement, Reservation, Trajet, Vehicule
from django_filters import rest_framework as filters

from dj_rest_auth.serializers import LoginSerializer


    
class VehiculeSerializers(serializers.ModelSerializer):
    class Meta:
        model=Vehicule
        fields="__all__"
    
    
class PaiementSerializers(serializers.ModelSerializer):
    class Meta:
        model=Paiement
        fields="__all__"

class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields="__all__"
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=("id","last_login","username","first_name","last_name","email","numero","image","est_conducteur")
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

class TrajetSerializers(serializers.ModelSerializer):
    chauffer=UserSerializers(source="idUser", read_only=True)
    class Meta:
        model=Trajet
        fields=('idTrajet', 'lieuDepart', 'lieuArrive', 'horaire', 'prix',
                  'idVehicule','idUser', 'siegeReserver', 'chauffer')
class ReservationSerializers(serializers.ModelSerializer):
    trajet = TrajetSerializers(source='idTrajet', read_only=True)
    utlitisateurResever=UserSerializers(source="idUser", read_only=True)
    paiement = PaiementSerializers(read_only=True)
    class Meta:
        model=Reservation
        fields = ('idReservation', 'idUser', 'idTrajet', 'siegeNumero', 'trajet', 'utlitisateurResever','paiement')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            paiement = Paiement.objects.get(idReservation=instance)
            representation['paiement'] = PaiementSerializers(paiement).data
        except Paiement.DoesNotExist:
            representation['paiement'] = None
        return representation
# class CustomLoginSerializer(LoginSerializer):
#     username = serializers.CharField(required=True, allow_blank=False)

#     def get_auth_user(self, numero, password):
#         user = authenticate(numero=numero, password=password)
#         if user:
#             return user
#         raise serializers.ValidationError("Unable to log in with provided credentials.")
class CustomLoginSerializer(LoginSerializer):
    numero = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        numero = attrs.get('numero')
        password = attrs.get('password')

        if numero and password:
            user = authenticate(numero=numero, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "numero" and "password".'
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs




class UserFilter(filters.FilterSet):
    numero = filters.CharFilter(field_name="numero", lookup_expr='exact')

    class Meta:
        model = CustomUser
        fields = ['numero']
 
