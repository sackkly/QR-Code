from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *
# from PIL import Image, ImageFont, ImageDraw
from Addprint import*
from Addprint import Add_Print

root = Tk()
root.title ("เพิ่มรายการลาเบล")
iconMain = tkinter.PhotoImage(file =r"ico/edit2.png")
root.iconphoto(False,iconMain)
#ALLIcon
Edit_ico = tkinter.PhotoImage(file =r"ico/edit2.png")
View_ico = tkinter.PhotoImage(file =r"ico/search.png") 
Del_ico = tkinter.PhotoImage(file =r"ico/del.png")
Save_ico = tkinter.PhotoImage(file =r"ico/Save.png")
icon = tkinter.PhotoImage(file = r"ico/Adfrm.png")

# def Addprinter():
# photo = PhotoImage(file = r"C:\New folder\Adfrm.png")
buton =Button(foreground="#7b1fa2",bg="White",text="เพิ่มรายการ",font=("Tahoma",13),image=icon,compound=LEFT,command=Add_Print).grid(row=0,column=0,padx=(0,0),pady=(0,20))  #picsize 50*50
buton =Button(foreground="#7b1fa2",bg="White",text="แก้ไขข้อมูล",font=("Tahoma",13),image=Edit_ico,compound=LEFT).grid(row=0,column=1,padx=(0,0),pady=(0,20))
buton =Button(foreground="#7b1fa2",bg="White",text="ลบข้อมูล",font=("Tahoma",13),image=Del_ico,compound=LEFT).grid(row=0,column=2,padx=(0,0),pady=(0,20))
buton =Button(foreground="#7b1fa2",bg="White",text="ค้นหา",font=("Tahoma",13),image=View_ico,compound=LEFT).grid(row=0,column=3,padx=(0,0),pady=(0,20))
choice = StringVar (value="เลือกรหัส")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("0","1")
combo.place(x=520,y=20,width=200,height=30)
et3= Entry()
et3.place(x=740,y=20,width=200,height=30)
et3.insert(0," ")
buton =Button(foreground="#7b1fa2",bg="White",text="แสดงข้อมูล",image=View_ico,width=120,height=30,font=13,compound=LEFT).place(x=950,y=15)
buton =Button(foreground="#7b1fa2",bg="White",text="ตกลง",image=Save_ico,width=120,height=50,font=13,compound=LEFT).place(x=1200,y=0)
buton =Button(foreground="#7b1fa2",bg="White",text="ยกเลิก",image=Del_ico,width=120,height=50,font=13,compound=LEFT).place(x=1330,y=0)

Label(bg='#e1f5fe',height=2,text="Part Code ชื่อรุ่น",font=20).place(x=50,y= 100 )
Label(bg='#e1f5fe',height=2,text="Part Name ชื่อโมเดล",font=20).place(x=50,y= 130 )
Label(bg='#e1f5fe',height=2,text="Customer ชื่อลูกค้า",font=20).place(x=50,y= 160 )
Label(bg='#e1f5fe',height=2,text="Location ชื่อต่อท้าย",font=20).place(x=50,y= 190 )
Label(bg='#e1f5fe',height=2,text="Rev_drawing No.",font=20).place(x=50,y= 220 )
Label(bg='#e1f5fe',height=2,text="SignClean",font=20).place(x=50,y= 250 )
Label(bg='#e1f5fe',height=2,text="ID รหัสลูกค้า",font=20).place(x=50,y= 280 )

et1= Entry()
et1.place(x=200,y= 110,width=300,height=20)
et4= Entry()
et4.place(x=200,y=140,width=300,height=20)

et5= Entry()
et5.place(x=200,y=170,width=200,height=20)
et5.insert(0,"")
et6= Entry()
et6.place(x=200,y=200,width=200,height=20)
et6.insert(0,"")
et7= Entry()
et7.place(x=200,y=230,width=50,height=20)
et7.insert(0," ")
choice = StringVar (value="เลือกรหัส")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("0","1")
combo.place(x=200,y=260,width=50,height=20)
Label(text="( 0 = False).( 1 = True )").place(x=250,y=260)
et9= Entry()
et9.place(x=200,y=290,width=50,height=20)
et9.insert(0," ")
btn_CodeCus =Button(foreground="#7b1fa2",bg="White",text="แสดงรหัส",width=10,height=1,font= 2,compound=LEFT).place(x=260,y=285)

root.geometry("1580x860")
root.configure(bg='#e1f5fe')
root.mainloop()

