from django.db import models

# Create your models here.


class NajotTalim(models.Model):
     Kurs_nomi = models.CharField(max_length=100)
     Kurs_turi = models.CharField(max_length=100)
     Kurs_narxi =models.DecimalField(max_digits=10, decimal_places=2)
     Kurs_muddati = models.CharField(max_length=50)
     Darslar_soni = models.IntegerField()
     Darslar_soati = models.IntegerField()
     Kurs_haqida = models.TextField()
     

     def __str__(self):
          return self.Kurs_nomi