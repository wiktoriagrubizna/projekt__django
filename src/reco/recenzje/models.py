from django.db import models

class Actor (models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)

    def __str__(self):
        return self.imie + '' + self.nazwisko

class Director (models.Model):
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)

    def __str__(self):
        return self.imie + '' + self.nazwisko

class Ocena (models.Model):
    wartosc = models.CharField(max_length=45)
    user = models.CharField(max_length=45)

    def __str__(self):
        return self.wartosc

class Film (models.Model):
    nazwa = models.CharField(max_length=45)
    opis = models.TextField()
    aktorzy = models.ManyToManyField(Director)
    rezyserzy = models.ManyToManyField(Actor)
    srednia_ocena = models.CharField(max_length=45)
    created = models.CharField(max_length=45)
    uploated = models.CharField(max_length=45)
    ilosc_ocen = models.CharField(max_length=45)

    def __str__(self):
        return self.nazwa


