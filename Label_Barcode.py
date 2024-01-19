from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import qrcode
from PIL import Image
from tkinter.colorchooser import *
from tkinter.filedialog import *
from PIL import Image, ImageFont, ImageDraw

WindowBarC = Tk()
WindowBarC.title("Customer Data Edit"),WindowBarC.config(bg='#e1f5fe'),WindowBarC.geometry("1200x700+300+100")
lbf_LPrint = LabelFrame(WindowBarC, text='1.รายการลาเบลที่พิมพ์แล้ว',font=("Cordia New", 16), bg='#e1f5fe', fg="#7b1fa2")
lbf_LPrint.place(x=30, y=30, width=800, height=200)
lbf_List = LabelFrame(WindowBarC, text='1.รายการสั่งพิมพ์ลาเบล',font=("Cordia New", 16), bg='#e1f5fe', fg="#7b1fa2")
lbf_List.place(x=30, y=30, width=800, height=200)

data = "Hello, World!"
qr = qrcode.QRCode(
    version=1,  # Adjust version as needed (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)
imgqr = qr.make_image(fill_color="black", back_color="white")

#lb_print =Label(image=imgqr)
imgqr.show()
WindowBarC.mainloop()