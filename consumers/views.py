# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models import Q
from rest_framework import generics, mixins
from consumers.models import Users

from django.shortcuts import render

from django.http import HttpResponse


def index(self, request):
    #return HttpResponse("Veuillez fournir une clé d'API..")
    usersList = Users.objects.all()
    #serializer = UserSerializer #Serialise my users with the video
    html = ''
    for user in usersList:
        pass

def usersManagement(request, API_KEY): #Listing all Users of the connected Tenant
    return HttpResponse("Voici la clé %s." % API_KEY)
