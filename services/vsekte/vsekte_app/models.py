from django.db import models


class Sektant(models.Model):
    username = models.fields.CharField(max_length=50)
    password = models.fields.CharField(max_length=32)


class Sekta(models.Model):
    sektaname = models.fields.CharField(max_length=50)
    private_key = models.fields.CharField(max_length=32)
    participants = models.ManyToManyField(Sektant,blank=True)


class Nickname(models.Model):
    sektant = models.OneToOneField(Sektant)
    sekta = models.OneToOneField(Sekta)
    nickname = models.fields.CharField(max_length=50)


