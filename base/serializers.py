from rest_framework import serializers
from django.contrib.auth import authenticate
from base.models import CustomUser, Notification, Paiement, Reservation, Trajet, Vehicule
from django_filters import rest_framework as filters

from dj_rest_auth.serializers import LoginSerializer

class ReservationSerializers(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields="__all__"

class TrajetSerializers(serializers.ModelSerializer):
    class Meta:
        model=Trajet
        fields="__all__"
    
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
        fields=("id","last_login","username","first_name","last_name","email","numero","image","password") 


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
 
