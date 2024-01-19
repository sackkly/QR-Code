import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Treeview Example")

# Define columns for the treeview
columns = ('Name', 'Age', 'City')

# Create the Treeview widget
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.place(x=250, y=100, width=500, height=300)

# Configure column headings
for col in columns:
    tree.heading(col, text=col)

# Add sample data to the treeview
data = [('John', 30, 'New York'),
        ('Alice', 25, 'Los Angeles'),
        ('Bob', 35, 'Chicago')]

for item in data:
    tree.insert('', 'end', values=item)

# Run the Tkinter event loop
root.mainloop()