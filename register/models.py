# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    PROFESSIONAL = 'PROFESSIONAL'
    PATIENT = 'PATIENT'
    ROLE_CHOICES = (
        (PROFESSIONAL, 'Pro'),
        (PATIENT, 'Patient'),
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    addressCabinet = models.CharField(max_length=255, verbose_name='Adresse du cabinet', null=True, default=None, blank=True)
    age = models.IntegerField(verbose_name='Age', null=True, default=None, blank=True)
    description = models.TextField(verbose_name='Description', null=True, default=None, blank=True)

