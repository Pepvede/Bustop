#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017, José Verdú Díaz, All rights reserved.
from django.contrib import admin
from .models import Bus, Parada, Linea

admin.site.register(Bus)
admin.site.register(Parada)
admin.site.register(Linea)