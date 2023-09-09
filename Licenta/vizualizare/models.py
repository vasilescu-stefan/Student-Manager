from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.



class Students(models.Model):
    nr_matricol = models.CharField(max_length=20)
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    an = models.IntegerField()
    grupa = models.CharField(max_length=2)
    specializare=models.CharField(max_length=50, null=True)
    data_nastere = models.DateField(auto_now=False, auto_now_add=False)
    telefon=models.IntegerField(null=True)
    mama=models.CharField(max_length=50, null=True)
    tata=models.CharField(max_length=50, null=True)
    nationalitatea=models.CharField(max_length=50, null=True)
    cetatenia=models.CharField(max_length=50, null=True)
    class Meta:
        verbose_name_plural = "Studenti"


class Profesori(models.Model):
    id_prof = models.CharField(max_length=50)
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    grad_didactic = models.CharField(max_length=50)
    id_curs = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Profesori"


class Cursuri(models.Model):
    id_curs = models.CharField(max_length=50)
    titlu_curs = models.CharField(max_length=100)
    an = models.IntegerField()
    semestru = models.IntegerField()
    credite = models.IntegerField()

    class Meta:
        verbose_name_plural = "Cursuri"


class Note(models.Model):
    nr_matricol = models.CharField(max_length=20)
    id_curs = models.CharField(max_length=50)
    valoare = models.IntegerField(null=True, blank=True)
    data_notare = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Note"

class Optionale(models.Model):
    nr_matricol = models.CharField(max_length=20, null=True)
    pachet = models.CharField(max_length=50)
    optiunea1=models.CharField(max_length=50)
    optiunea2=models.CharField(max_length=50)
    optiunea3=models.CharField(max_length=50)
    optiunea4=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Optionale"
