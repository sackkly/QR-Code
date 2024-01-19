import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext

def fetch_and_display_url():
    url = entry.get()
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.get_text()

        # Display the content in the scrolled text widget
        scrolled_text.delete(1.0, tk.END)  # Clear previous content
        scrolled_text.insert(tk.END, content)
    except requests.RequestException as e:
        scrolled_text.delete(1.0, tk.END)  # Clear previous content
        scrolled_text.insert(tk.END, f"Error fetching URL: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Web Content Fetcher")

# Create an entry widget to input the URL
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a button to fetch and display the URL content
fetch_button = tk.Button(root, text="Fetch URL", command=fetch_and_display_url)
fetch_button.pack(pady=10)

# Create a scrolled text widget to display the fetched content
scrolled_text = scrolledtext.ScrolledText(root, width=80, height=20)
scrolled_text.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
