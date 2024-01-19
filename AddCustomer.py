from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *
# from PIL import Image, ImageFont, ImageDraw
Customerfrm = Tk()
Customerfrm.title("Customer Data Edit"),Customerfrm.config(bg='#e1f5fe'),Customerfrm.geometry("1200x720+300+100")

label1 = Label (Customerfrm,bg="White", text = "รหัสลูกค้า :",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=20,y=10,width=120,height=30)
label1 = Label (Customerfrm,bg="White", text = "ชื่อลูกค้า :",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=30,y=50,width=120,height=30)
custname= Entry(bg="White")#Qty
custname.place(x=100,y=55,width=150,height=20)
label1 = Label (Customerfrm,bg="White", text = "บริษัท :",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=45,y=85,width=50,height=30)
compname= Entry(bg="White")#Qty
compname.place(x=100,y=90,width=300,height=20)
btnSearch =Button(Customerfrm,foreground="#7b1fa2",bg="White",text="ตรวจสอบข้อมูล",font=("Cordia New", 16),compound=LEFT).place(x=410, y=40, width=100, height=70)
frame1 = Frame(Customerfrm,bg="White").place(x=20,y=120,width=500,height=370)
btnExp =Button(Customerfrm,foreground="#7b1fa2",bg='#e1f5fe',text="Export",font=("Cordia New", 16),compound=LEFT).place(x=20, y=120, width=50, height=50)

butonAdd =Button(Customerfrm,foreground="#7b1fa2",bg="White",text="เพิ่มข้อมูล",font=("Cordia New", 16),width=10,height=1)
butonAdd.place(relx = 1,rely = 1.0,x=1,y=-150,anchor ='se') #ล็อคตำแหน่งไว้มุมขวาล่างของหน้าโปนแกรมตลอด
butonEdit =Button(Customerfrm,foreground="#7b1fa2",bg="White",text="แก้ไขข้อมูล",font=("Cordia New", 16),width=10,height=1)
butonEdit.place(relx = 1,rely = 1.0,x=1,y=-50,anchor ='se')
butonDel =Button(Customerfrm,foreground="#7b1fa2",bg="White",text="ลบรายการ",font=("Cordia New", 16),width=10,height=1)
butonDel.place(relx = 1,rely = 1.0,x=1,y=-100,anchor ='se')
butonClr =Button(Customerfrm,foreground="#7b1fa2",bg="White",text="ล้างข้อมูล",font=("Cordia New", 16),width=10,height=1)
butonClr.place(relx = 1,rely = 1.0,x=1,y=1,anchor ='se')
Customerfrm.mainloop()