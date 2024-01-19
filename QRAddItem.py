import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from ttkwidgets import Table
from tkinter.colorchooser import *
from tkinter.filedialog import *
from tkinter import *
root = tk.Tk()
root.title('Treeview demo')
root.geometry('1020x720+500+200')

# frame1 = Frame(root,bg="White").place(x=60,y=80,width=200,height=200)
style = ttk.Style()
style.configure("Treeview", font=("Cordia New", 18))
lbf_Printer = LabelFrame(root, text='Add Item',font=("Cordia New", 18), bg='#e1f5fe', fg="#7b1fa2")
lbf_Printer.place(x=20, y=20, width=250, height=350)
lb1=Label(lbf_Printer,text='Code',font=("Cordia New", 18), bg='#e1f5fe', fg="#7b1fa2").place(x=20, y=0)
et1= Entry(lbf_Printer)
et1.config(bg="#afbfff",font=("Cordia New", 16))
et1.place(x=20, y=30,width=70)#.place(x=250,y=440,width=150,height=30)
code= chr
code = "I0111"
et1.insert(0,code)
lb1=Label(lbf_Printer,text='Part No',font=("Cordia New", 18), bg='#e1f5fe', fg="#7b1fa2").place(x=20, y=75)
et1= Entry(lbf_Printer)
et1.config(bg="#afbfff",font=("Cordia New", 16))
et1.place(x=20, y=105,width=150)#.place(x=250,y=440,width=150,height=30)
partno = chr
partno = "A 4-62175-F"
et1.insert(0,partno)
lb1=Label(lbf_Printer,text='Part Name',font=("Cordia New", 18), bg='#e1f5fe', fg="#7b1fa2").place(x=20, y=155)
et1= Entry(lbf_Printer)
et1.config(bg="#afbfff",font=("Cordia New", 16))
et1.place(x=20, y=185,width=150)#.place(x=250,y=440,width=150,height=30)
partna = chr
partna = "FELT"
et1.insert(0,partna)
lb1=Label(lbf_Printer,text='Status',font=("Cordia New", 18), bg='#e1f5fe', fg="#7b1fa2").place(x=20, y=235)
et1= Entry(lbf_Printer)
et1.config(bg="#afbfff",font=("Cordia New", 16))
et1.place(x=20, y=265,width=150)#.place(x=250,y=440,width=150,height=30)
stat = chr
stat = "1"
et1.insert(0,stat)

button = Button (root,text="Update New Item",font=("Cordia New", 16), bg='#e1f5fe', fg="#7b1fa2").place(x=40,y=380,height=70,width=220)
# frame2 = Frame(root,bg="White").place(x=60,y=350,width=200,height=200)
style = ttk.Style()
style.configure("Treeview", font=("Cordia New", 16))
lbf_Printer = LabelFrame(root, text='Edit data',font=("Cordia New", 16), bg='#e1f5fe', fg="#7b1fa2")
lbf_Printer.place(x=20, y=470, width=250, height=150)


def on_vertical_scroll(*args):
    tree.yview(*args)

def on_horizontal_scroll(*args):
    tree.xview(*args)

lbf_data = LabelFrame(root,  bg='#e1f5fe', fg="#7b1fa2")
lbf_data.place(x=300,y=30,width=750,height=700)
# lb1=Label(lbf_Printer,text='Code',font=("Cordia New", 18), bg='#e1f5fe', fg="#7b1fa2").place(x=20, y=0)

columns = (' ','Code', 'Part No', 'Part Name','Status')
tree = ttk.Treeview(lbf_data, columns=columns, show='headings')

# define headings
tree.heading(' ', text=' ')
tree.column(' ',width=10)
tree.heading('Code', text='Code')
tree.column('Code',width=50)
tree.heading('Part No', text='Part No')
tree.column('Part No',width=150)
tree.heading('Part Name', text='Part Name')
tree.column('Part Name',width=200)
tree.heading('Status', text='Status')
tree.column('Status',width=30)

# generate sample data
contacts = []
for n in range(1, 50):
    contacts.append((f' {n}',f'first {n}', f'last {n}', f'email{n}@example.com',f'Status {n}'))

# add data to the treeview
for contact in contacts:
    tree.insert('', tk.END, values=contact)


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))

# Create vertical scrollbar
vertical_scrollbar = ttk.Scrollbar(lbf_data, orient=tk.VERTICAL, command=tree.yview)
vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create horizontal scrollbar
horizontal_scrollbar = ttk.Scrollbar(lbf_data, orient=tk.HORIZONTAL, command=tree.xview)
horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
# Configure the Treeview to scroll with the scrollbars
tree.config(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)
# Configure the Canvas to scroll with the scrollbars
tree.bind('<<TreeviewSelect>>', item_selected)
tree.pack(fill=tk.BOTH, expand=True)
# tree.grid(row=0, column=0, sticky='nsew')

# add a scrollbar
# scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.place(x=900,y=30,width=10,height=400)
#.grid(row=0, column=1, sticky='ns')
# scrollbar = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=tree.xview)
# tree.configure(xscroll=scrollbar.set)
# scrollbar.place(x=300,y=450,width=300,height=10)
# run the app
root.mainloop()