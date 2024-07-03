from django.db import models
from django.contrib.auth.models import AbstractUser


'''
Relations et Cardinalités

    Utilisateur et Notification:
        Un utilisateur peut avoir plusieurs notifications (0..*), 
        mais une notification appartient à un seul utilisateur (1).
    Utilisateur et Réservation: 
        Un utilisateur peut avoir plusieurs réservations (0..*), 
        mais une réservation appartient à un seul utilisateur (1).
    Réservation et Paiement: 
        Une réservation a un paiement (1), 
        et un paiement est associé à une seule réservation (1).
    Trajet et Réservation: 
        Un trajet peut avoir plusieurs réservations (0..*), 
        mais une réservation est associée à un seul trajet (1).
    Trajet et Véhicule: 
        Un trajet est associé à un seul véhicule (1), 
        et un véhicule peut être associé à plusieurs trajets (0..*).
'''


class CustomUser(AbstractUser):
    numero = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    cin=models.CharField(max_length=20)
    est_conducteur=models.BooleanField(default=False)
    USERNAME_FIELD = 'numero'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.numero
class Utilisateur(models.Model):
    idUser = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)
    motDePasse = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.nom} {self.prenom}'

class Trajet(models.Model):
    idTrajet = models.AutoField(primary_key=True)
    lieuDepart = models.CharField(max_length=100)
    lieuArrive = models.CharField(max_length=100)
    horaire = models.DateTimeField()
    prix=models.DecimalField(max_digits=10,decimal_places=2)
    idVehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE)
    attribute = models.CharField(max_length=100, null=True, blank=True)
    idUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return f'Trajet de {self.lieuDepart} à {self.lieuArrive}'
    
class Vehicule(models.Model):
    idVehicule = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    positionActuelle = models.CharField(max_length=100,null=True)
    capacite = models.IntegerField()
    numeroVechicule = models.CharField(max_length=100,null=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    def __str__(self):
        return f'Vehicule {self.idVehicule}'
    
class Reservation(models.Model):
    idReservation = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    idTrajet = models.ForeignKey(Trajet, on_delete=models.CASCADE)
    siegeNumero = models.CharField(max_length=10)
    def __str__(self):
        return f'Reservation {self.idReservation} par {self.idUser}'
    
class Paiement(models.Model):
    idPaiement = models.AutoField(primary_key=True)
    ref=models.CharField(max_length=10,null=True)
    preuve = models.ImageField(upload_to='preuve/', null=True, blank=True)
    idReservation = models.OneToOneField(Reservation, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'Paiement {self.idPaiement} pour la reservation {self.idReservation.idReservation}'

class Notification(models.Model):
    idNotification = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    dateEnvoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification {self.idNotification} pour l\'utilisateur {self.idUser.idUser}'