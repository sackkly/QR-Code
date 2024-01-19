import tkinter as tk
from tkinterweb import WebView

def load_youtube_video():
    video_url = entry.get()
    html_code = f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allowfullscreen></iframe>'
    webview.set_html(html_code)

# Create the main window
root = tk.Tk()
root.title("YouTube Video Player")

# Create an entry widget to input the YouTube video URL
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a button to load the YouTube video
load_button = tk.Button(root, text="Load Video", command=load_youtube_video)
load_button.pack(pady=10)

# Create a WebView widget for displaying the YouTube video
webview = WebView(root, width=600, height=400)
webview.pack(expand=True, fill="both")

# Run the Tkinter event loop
root.mainloop()
