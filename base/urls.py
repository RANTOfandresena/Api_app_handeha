from rest_framework import routers

from base.views import NotificationViewSet, PaiementViewSet, ReservationViewSet, TrajetViewSet, VehiculeViewSet, userViewSet
router=routers.DefaultRouter()
router.register("reservation",ReservationViewSet)
router.register("trajet",TrajetViewSet)
router.register("vehicule",VehiculeViewSet)
router.register("paiement",PaiementViewSet)
router.register("notification",NotificationViewSet)
router.register("user",userViewSet)
