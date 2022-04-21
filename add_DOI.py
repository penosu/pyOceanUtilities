#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 10:33:39 2022

@author: gonzalo
"""

import netCDF4 as nc

import os


for archivo in os.listdir(): 
	print(archivo)
	if (archivo.endswith('.nc')):
		
		ncfile=nc.Dataset(archivo,'r+')
		ncfile.DOI='10.17882/87503'
		ncfile.close()
	