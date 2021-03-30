# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 14:18:10 2021

@author: syg
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]