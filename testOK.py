import tkinter as tk
from PIL import Image, ImageTk
import qrcode
root = tk.Tk()
root.title("QR Code Display")
def generate_labeled_qr_code(data, label_text):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Convert the PIL image to a Tkinter PhotoImage
    tk_image = ImageTk.PhotoImage(qr_image)

    # Create Tkinter window

    # Create and place a Label with the QR code image
    label1 = tk.Label(root, text=label_text, image=tk_image, compound="top")
    label1.image = tk_image  # Keep a reference to avoid garbage collection
    label1.place(x=20,y=20,width=100,height=100)
    # pack(pady=5)

    # Run the Tkinter event loop
    root.mainloop()

# Example usage
data_to_encode = "https://www.example.com"
label_text = "Scan QR Code"
generate_labeled_qr_code(data_to_encode, label_text)
