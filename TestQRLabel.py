import qrcode
from PIL import Image, ImageDraw, ImageFont
import json
# Function to generate QR code and create a labeled image
def generate_labeled_qr_code(data_to_encode, label_text, output_filename="labeled_qr_code.png"):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4,
    )
    qr.add_data,data_to_encode
    qr.make(fit=True)

    # Create an image from the QR code instance
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.show()
    # Create a labeled image with Pillow
    label_image = Image.new("RGB", (150,150), "white")
    draw = ImageDraw.Draw(label_image)

    # Paste the QR code onto the labeled image
    label_image.paste(qr_image, (0, 0))
    # Add label text below the QR code
    # Save the labeled image
    label_image=label_image.resize((100,100))
    label_image.save(output_filename)

# Example usage
name = "John"
age = 30
town = "New York"

data_to_encode  = name,age,town
label_text = "Scan QR Code"
generate_labeled_qr_code(data_to_encode, label_text)