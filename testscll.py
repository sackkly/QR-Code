import tkinter as tk
from tkinter import ttk

def on_vertical_scroll(*args):
    tree.yview(*args)

def on_horizontal_scroll(*args):
    tree.xview(*args)

# Create the main window
root = tk.Tk()
root.title("Treeview with Scrollbars Example")

# Create a Treeview widget with vertical and horizontal scrollbars
tree = ttk.Treeview(root, columns=('Column 1', 'Column 2', 'Column 3'), show='headings')

# Add sample data to the treeview
for i in range(1, 21):
    tree.insert('', 'end', values=(f'Item {i}', f'Description {i}', f'Value {i}'))

# Create vertical scrollbar
vertical_scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create horizontal scrollbar
horizontal_scrollbar = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=tree.xview)
horizontal_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Configure the Treeview to scroll with the scrollbars
tree.config(yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)

# Pack the Treeview widget
tree.pack(fill=tk.BOTH, expand=True)

# Run the Tkinter event loop
root.mainloop()
