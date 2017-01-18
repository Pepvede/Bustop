#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017, José Verdú Díaz, All rights reserved.
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'^mapa/$', views.mapa, name='mapa'),
	url(r'^lineas/$', views.lineas, name='lineas'),
	url(r'^lineas/(?P<linea_numero>\d+)/$', views.lineas_detalles, name='lineas_detalles'),
	url(r'^versiones/$', views.versiones, name='versiones'),
	url(r'^rutas/$', views.rutas, name='rutas')
]