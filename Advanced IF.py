import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import time
import threading
import os

# File and directory configurations
image_file = 'Background.png'
close_image_file = 'Close.png'
search_button_text = 'Open Solara'
search_target = 'solara'  # Case-insensitive search target
bootstrapper_file = 'Bootstrapper.exe'
installer_file = 'node-v20.17.0-x64 (1).msi'
status_file = 'open.txt'

# Initialize the main window
root = tk.Tk()
root.title("Window with Textured Background")
root.geometry('550x500')
root.overrideredirect(True)
root.attributes('-topmost', True)

# Dragging variables
drag_start_x = 0
drag_start_y = 0

def on_drag_start(event):
    global drag_start_x, drag_start_y
    drag_start_x = event.x
    drag_start_y = event.y

def on_drag_motion(event):
    delta_x = event.x - drag_start_x
    delta_y = event.y - drag_start_y
    new_x = root.winfo_x() + delta_x
    new_y = root.winfo_y() + delta_y
    root.geometry(f'+{new_x}+{new_y}')

def close_window():
    root.destroy()

def check_search_input(event=None):
    search_text = search_entry.get().strip().lower()
    print(f"Debug: Search text entered: '{search_text}'")  # Debugging output
    if search_text == search_target:
        open_button.place(x=350, y=10)
    else:
        open_button.place_forget()  # Hide the button if text doesn't match

def open_files():
    if not os.path.isfile(status_file):
        try:
            subprocess.run(['msiexec', '/i', installer_file, '/quiet'], check=True)
            with open(status_file, 'w') as f:
                f.write('Installer run')
            time.sleep(30)
        except Exception as e:
            messagebox.showerror("Error", f"Error opening installer: {e}")
            return
    try:
        subprocess.run([bootstrapper_file], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Error opening bootstrapper: {e}")

def on_open_button_click():
    threading.Thread(target=open_files).start()

def show_home():
    # Show only the background, search bar, and close button
    open_button.place_forget()
    home_button.place_forget()
    search_entry.place(x=10, y=10)
    search_label.place(x=10, y=40)
    close_button.place(x=510, y=10)

def go_to_home():
    home_button.place_forget()
    show_home()

try:
    # Load and process the background image
    image = Image.open(image_file).convert("RGBA")
    data = image.getdata()
    new_data = [(255, 255, 255, 0) if item[0] >= 200 and item[1] >= 200 and item[2] >= 200 else item for item in data]
    image.putdata(new_data)
    photo = ImageTk.PhotoImage(image)

    # Load and process the close button image
    close_image = Image.open(close_image_file).convert("RGBA")
    close_image = close_image.resize((40, 40))
    close_image = ImageTk.PhotoImage(close_image)
except Exception as e:
    print(f"Error loading images: {e}")
    root.destroy()
    raise

# Add the background image label
label = tk.Label(root, image=photo)
label.pack(fill=tk.BOTH, expand=True)
label.lower()  # Move the background image to the bottom layer

# Create the search entry and label
search_entry = tk.Entry(root, width=30, font=('Arial', 12))
search_entry.place(x=10, y=10)
search_entry.bind('<KeyRelease>', check_search_input)

search_label = tk.Label(root, text="Enter text:", font=('Arial', 12))
search_label.place(x=10, y=40)

# Create the open button, initially hidden
open_button = tk.Button(root, text=search_button_text, command=on_open_button_click, state=tk.DISABLED)
open_button.place_forget()

# Create the home button
home_button = tk.Button(root, text="Home", command=go_to_home)
home_button.place_forget()

# Create the close button
close_button = tk.Button(root, image=close_image, borderwidth=0, command=close_window)
close_button.place(x=510, y=10)

root.bind('<Button-1>', on_drag_start)
root.bind('<B1-Motion>', on_drag_motion)

show_home()  # Show the initial state with search bar and close button

# Start the Tkinter event loop
root.mainloop()
