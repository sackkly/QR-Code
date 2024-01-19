import tkinter as tk
from tkinterweb import WebView

def load_url():
    url = entry.get()
    webview.load_url(url)

# Create the main window
root = tk.Tk()
root.title("Tkinter Web Browser")

# Create an entry widget to input the URL
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a button to load the URL
load_button = tk.Button(root, text="Load URL", command=load_url)
load_button.pack(pady=10)

# Create a WebView widget
webview = WebView(root, width=800, height=600)
webview.pack(expand=True, fill="both")

# Run the Tkinter event loop
root.mainloop()