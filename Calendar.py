import tkinter as tk
from tkcalendar import DateEntry

def on_date_select():
    selected_date = cal.get_date()
    result_label.config(text=f"Selected Date: {selected_date}")

# Create the main window
root = tk.Tk()
root.title("Calendar Example")

# Create a DateEntry widget
cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
cal.pack(pady=10)

# Create a button to get the selected date
select_button = tk.Button(root, text="Select Date", command=on_date_select)
select_button.pack(pady=10)

# Label to display the selected date
result_label = tk.Label(root, text="Selected Date: ")
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()