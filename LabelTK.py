from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *
# from PIL import Image, ImageFont, ImageDraw
# def LabelTkFrm() :
Labeltk = Tk()
Labeltk.title("LabelTokyo"),Labeltk.config(bg="White"),Labeltk.geometry("1200x800+300+100")
butonS =Button(Labeltk,foreground="#7b1fa2",bg="White",text="ค้นหา",font=("Cordia New", 16),compound=LEFT,relief=RAISED,cursor="heart").place(x=3, y=1, width=100, height=30) #picsize 50*50
butonV =Button(Labeltk,foreground="#7b1fa2",bg="White",text="View Data",font=("Cordia New", 16),compound=LEFT).place(x=410, y=1, width=100, height=30) #picsize 50*50
butonOK =Button(Labeltk,foreground="#7b1fa2",bg="White",text="ตกลง",font=("Cordia New", 16),width=10,height=1)
butonOK.place(relx = 1,rely = 0.0,x=-90,anchor ='ne')
butonC =Button(Labeltk,foreground="#7b1fa2",bg="White",text="ยกเลิก",font=("Cordia New", 16),width=10,height=1)
butonC.place(relx = 1,rely = 0.0,x=1,anchor ='ne') #ล็อคตำแหน่งไว้มุมขวาบนของหน้าโปนแกรมตลอด
frame1 = Frame(Labeltk,bg="white",highlightbackground="black", highlightthickness=1).place(x=20,y=60,width=450,height=250)
frame2 = Frame(Labeltk,bg="white",highlightbackground="black", highlightthickness=1).place(x=480,y=60,width=500,height=250)
label1 = Label (frame1,bg="White", text = "Date / Sign :",font=("Cordia New", 16),anchor="w",justify="left").place(x=25,y=70,width=80,height=30)
label1 = Label (frame1,bg="White", text = "Name :",font=("Cordia New", 16),anchor="w",justify="left").place(x=25,y=100,width=80,height=30)
label1 = Label (frame1,bg="White", text = "Lot No. :",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=25,y=130,width=80,height=30)
label1 = Label (frame1,bg="White", text = "Item No. :",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=25,y=160,width=80,height=30)
label1 = Label (frame1,bg="White", text = "Q'ty :",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=25,y=190,width=80,height=30)

# ใส่ LOG Vel
etryS= Entry(bg='#e1f5fe')
etryS.place(x=210,y=5,width=200,height=20)
etry1= Entry(bg='#e1f5fe')
etry1.place(x=120,y=75,width=100,height=20)
etry2= Entry(bg='#e1f5fe')#Lot No.
etry2.place(x=120,y=135,width=200,height=20)
etry3= Entry(bg='#e1f5fe')#Item No.
etry3.place(x=120,y=165,width=300,height=20)
etry4= Entry(bg='#e1f5fe')#Qty
etry4.place(x=120,y=195,width=100,height=20)


choiceS = StringVar (value=" ")
comboS = ttk.Combobox(textvariable=choiceS)
comboS["values"] = ("Part Code","Part Name","Customers")
comboS.place(x=105,y=1,width=100,height=30)

choice1 = StringVar (value=" ")
combo1 = ttk.Combobox(textvariable=choice1)
combo1["values"] = ("Sack","P'F","P'Tungz")
combo1.place(x=120,y=105,width=150,height=20)

choice2 = StringVar (value=" ",)
combo2 = ttk.Combobox(textvariable=choice2)
combo2["values"] = ("7 ช่อง","8 ช่อง","9 ช่อง","10 ช่อง","ว่าง")
combo2.place(x=325,y=135,width=70,height=20)

choice3 = StringVar (value=" ")
combo3 = ttk.Combobox(textvariable=choice3)
combo3["values"] = ("Roll","pcs","Rolls")
combo3.place(x=240,y=195,width=70,height=20)

# outside Frame
label1 = Label (frame1,bg="White", text = "จำนวนลาเบล :",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=20,y=320,width=120,height=30)
num_print= Entry(bg='#e1f5fe')#Qty
num_print.place(x=120,y=325,width=70,height=20)
label1 = Label (frame1,bg="White", text = "แผ่น",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=195,y=320,width=50,height=30)

btnPrint =Button(Labeltk,foreground="#7b1fa2",bg="White",text="พิมพ์ลาเบล",font=("Cordia New", 16),compound=LEFT).place(x=120, y=360, width=100, height=40) #picsize 50*50
btnPrint =Button(Labeltk,foreground="#7b1fa2",bg="White",text="ลบรายการ",font=("Cordia New", 16),compound=LEFT).place(x=230, y=360, width=100, height=40) #picsize 50*50
# C2 = Checkbutton(frame1, text = "Video", width=200, anchor="w")
# C2.pack(padx=10, pady=10)

Labeltk.mainloop()