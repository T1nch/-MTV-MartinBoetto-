from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from pipes import Template
from django.shortcuts import render
from AppMartin.models import Familia
from django.template import Context, Template 
from django.template import loader 


def familiar(self):

        familiar= Familia(nombre="Martin", edad="20", nacimiento="10-03-2002")
        familiar.save() 
        texto= f"{familiar.nombre} {familiar.edad} {familiar.nacimiento}"
        return HttpResponse(texto)

def familiar2(self):

        familiar= Familia(nombre="Carla", edad="48", nacimiento="11-11-1973")
        familiar.save()
        texto= f"{familiar.nombre} {familiar.edad} {familiar.nacimiento}"
        return HttpResponse(texto)

def templatehtml(self):
    mihtml = open("C:/Users/marti/OneDrive/Escritorio/ProyectoMartin/Plantillas/template.html")

    plantilla = Template(mihtml.read())

    mihtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)