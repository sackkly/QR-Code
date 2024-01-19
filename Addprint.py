from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *
from PIL import Image, ImageFont, ImageDraw
def Add_Print():
    AddPrinter = Toplevel()
    AddPrinter.title("Printer Info"),AddPrinter.config(bg="White"),AddPrinter.geometry("800x600+300+100")
    buton =Button(AddPrinter,foreground="#7b1fa2",bg="White",text="เพิ่ม Priner",font=("Cordia New", 16),compound=LEFT).place(x=3, y=1, width=100, height=30) #picsize 50*50
    buton =Button(AddPrinter,foreground="#7b1fa2",bg="White",text="แก้ไข",font=("Cordia New", 16),compound=LEFT).place(x=104, y=1, width=100, height=30)
    buton =Button(AddPrinter,foreground="#7b1fa2",bg="White",text="ลบข้อมูล",font=("Cordia New", 16),compound=LEFT).place(x=205, y=1, width=100, height=30)
    buton =Button(AddPrinter,foreground="#7b1fa2",bg="White",text="ตกลง",font=("Cordia New", 16),compound=LEFT).place(x=600, y=1, width=100, height=30) #picsize 50*50
    buton =Button(AddPrinter,foreground="#7b1fa2",bg="White",text="ยกเลิก",font=("Cordia New", 16),compound=LEFT).place(x=700, y=1, width=100, height=30)

    style = ttk.Style()
    style.configure("Treeview", font=("Cordia New", 16))
    lbf_Printer = LabelFrame(AddPrinter, text='Printer List',font=("Cordia New", 16), bg='#e1f5fe', fg="#7b1fa2")
    lbf_Printer.place(x=50, y=50, width=600, height=240)
    scbary2 = Scrollbar(lbf_Printer, orient='vertical')
    scbarx2 = Scrollbar(lbf_Printer, orient='horizontal')
    Table2 = ttk.Treeview(lbf_Printer, height=18, columns=(1, 2, 3, 4), yscrollcommand=scbary2.set,
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
    Table2.heading(4, text='Referance')
    label1 =Label(AddPrinter,bg='#e1f5fe',text="Path Printer:",font=("Cordia New", 16),compound=LEFT).place(x=100, y=300, width=100, height=30)
    et1= Entry(AddPrinter)
    et1.config(bg="#afbfff")
    et1.place(x=210,y=300,width=200,height=30)
    et1.insert(0,"f ")

    label2 =Label(AddPrinter,bg='#e1f5fe',text="Room:",font=("Cordia New", 16),compound=LEFT).place(x=130, y=350, width=70, height=30)
    et2= Entry(AddPrinter)
    et2.config(bg="#afbfff")
    et2.place(x=210,y=350,width=100,height=30)
    et2.insert(0," f")
    AddPrinter.mainloop()

# frm2 = Frame(AddPrinter)
# frm2.place(x=690, y=340, width=650, height=320)


