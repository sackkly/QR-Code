import tkinter as tk
from tkhtmlview import HTMLLabel

def load_url():
    url = entry.get()
    html_label.set_html(f'<a href="{url}">{url}</a>')

# Create the main window
root = tk.Tk()
root.title("Tkinter Web Browser")

# Create an entry widget to input the URL
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a button to load the URL
load_button = tk.Button(root, text="Load URL", command=load_url)
load_button.pack(pady=10)

# Create an HTMLLabel widget for displaying the web browser content
html_label = HTMLLabel(root, html='', width=800, height=600)
html_label.pack(expand=True, fill="both")

# Run the Tkinter event loop
root.mainloop()