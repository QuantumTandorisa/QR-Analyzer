import qrcode

# Contenido que deseas codificar en el QR
original_qr_data = "Hola, este es un codigo QR de ejemplo."

# Crear un objeto QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Añadir los datos al QRCode
qr.add_data(original_qr_data)
qr.make(fit=True)

# Crear una imagen QR en formato PNG
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen como un archivo PNG
img.save("codigo_qr.png")
