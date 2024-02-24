# -*- coding: utf-8 -*-

import getpass
from pyicloud import PyiCloudService

# Ingresa tu correo electrónico y contraseña de iCloud
username = input("Ingresa tu correo de iCloud: ")
password = getpass.getpass("Ingresa tu contraseña de iCloud: ")

# Inicia sesión en iCloud
api = PyiCloudService(username, password)

# Obtiene la lista de dispositivos asociados a tu cuenta
devices = api.devices

if devices:
    # Tomamos el primer dispositivo de la lista (normalmente es el principal)
    device = devices[0]
    
    # Obtenemos la ubicación del dispositivo
    location = device.location()
    
    if location:
        # Obtenemos la latitud y longitud
        latitude = location['latitude']
        longitude = location['longitude']
        
        # Generamos el enlace a Google Maps
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        
        # Imprimimos el enlace
        print("Ubicación encontrada:")
        print("Latitud:", latitude)
        print("Longitud:", longitude)
        print("Precisión:", location['horizontalAccuracy'])
        print("Enlace a Google Maps:", google_maps_link)
    else:
        print("No se pudo obtener la ubicación del dispositivo.")
else:
    print("No se encontraron dispositivos asociados a tu cuenta.")