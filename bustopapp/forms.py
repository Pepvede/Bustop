#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017, José Verdú Díaz, All rights reserved.
from django import forms
from .models import Linea


class LineaForm(forms.ModelForm):
	

	class Meta:
		model = Linea
		fields = ('numero',)
