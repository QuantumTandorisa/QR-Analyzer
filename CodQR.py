import cv2
import hashlib
from pyzbar import pyzbar
import qrcode

def scan_qr_code(image_path):
    # Upload QR code image / Cargar la imagen del código QR
    image = cv2.imread(image_path)

    # Convert the image to grayscale / Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pyzbar library to scan QR code / Utilizar la biblioteca pyzbar para escanear el código QR
    qr_codes = pyzbar.decode(gray)

    if len(qr_codes) == 0:
        print("No se encontró ningún código QR en la imagen.")
        return

    # Iterate over the found QR codes / Iterar sobre los códigos QR encontrados
    for qr_code in qr_codes:
        # Get QR code content / Obtener el contenido del código QR
        qr_data = qr_code.data.decode('utf-8')

        # Verify the authenticity and integrity of the QR code / Verificar la autenticidad y la integridad del código QR
        if verify_qr_code(qr_data):
            print("El código QR es auténtico y no ha sido modificado.")
        else:
            print("El código QR ha sido modificado o no es auténtico.")

def verify_qr_code(qr_data):
    # Verify the source of the QR code (Example: verify if the URL contains a trusted domain) / Verificar la fuente del código QR (Ejemplo: verificar si la URL contiene un dominio confiable)
    if "miempresa.com" not in qr_data:
        return False

    # Validate a digital signature (Example: check if the QR code is digitally signed) / Validar una firma digital (Ejemplo: verificar si el código QR está firmado digitalmente)
    if not verify_signature(qr_data):
        return False

    # Compare with a trusted database (Example: check if the QR code is on a white list of authentic codes) / Comparar con una base de datos confiable (Ejemplo: verificar si el código QR está en una lista blanca de códigos auténticos)
    if not check_database(qr_data):
        return False

    # Validate the structure of the QR code (Example: check if the QR code complies with the ISO/IEC 18004 standard) / Validar la estructura del código QR (Ejemplo: verificar si el código QR cumple con el estándar ISO/IEC 18004)
    if not validate_qr_structure(qr_data):
        return False

    # Verify the integrity of the QR code (Example: calculate and compare the hash of the original content) / Verificar la integridad del código QR (Ejemplo: calcular y comparar el hash del contenido original)
    if not verify_integrity(qr_data):
        return False

    return True

def validate_qr_structure(qr_data):
    try:
        # Use the qrcode library to create a temporary QR code from the content of the scanned QR code / Utilizar la biblioteca qrcode para crear un código QR temporal a partir del contenido del código QR escaneado
        temp_qr = qrcode.QRCode()
        temp_qr.add_data(qr_data)
        temp_qr.make()

        #  Validate if the QR code complies with the structure of the ISO/IEC 18004 standard / Validar si el código QR cumple con la estructura del estándar ISO/IEC 18004
        temp_qr.validate()
        return True

    except qrcode.exceptions.VersionError:
        print("Error: El código QR no cumple con la versión del estándar ISO/IEC 18004.")
        return False

    except qrcode.exceptions.FormatError:
        print("Error: El código QR no cumple con el formato del estándar ISO/IEC 18004.")
        return False

    except qrcode.exceptions.DataOverflowError:
        print("Error: El código QR contiene datos que exceden la capacidad del estándar ISO/IEC 18004.")
        return False

def verify_integrity(qr_data):
    # Calculate the hash of the original content of the QR code / Calcular el hash del contenido original del código QR
    original_content_hash = calculate_hash(original_qr_data)

    # Calculate the hash of the content of the scanned QR code / Calcular el hash del contenido del código QR escaneado
    scanned_content_hash = calculate_hash(qr_data)

    # Compare the hashes / Comparar los hashes
    if original_content_hash != scanned_content_hash:
        return False

    return True

def calculate_hash(data):
    # Use a hash function (for example, SHA-256) to calculate the hash of the content / Utilizar una función de hash (por ejemplo, SHA-256) para calcular el hash del contenido
    hash_object = hashlib.sha256(data.encode('utf-8'))
    data_hash = hash_object.hexdigest()
    return data_hash

# Example of use / Ejemplo de uso
image_path = "ruta_de_la_imagen.png"  # Replace with the path of your image / Reemplaza con la ruta de tu imagen
scan_qr_code(image_path)
