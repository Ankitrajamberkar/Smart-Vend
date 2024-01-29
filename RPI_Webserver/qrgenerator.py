from flask import send_file
import qrcode

def generate_qrcode(name):

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(name)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image (you can also return the image directly without saving)
    img.save('static/qrcode.png')

    # Return the QR code image file path
    return send_file('static/qrcode.png', mimetype='image/png', as_attachment=True)

