#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017, José Verdú Díaz, All rights reserved.
from django.shortcuts import render, redirect, reverse
from .forms import LineaForm
from django.http import HttpResponseRedirect
from datetime import datetime
from models import Linea


def main(request):
	return render(request, 'bustopapp/main.html', {})


def mapa(request):
	return render(request, 'bustopapp/mapa.html', {})


def lineas(request, template="bustopaplineas.html"):
	if request.method == "POST":
		form = LineaForm(request.POST)
		if form.is_valid():
			numero = form.save(commit=False)
			linea_numero = str(numero)
			return redirect('lineas_detalles', linea_numero=linea_numero)
	else:
		form = LineaForm()
	return render(request, 'bustopapp/lineas.html', {'form': form})


def lineas_detalles(request, linea_numero):
	return render(request, 'bustopapp/lineas_detalles.html', {"linea_numero":linea_numero})


def versiones(request):
	return render(request, 'bustopapp/versiones.html', {})

def rutas(request):
	return render(request, 'bustopapp/rutas.html', {})

def tarifas(request):
	return render(request, 'bustopapp/tarifas.html', {})