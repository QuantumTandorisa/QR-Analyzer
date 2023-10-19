QR Analyzer es una herramienta que permite generar y analizar códigos QR. Usted puede utilizar esta herramienta para crear códigos QR con contenido específico y luego verificar si los códigos QR escaneados son auténticos y no han sido modificados.
Aclaro esta herramienta hasta el día de hoy es muy simple, la idea es estudiar y entender la funcionalidad para crear una herramienta funcional y competente para cualquier escaneo de QR.

## Características

- Guardar Información Adicional: Además de verificar si el código QR ha sido modificado, podrías permitir que los usuarios almacenen información adicional en el código QR, como metadatos o una descripción relacionada con el contenido
- Generar Códigos QR con Datos Variables.

## Requisitos

- Bibliotecas requeridas, que puedes instalar ejecutando `pip install -r requirements.txt`.
- pip install pyzbar qrcode opencv-python

## Uso

- Clona este repositorio en tu máquina local.
- Ejecuta la aplicación con Python 3.9 o superior: `python3 GenerateTset.py`.
- Generar un Código QR
- Ejecuta la aplicación con Python 3.9 o superior: `QR-Analyzer.py`.

## Configuración de API

Puedes personalizar el contenido del código QR modificando la variable original_qr_data en los scripts `GenerateTset.py` y `QR-Analyzer.py`.
