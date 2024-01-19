from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *
from PIL import Image, ImageFont, ImageDraw
labelW = Tk()
canvas = Canvas()
labelW.title("LabelBig")
label1 =LabelFrame(text="tt").place(x=10,y=1000)
# labelW.state('zoomed') #เต็มจอ
iconMain = tkinter.PhotoImage(file =r"ico/Books.PNG") #path style
labelW.iconphoto(False,iconMain)

Edit_ico = tkinter.PhotoImage(file =r"ico/edit2.png")
View_ico = tkinter.PhotoImage(file =r"ico/search.png") 
Del_ico = tkinter.PhotoImage(file =r"ico/del.png")
Save_ico = tkinter.PhotoImage(file =r"ico/Save.png")
icon = tkinter.PhotoImage(file = r"ico/Adfrm.png")
# imgcon = tkinter.PhotoImage

buton =Button(foreground="#7b1fa2",bg="White",text="ค้นหา",font=("Cordia New",16),image=View_ico,compound=LEFT).grid(row=0,column=0,padx=(0,0),pady=(0,20))

# Label(bg='#e1f5fe',height=2,image=View_ico,compound=LEFT).grid(row=0,column=1,padx=(3,1),pady=(0,20))
choice = StringVar (value=" ")
combo = ttk.Combobox(textvariable=choice,font=("Cordia New",16))
combo["values"] = ("Part Code","Part Name","Customer Code")
combo.place(x=100,y=16,width=150,height=35)
# if combo == "part code" :
# #    imgcon = Edit_ico
#    Label(bg='#e1f5fe',image=Edit_ico,height=2,image=View_ico,compound=LEFT).grid(row=0,column=1,padx=(3,1),pady=(0,20))
# elif combo == "part Name":
# #    imgcon = Del_ico
#    Label(bg='#e1f5fe',image=Edit_ico,height=2,image=Del_ico,compound=LEFT).grid(row=0,column=1,padx=(3,1),pady=(0,20))
# else :
    # imgcon = Save_ico
    # Label(bg='#e1f5fe',image=Edit_ico,height=2,image=Save_ico,compound=LEFT).grid(row=0,column=1,padx=(3,1),pady=(0,20))
et3= Entry()
et3.place(x=350,y=16,width=300,height=30)
et3.insert(0," ")
buton =Button(foreground="#7b1fa2",bg="White",text="แสดงข้อมูล",image=View_ico,width=120,height=30,font=13,compound=LEFT).place(x=660,y=11)
buton =Button(foreground="#7b1fa2",bg="White",text="ตกลง",image=Save_ico,width=120,height=50,font=13,compound=LEFT).place(x=1200,y=0)
buton =Button(foreground="#7b1fa2",bg="White",text="ยกเลิก",image=Del_ico,width=120,height=50,font=13,compound=LEFT).place(x=1330,y=0)

# canvas.create_rectangle(10,10,110,110,outline ="black",fill ="white",width = 2)
# canvas.create_rectangle(210,10,310,210,outline ="black",fill ="white",width =2)
# canvas.place(x= 150,y=200)  วาด4 เหลี่ยม
#Row1
Label(bg='white',width=90,height=23,compound=LEFT).place(x=100,y=300)
Label(bg='#e1f5fe',text= "Vendor",font=("Tahoma",12),compound=LEFT).place(x=130,y=325)
Label(bg='#e1f5fe',text= "Vel Suede (Thailand) Co., Ltd.",font=("Tahoma",12),height=2,compound=LEFT).place(x=250,y=310)
#Row2
Label(bg='#e1f5fe',text= "Part Code",font=("Tahoma",12),compound=LEFT).place(x=130,y=370)
et1= Entry()
et1.config(bg="#b2dfdb")
et1.place(x=250,y=360,width=450,height=30)
et1.insert(0," ")
Label(bg='#e1f5fe',text= "Sub Code",font=("Tahoma",12),compound=LEFT).place(x=130,y=405)
et2= Entry()
et2.config(bg="#afbfff")
et2.place(x=250,y=400,width=250,height=30)
et2.insert(0," ")
#Row3
Label(bg='#e1f5fe',text= "Lot Rev",font=("Tahoma",12),compound=LEFT).place(x=530,y=405)
et4= Entry()
et4.config(bg="#afbfff")
et4.place(x=630,y=400,width=70,height=30)
et4.insert(0," ")
#Row4
Label(bg='#e1f5fe',text= "Q'ty",font=("Tahoma",12),compound=LEFT).place(x=130,y=445)
et5= Entry()
et5.config(bg="#afbfff")
et5.place(x=250,y=440,width=150,height=30)
et5.insert(0," ")
choice = StringVar (value=" ")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("Roll","pcs","Rolls")
combo.place(x=420,y=440,width=70,height=30)
Label(bg='#e1f5fe',text= "Drawing No.",font=("Tahoma",12),compound=LEFT).place(x=530,y=445)
et6= Entry()
et6.config(bg="#afbfff")
et6.place(x=630,y=440,width=70,height=30)
et6.insert(0," ")
#Row5
Label(bg='#e1f5fe',text= "Lot No.",font=("Tahoma",12),compound=LEFT).place(x=130,y=485)
et7= Entry()
et7.config(bg="#afbfff")
et7.place(x=250,y=480,width=250,height=30)
et7.insert(0," ")
choice = StringVar (value=" ")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("ว่าง","7 ช่อง","8 ช่อง","9 ช่อง","10 ช่อง")
combo.place(x=530,y=480,width=70,height=30)
Label(bg='#e1f5fe',text= "Normal",font=("Tahoma",12),compound=LEFT).place(x=630,y=485)
#Row6
Label(bg='#e1f5fe',text= "Date / Sign",font=("Tahoma",12),compound=LEFT).place(x=130,y=530)
et8= Entry()
et8.config(bg="#afbfff")
et8.place(x=250,y=520,width=150,height=30)
et8.insert(0," ")
Label(bg='#e1f5fe',text= "Inchager",font=("Tahoma",12),compound=LEFT).place(x=430,y=525)
choice = StringVar (value=" ")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("AMPORN","NITTAYA","NISACHON","PITAK","SAKSIT")
combo.place(x=510,y=520,width=150,height=30)
#Row7
Label(bg='#e1f5fe',text= "Expire Date",font=("Tahoma",12),compound=LEFT).place(x=130,y=570)
choice = StringVar (value=" ")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("AMPORN","NITTAYA","NISACHON","PITAK","SAKSIT")
combo.place(x=250,y=560,width=150,height=30)
ch1=Checkbutton(bg='#e1f5fe',text="Lot try",font=("Tahoma",12)).place(x=500,y=560,width=100,height=30)
ch2=Checkbutton(bg='#e1f5fe',text="เช็คข้อมูล",font=("Tahoma",12)).place(x=600,y=560,width=100,height=30)

#Row8
Label(bg='#e1f5fe',text= "ผู้พิมพ์ลาเบล",font=("Tahoma",12),compound=LEFT).place(x=130,y=670)
choice = StringVar (value=" ")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("AMPORN","NITTAYA","NISACHON","PITAK","SAKSIT")
combo.place(x=230,y=665,width=150,height=30)
buton =Button(foreground="#7b1fa2",bg="#e1f5fe",text="พิมพ์ลาเบล",image=View_ico,width=140,height=40,font=("Tahoma",12),compound=LEFT).place(x=400,y=660)
buton =Button(foreground="#7b1fa2",bg="#e1f5fe",text="ลบรายการ",image=Save_ico,width=140,height=40,font=("Tahoma",12),compound=LEFT).place(x=550,y=660)
#Row9
Label(bg='#e1f5fe',text= "จำนวนลาเบล",font=("Tahoma",12),compound=LEFT).place(x=130,y=710)
et9= Entry()
et9.config(bg="#afbfff")
et9.place(x=230,y=705,width=100,height=30)
et9.insert(0," ")
Label(bg='#e1f5fe',text= "แผ่น",font=("Tahoma",12),compound=LEFT).place(x=340,y=710)
# Radiobutton
#Row10
Label(bg='#e1f5fe',text= "เครื่องปริ้นท์",font=("Tahoma",12),compound=LEFT).place(x=130,y=745)
choice = StringVar (value=" ")
combo = ttk.Combobox(textvariable=choice)
combo["values"] = ("Check-10","Check-8","Check-9","Check-6","Check-5")
combo.place(x=230,y=740,width=150,height=30)
buton =Button(foreground="#7b1fa2",bg="#e1f5fe",text="บันทึกรายการ",height=2,font=("Tahoma",12),compound=LEFT).place(x=400,y=720)
buton =Button(foreground="#7b1fa2",bg="#e1f5fe",text="Barcode",height=2,font=("Tahoma",12),compound=LEFT).place(x=550,y=720)
#Row11
Label(bg='#e1f5fe',text= "ชื่อเครื่อง",font=("Tahoma",12),compound=LEFT).place(x=130,y=785)
et10= Entry()
et10.config(bg="#afbfff")
et10.place(x=230,y=780,width=150,height=30)
et10.insert(0,"Computer Name")
radi1 = Radiobutton (bg='#e1f5fe',text="ปริ้นท์แบบมีบาร์โค้ด",font=("Tahoma",10)).place(x=385,y=780,width=160,height=30)
radis2 = Radiobutton (bg='#e1f5fe',text="ปริ้นท์ไม่มีบาร์โค้ด",font=("Tahoma",10)).place(x=535,y=780,width=160,height=30)

#list Label
labelframe = LabelFrame(labelW, text="This is a LabelFrame")
labelframe.place(x=790,y=1000)
left = Label(labelframe, text="Inside the LabelFrame")
left.place(x=800,y=1000)
Label(bg='#e1f5fe',text= "รายการลาเบลที่พิมพ์แล้ว",font=("Tahoma",10),compound=LEFT).place(x=800,y=80)
Label(bg='white',width=70,height=15,compound=LEFT).place(x=800,y=100)
buton =Button(foreground="#7b1fa2",bg="#e1f5fe",text="ดู..",width=2,height=1,font=("Tahoma",12),compound=LEFT).place(x=801,y=101)


#list Label2
Label(bg='#e1f5fe',text= "รายการลาเบลที่พิมพ์แล้ว",font=("Tahoma",10),compound=LEFT).place(x=800,y=350)
Label(bg='white',width=70,height=15,compound=LEFT).place(x=800,y=370)
buton =Button(foreground="#7b1fa2",bg="#e1f5fe",text="ดู..",width=2,height=1,font=("Tahoma",12),compound=LEFT).place(x=801,y=371)

#list Label3
Label(bg='white',width=50,height=10,compound=LEFT).place(x=870,y=620)
# Label(bg='#e1f5fe',text= "รายการลาเบลที่พิมพ์แล้ว",font=("Tahoma",10),compound=LEFT).place(x=800,y=350)

buton =Button(foreground="#7b1fa2",bg="#e1f5fe",text="พิมพ์ข้อความนี้",width=15,height=1,font=("Tahoma",12),compound=LEFT).place(x=970,y=790)


labelW.geometry("1480x860+250+100")
labelW.configure(bg='#e1f5fe')
labelW.mainloop()
