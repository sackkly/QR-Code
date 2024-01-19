import tkinter as tk
from tkinterweb import HtmlFrame

# Create the main window
root = tk.Tk()
root.title("Website Viewer")

# Create a WebView widget for displaying the website
webview = HtmlFrame(root, width=800, height=600)
webview.pack(expand=True, fill="both")

# Load a website (e.g., Google's homepage)
webview.load_url("https://www.google.com")

# Run the Tkinter event loop
root.mainloop()
