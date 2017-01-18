#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017, José Verdú Díaz, All rights reserved.
"""
WSGI config for bustop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bustop.settings")

application = get_wsgi_application()
