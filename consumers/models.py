# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    idUsers       = models.CharField(max_length=24)
    login     = models.CharField(max_length=24)
    email   = models.CharField(max_length=24)
    tenantId   = models.CharField(max_length=24)
    state = models.CharField(max_length=12)
    def __str__(self):
        return self.login
