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