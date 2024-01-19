from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from ttkwidgets import Table
from tkinter.colorchooser import *
from tkinter.filedialog import *
# from PIL import Image, ImageFont, ImageDraw
Customerdata = Tk()
Customerdata.title("Customer Data"),Customerdata.config(bg='#e1f5fe'),Customerdata.geometry("1200x800+300+100")

label1 = Label (Customerdata,bg="White", text = "รหัสลูกค้า :",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=20,y=10,width=120,height=30)
label1 = Label (Customerdata,bg="White", text = "ชื่อลูกค้า :",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=30,y=50,width=120,height=30)
custname= Entry(bg="White")#Qty
custname.place(x=100,y=55,width=150,height=20)
label1 = Label (Customerdata,bg="White", text = "บริษัท :",font=("Cordia New", 16),anchor="w",compound=LEFT).place(x=45,y=85,width=50,height=30)
compname= Entry(bg="White")#Qty
compname.place(x=100,y=90,width=300,height=20)
btnSearch =Button(Customerdata,foreground="#7b1fa2",bg="White",text="ตรวจสอบข้อมูล",font=("Cordia New", 16),compound=LEFT).place(x=410, y=40, width=100, height=70)
frame1 = Frame(Customerdata,bg="White").place(x=20,y=120,width=500,height=370)
btnExp =Button(Customerdata,foreground="#7b1fa2",bg='#e1f5fe',text="Export",font=("Cordia New", 16),compound=LEFT).place(x=20, y=120, width=50, height=50)

butonAdd =Button(Customerdata,foreground="#7b1fa2",bg="White",text="เพิ่มข้อมูล",font=("Cordia New", 16),width=10,height=1)
butonAdd.place(relx = 1,rely = 1.0,x=1,y=-150,anchor ='se') #ล็อคตำแหน่งไว้มุมขวาล่างของหน้าโปนแกรมตลอด
butonEdit =Button(Customerdata,foreground="#7b1fa2",bg="White",text="แก้ไขข้อมูล",font=("Cordia New", 16),width=10,height=1)
butonEdit.place(relx = 1,rely = 1.0,x=1,y=-50,anchor ='se')
butonDel =Button(Customerdata,foreground="#7b1fa2",bg="White",text="ลบรายการ",font=("Cordia New", 16),width=10,height=1)
butonDel.place(relx = 1,rely = 1.0,x=1,y=-100,anchor ='se')
butonClr =Button(Customerdata,foreground="#7b1fa2",bg="White",text="ล้างข้อมูล",font=("Cordia New", 16),width=10,height=1)
butonClr.place(relx = 1,rely = 1.0,x=1,y=1,anchor ='se')
frame2 = Frame(Customerdata,bg="White").place(x=600,y=120,width=500,height=370)
style = ttk.Style()
style.configure("Treeview", font=("Cordia New", 16))
lbf_Printer = LabelFrame(Customerdata, text='Printer List',font=("Cordia New", 16), bg='#e1f5fe', fg="#7b1fa2")
lbf_Printer.place(x=50, y=50, width=600, height=240)
scbary2 = Scrollbar(lbf_Printer, orient='vertical')
scbarx2 = Scrollbar(lbf_Printer, orient='horizontal')
Table2 = Tk.Treeview(lbf_Printer, height=18, columns=(1, 2, 3, 4), yscrollcommand=scbary2.set,
                          xscrollcommand=scbarx2.set)
Table2['show'] = 'headings'
scbary2.config(command=Table2.yview)
scbary2.pack(side=RIGHT, fill=Y)
scbarx2.config(command=Table2.xview)
scbarx2.pack(side=BOTTOM, fill=X)
Table2.pack(padx=1, pady=1)
Table2.column(1, width=150, anchor='n')
Table2.column(2, width=250, anchor='n')
Table2.column(3, width=100, anchor='n')
Table2.column(4, width=50, anchor='n')
Table2.heading(1, text='Printer Name')
Table2.heading(2, text='Path Printer')
Table2.heading(3, text='Room')

Customerdata.mainloop()