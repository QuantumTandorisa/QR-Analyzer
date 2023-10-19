# -*- coding: utf-8 -*-
'''
   ____    ____        ___                __                     
  / __ \  / __ \      /   |  ____  ____ _/ /_  ______  ___  _____
 / / / / / /_/ /_____/ /| | / __ \/ __ `/ / / / /_  / / _ \/ ___/
/ /_/ / / _, _/_____/ ___ |/ / / / /_/ / / /_/ / / /_/  __/ /    
\___\_\/_/ |_|     /_/  |_/_/ /_/\__,_/_/\__, / /___/\___/_/     
                                        /____/                   
'''                                        
############################################################
#   QR-Analyzer.py
#
# QR Analyzer is a tool that allows you to generate and 
# analyze QR codes. You can use this tool to create QR 
# codes with specific content and then verify if the 
# scanned QR codes are authentic and have not been modified.
# I clarify this tool to this day is very simple, the idea
# is to study and understand the functionality to create 
# a functional and competent tool to any QR scanning.
#
#
# 10/18/23 - Changed to Python3 (finally)
#
# Author: Facundo Fernandez 
#
#
############################################################

import cv2
from pyzbar.pyzbar import decode

# Define el contenido original
original_qr_data = "Hola, este es un codigo QR de ejemplo."

def scan_qr_code(image_path):
    try:
        image = cv2.imread(image_path)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qr_codes = decode(gray)

    if not qr_codes:
        print("No se encontró ningún código QR en la imagen.")
        return

    for qr_code in qr_codes:
        qr_data = qr_code.data.decode('utf-8')
        print(f"Contenido del código QR: {qr_data}")
        if qr_data == original_qr_data:
            print("El código QR es auténtico y no ha sido modificado.")
        else:
            print("El código QR ha sido modificado o no es auténtico.")

# Example of use
image_path = "codigo_qr.png"
scan_qr_code(image_path)

