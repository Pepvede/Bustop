#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017, José Verdú Díaz, All rights reserved.
from __future__ import unicode_literals

from django.db import models


class Linea(models.Model):
	numero = models.CharField(max_length=2)


	def __str__(self):
		return self.numero
		

class Bus(models.Model):
	linea = models.ForeignKey(Linea, on_delete=models.CASCADE)
	latitud = models.DecimalField(max_digits=8, decimal_places=6)
	longitud = models.DecimalField(max_digits=8, decimal_places=6)


	def __int__(self):
		pass


class Parada(models.Model):
	numero = models.CharField(max_length=3)
	latitud = models.DecimalField(max_digits=8, decimal_places=6)
	longitud = models.DecimalField(max_digits=8, decimal_places=6)

	def __str__(self):
		return self.numero
'''
class: define un objeto

Bus: nombre del objeto, debe empezar en mayúsculas siempre

models.Model: especifica que es un modelo de django y que, por tanto,
			  debe guardarse en la base de datos

x = y establece una propiedad del objeto

y.z() establece el tipo de propiedad

linea: número de la línea de bus

PositiveSmallIntegerField(): número entero desde 0 hasta 32767,
							 con un número de estas dimensiones se 
							 evitan conflictos con la base de datos

posiciongps: posicion del bus en coordenadas latitud/longitud

max_digits: número maximo de dígitos
decimal_places: cantidad de dígitos decimales

def x(): define un "method" del objecto
'''
