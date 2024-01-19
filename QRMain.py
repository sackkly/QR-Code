from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from ttkwidgets import Table
from tkinter.colorchooser import *
from tkinter.filedialog import *
import qrcode
from PIL import Image,ImageTk, ImageDraw, ImageFont
import json
import ntplib
from time import ctime
from datetime import datetime
from tkcalendar import DateEntry
# from PIL import Image, ImageFont, ImageDraw
labelW = Tk()
canvas = Canvas()
labelW.title("Label QR Code")
# labelW.state('zoomed') #เต็มจอ
iconMain = tkinter.PhotoImage(file =r"ico/Books.PNG") #path style
labelW.iconphoto(False,iconMain)

Edit_ico = tkinter.PhotoImage(file =r"ico/edit2.png")
View_ico = tkinter.PhotoImage(file =r"ico/search.png") 
Del_ico = tkinter.PhotoImage(file =r"ico/del.png")
Save_ico = tkinter.PhotoImage(file =r"ico/Save.png")
icon = tkinter.PhotoImage(file = r"ico/Adfrm.png")

buton =Button(foreground="#7b1fa2",bg="White",text="Set Printer",font=("Cordia New",16),image=View_ico,compound=TOP).place(x=1, y=20, width= 100, height= 80)
buton =Button(foreground="#7b1fa2",bg="White",text="Create QR Code",font=("Cordia New",16),image=View_ico,compound=TOP).place(x=100, y=20, width= 130, height= 80)
buton =Button(foreground="#7b1fa2",bg="White",text="Calculator",font=("Cordia New",16),image=View_ico,compound=TOP).place(x=229, y=20, width= 100, height= 80)
buton =Button(foreground="#7b1fa2",bg="White",text="Add Item",font=("Cordia New",16),image=View_ico,compound=TOP).place(x=328, y=20, width= 100, height= 80)
buton =Button(foreground="#7b1fa2",bg="White",text="Exit",font=("Cordia New",16),image=View_ico,compound=TOP).place(x=427, y=20, width= 100, height= 80)
#buton =Button(foreground="#7b1fa2",bg="White",text="Create QE Code",image=View_ico,width=120,height=30,font=13,compound=LEFT).place(x=660,y=11)
#buton =Button(foreground="#7b1fa2",bg="White",text="Calculator",image=Save_ico,width=120,height=50,font=13,compound=LEFT).place(x=1200,y=0)
#buton =Button(foreground="#7b1fa2",bg="White",text="Add Item",image=Del_ico,width=120,height=50,font=13,compound=LEFT).place(x=1330,y=0)
#buton =Button(foreground="#7b1fa2",bg="White",text="Exit",image=Del_ico,width=120,height=50,font=13,compound=LEFT).place(x=1450,y=0)
Label(bg='#e1f5fe',text= "QR Code ID",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=110, width= 90, height= 20)
et5= Entry()
et5.config(bg="#afbfff")
et5.place(x=122, y=105, width= 500, height= 30)#.place(x=250,y=440,width=150,height=30)
et5.insert(0," ")

Label(bg='#e1f5fe',text= "User ID",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=145, width= 90, height= 20)
choice = StringVar (value=" ")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("Check 1","Check 2","Check 3","Check 4" ,"Check 5" ,"Check 6","Check 7")
combo.place(x=122, y=140, width= 200, height= 30)

def update_datetime():
    now = datetime.now()
    time =now.strftime("%H:%M:%S")
    Label(bg='#e1f5fe',text= time,font=("Tahoma",14), anchor="w", justify="left").place(x=330, y=140, width= 70, height= 30)#.place(x=420,y=440,width=70,height=30)
    labelW.after(1000, update_datetime) 

update_datetime()

def on_date_select():
    selected_date = cal.get_date()
    result_label.config(text=f"Selected Date: {selected_date}")
    
def Lb_IDno():
    Label(bg='#e1f5fe',text= "ID No.",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=180, width= 100, height= 20)
    et5= Entry()
    et5.config(bg="#afbfff")
    et5.place(x=122, y=175, width= 200, height= 30)#.place(x=250,y=440,width=150,height=30)
    et5.insert(0,"sack ")

cal = DateEntry(labelW, width=20, background='#e1f5fe', foreground='black', borderwidth=2)
cal.place(x=330, y=175, width= 100, height= 30)
select_button = tk.Button(labelW, text="Select Date", command=on_date_select)
result_label = tk.Label(labelW, text="Selected Date: ")
Lb_IDno()
def Lb_Lotno():
    Label(bg='#e1f5fe',text= "Lot No.",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=215, width= 100, height= 20)
    et6= Entry()
    et6.config(bg="#afbfff")
    et6.place(x=122, y=210, width= 100, height= 30)#.place(x=250,y=440,width=150,height=30)
    et6.insert(0," ")
Lb_Lotno()

Label(bg='white').place(x=450, y=145, width= 322, height= 170)
Label(bg='white').place(x=800, y=110, width= 500, height= 800)
lb_url = tk.Label(bg='white',url = "https://www.google.com").place(x=800, y=110, width= 300, height= 500)

def Lb_Supno():
    Label(bg='#e1f5fe',text= "Supplier Lot",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=250, width= 100, height= 20)
    et7= Entry()
    et7.config(bg="#afbfff")
    et7.place(x=122, y=245, width= 200, height= 30)#.place(x=250,y=440,width=150,height=30)
    et7.insert(0," ")
Lb_Supno()
Label(bg='#e1f5fe',text= "Part No.",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=285, width= 100, height= 20)
et8= Entry()
et8.config(bg="#afbfff")
et8.place(x=122, y=280, width= 200, height= 30)#.place(x=250,y=440,width=150,height=30)
et8.insert(0," ")
Label(bg='#e1f5fe',text= "Cav",font=("Tahoma",11), anchor="e", justify="right").place(x=330, y=285, width= 30, height= 20)
et9= Entry()
et9.config(bg="#afbfff")
et9.place(x=380, y=280, width= 50, height= 30)#.place(x=250,y=440,width=150,height=30)
et9.insert(5,"0")

Label(bg='#e1f5fe',text= "Lot Size",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=320, width= 100, height= 20)
et10= Entry()
et10.config(bg="#afbfff")
et10.place(x=122, y=315, width= 200, height= 30)#.place(x=250,y=440,width=150,height=30)
et10.insert(0,"-")

Label(bg='#e1f5fe',text= "Sub Lot",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=355, width= 100, height=20)
et11= Entry()
et11.config(bg="#afbfff")
et11.place(x=122, y=350, width= 200, height= 30)#.place(x=250,y=440,width=150,height=30)
et11.insert(0,"-")
Label(bg='#e1f5fe',text= "Unit",font=("Tahoma",11), anchor="e", justify="right").place(x=330, y=355, width= 30, height= 20)
choice = StringVar (value="pcs")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("Roll","pcs","Rolls")
combo.place(x=380, y=350, width= 50, height= 30)

Label(bg='#e1f5fe',text= "Invoice",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=390, width= 100, height= 20)
et12= Entry()
et12.config(bg="#afbfff")
et12.place(x=122, y=385, width= 200, height= 30)#.place(x=250,y=440,width=150,height=30)
invc= chr
invc = "TH60706521"
et12.insert(0,invc)

Label(bg='#e1f5fe',text= "Expire Date",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=425, width= 100, height= 20)
et13= Entry()
et13.config(bg="#afbfff")
et13.place(x=122, y=420, width= 100, height= 30)#.place(x=250,y=440,width=150,height=30)
exp_date= chr
exp_date = "2024-01-30"
et13.insert(0,exp_date)
Label(bg='#e1f5fe',text= "Find Part No",font=("Tahoma",11), anchor="w", justify="left").place(x=225, y=425, width= 100, height= 20)
et14= Entry()
et14.config(bg="#afbfff")
et14.place(x=330, y=420, width= 200, height= 30)
Seacrh_PartNo= chr
Seacrh_PartNo= "A 4-615720-A"
et14.insert(0,Seacrh_PartNo)

Label(bg='#e1f5fe',text= "Remark",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=460, width= 100, height= 20)
et15 =Entry()
et15.config(bg="#afbfff")
et15.place(x=122, y=455, width= 200, height= 30)#.place(x=250,y=440,width=150,height=30)
remark= chr
remark = "ssr"
et15.insert(0,remark)
Label(bg='#e1f5fe',text= "Print QTY",font=("Tahoma",11), anchor="w", justify="left").place(x=330, y=460, width= 70, height= 20)
et16= Entry()
et16.config(bg="#afbfff")
et16.place(x=410, y=455, width= 30, height= 30)#.place(x=250,y=440,width=150,height=30)
print_qty = int
print_qty = 1
et16.insert(0,print_qty)

Label(bg='#e1f5fe',text= "Part Name",font=("Tahoma",11), anchor="e", justify="right").place(x=5, y=500, width= 100, height= 30)
et17= Entry()
et17.config(bg="#afbfff")
et17.place(x=122, y=495, width= 100, height= 30)#.place(x=250,y=440,width=150,height=30)
partname= chr
partname = "A 4-602175-F"
et17.insert(0,partname)  

alldata = invc + partname #test + Str
print(alldata)
et18= Entry()
et18.config(bg="#afbfff")
et18.place(x=5, y=540, width= 100, height= 30)#.place(x=250,y=440,width=150,height=30)
et18.insert(0,alldata)  

# label3 = tk.Label(bg='#e1f5fe').place(x=750,y=70,width=500,height=300)
def generate_labeled_qr_code(data, label_text):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=2,
        border=4,
    )
    qr.add_data(data)
    qr.make()#fit=True

    # Create an image from the QR code instance
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Convert the PIL image to a Tkinter PhotoImage
    tk_image = ImageTk.PhotoImage(qr_image)

    # Create Tkinter window

    # Create and place a Label with the QR code image
    labelQbar = tk.Label(labelW,bg='white', text=label_text, image=tk_image, compound="top")
    # label1 = tk.Label(labelW, text=label_text, image=tk_image, compound="top")
    labelQbar.image = tk_image  # Keep a reference to avoid garbage collection
    # label1.place(x=20,y=20,width=100,height=100)
    labelQbar.place(x=450,y=140,width=100,height=100)
    
data = alldata
label_text = "QR Code"
generate_labeled_qr_code(data, label_text)

labelW.geometry("1080x720+450+200")
labelW.configure(bg='#e1f5fe')
labelW.mainloop()

