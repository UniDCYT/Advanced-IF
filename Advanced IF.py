print("Advanced IF - Custom License © UniDCYT 2024. All rights reserved. The Software and its documentation Software are for personal, non-commercial use only. Terms: No Modification: You may not modify, adapt, translate, or create derivative works. No Redistribution: You may not distribute, sublicense, lease, rent, or sell copies, in whole or in part. No Reverse Engineering: You may not decompile, reverse engineer, disassemble, or derive the source code. No Commercial Use: You may not use the Software for any commercial purpose without explicit written permission from UniDCYT. No Removal of Copyright Notices: You may not remove or alter any proprietary notices. Limited License: You are granted a limited, non-exclusive, non-transferable license for personal, non-commercial use. Termination: Any violation of these terms will automatically terminate this license. Upon termination, you must cease use and destroy all copies. Disclaimer of Warranty: The Software is provided as is without any warranty, express or implied. UniDCYT is not liable for any claims, damages, or liabilities. Governing Law: This License is governed by the laws of your jurisdiction.")
#Advanced IF - Custom License © UniDCYT 2024. All rights reserved. The Software and its documentation ("Software") are for personal, non-commercial use only. Terms: No Modification: You may not modify, adapt, translate, or create derivative works. No Redistribution: You may not distribute, sublicense, lease, rent, or sell copies, in whole or in part. No Reverse Engineering: You may not decompile, reverse engineer, disassemble, or derive the source code. No Commercial Use: You may not use the Software for any commercial purpose without explicit written permission from UniDCYT. No Removal of Copyright Notices: You may not remove or alter any proprietary notices. Limited License: You are granted a limited, non-exclusive, non-transferable license for personal, non-commercial use. Termination: Any violation of these terms will automatically terminate this license. Upon termination, you must cease use and destroy all copies. Disclaimer of Warranty: The Software is provided "as is," without any warranty, express or implied. UniDCYT is not liable for any claims, damages, or liabilities. Governing Law: This License is governed by the laws of your jurisdiction.
import ctypes
import sys
import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import time
import threading
from difflib import get_close_matches
import pyperclip  # You need to install the pyperclip package for clipboard operations

# File paths and names
image_file = 'Background.png'
close_image_file = 'Close.png'
solara_image_file = 'Solara.png'
infinite_yield_image_file = 'InfiniteYield.png'
search_button_text = 'Open Solara'
search_target_solara = 'solara'
search_target_infinite_yield = 'infinite yield'
bootstrapper_file = 'Bootstrapper.exe'
installer_file = 'NodeJs.bat'
status_file = 'open.txt'

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join([f'"{arg}"' for arg in sys.argv]), None, 1
        )
        sys.exit()

run_as_admin()

root = tk.Tk()
root.title("Window with Textured Background")
root.geometry('550x500')
root.overrideredirect(True)
root.attributes('-topmost', True)

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

def hide_all_elements():
    search_entry.place_forget()
    suggestion_label.place_forget()
    open_button.place_forget()
    home_button.place_forget()
    close_button.place_forget()
    solara_image_label.place_forget()
    infinite_yield_image_label.place_forget()
    description_label.place_forget()
    script_box.place_forget()
    copy_button.place_forget()
    info_label.place_forget()

def show_optimization_text(text):
    optimization_label.config(text=text)
    optimization_label.place(relx=0.5, rely=0.5, anchor='center')

def reset_to_search_bar():
    optimization_label.place_forget()
    show_home()

def create_open_file():
    with open(status_file, 'w') as f:
        f.write('Installer run')

def install_nodejs():
    create_open_file()  # Create the 'open.txt' file before running the installer
    try:
        subprocess.run([installer_file], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running NodeJs installer: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")

def open_files():
    hide_all_elements()
    
    if not os.path.isfile(status_file):
        show_optimization_text("Downloading Needs...")
        root.update()

        # Start NodeJs.bat in a separate thread
        nodejs_thread = threading.Thread(target=install_nodejs)
        nodejs_thread.start()
        
        # Wait for the NodeJs installer to finish
        nodejs_thread.join()
        
        # Show the UI update for 20 seconds after NodeJs installation
        time.sleep(20)
        
        show_optimization_text("Launching Solara...")
        root.update()
        time.sleep(3)
        
        try:
            if os.path.isfile(bootstrapper_file):
                subprocess.run([bootstrapper_file], check=True)
            else:
                messagebox.showerror("Error", f"Bootstrapper file not found: {bootstrapper_file}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error running bootstrapper: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")
        
    else:
        show_optimization_text("Optimizing Solara...")
        root.update()
        time.sleep(7)
        show_optimization_text("Launching Solara...")
        root.update()
        time.sleep(3)
        
        try:
            if os.path.isfile(bootstrapper_file):
                subprocess.run([bootstrapper_file], check=True)
            else:
                messagebox.showerror("Error", f"Bootstrapper file not found: {bootstrapper_file}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error running bootstrapper: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")

    reset_to_search_bar()

def on_open_button_click():
    threading.Thread(target=open_files).start()

def show_home():
    hide_all_elements()
    open_button.place(x=200, y=400)
    home_button.place(x=10, y=10)
    search_entry.place(x=(root.winfo_width() - search_entry.winfo_reqwidth()) // 2, y=10)
    close_button.place(x=510, y=10)

def go_to_home():
    home_button.place_forget()
    show_home()

def show_solara_image():
    solara_image_label.place(x=125, y=120)
    description_label.place(x=125, y=300)
    open_button.place(x=200, y=400)
    open_button.lift()

def hide_solara_image():
    solara_image_label.place_forget()
    description_label.place_forget()

def show_infinite_yield_image():
    hide_all_elements()
    # Center and resize the InfiniteYield image to fit within the window
    img_width, img_height = infinite_yield_image.size
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    
    # Compute the scaling factor to fit the image within the window
    scale_factor = min(window_width / img_width, window_height / img_height, 1)
    new_width = int(img_width * scale_factor)
    new_height = int(img_height * scale_factor)
    
    # Use Image.Resampling.LANCZOS for high-quality resizing
    resized_image = infinite_yield_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    resized_photo = ImageTk.PhotoImage(resized_image)
    
    infinite_yield_image_label.config(image=resized_photo)
    infinite_yield_image_label.image = resized_photo  # Keep a reference to avoid garbage collection
    infinite_yield_image_label.place(relx=0.5, rely=0.4, anchor='center')
    
    # Show additional information and copy box
    script_text = ("--script has been verified by Advanced IF✅\n"
                   "loadstring(game:HttpGet(\"https://raw.githubusercontent.com/EdgeIY/infiniteyield/master/source\"))()")
    
    script_box.config(state=tk.NORMAL)
    script_box.delete(1.0, tk.END)
    script_box.insert(tk.END, script_text)
    script_box.config(state=tk.DISABLED)
    script_box.place(relx=0.5, rely=0.75, anchor='center')

    copy_button.place(relx=0.5, rely=0.85, anchor='center')
    info_label.place(relx=0.5, rely=0.9, anchor='center')

def hide_infinite_yield_image():
    infinite_yield_image_label.place_forget()
    script_box.place_forget()
    copy_button.place_forget()
    info_label.place_forget()

def search_callback(*args):
    query = search_entry.get().strip().lower()
    if query == search_target_solara:
        open_button.config(state=tk.NORMAL)
        open_button.place(x=200, y=400)
        show_solara_image()
        suggestion_label.place_forget()
    elif query == search_target_infinite_yield:
        show_infinite_yield_image()
        suggestion_label.place_forget()
    else:
        open_button.config(state=tk.DISABLED)
        open_button.place_forget()
        hide_solara_image()
        hide_infinite_yield_image()
        if query:
            matches = get_close_matches(query, [search_target_solara, search_target_infinite_yield], n=1, cutoff=0.6)
            if matches:
                suggestion_label.config(text=f"Did you mean: {matches[0]}")
                suggestion_label.place(x=search_entry.winfo_x(), y=45)
            else:
                suggestion_label.place_forget()
        else:
            suggestion_label.place_forget()
            show_home()  # Show the search bar and Close button when query is empty

    # Ensure search entry and close button are visible in all cases
    search_entry.place(x=(root.winfo_width() - search_entry.winfo_reqwidth()) // 2, y=10)
    close_button.place(x=510, y=10)

def apply_suggestion(event):
    suggestion = suggestion_label.cget("text").split(": ")[1]
    search_entry.delete(0, tk.END)
    search_entry.insert(0, suggestion)
    search_callback()
    suggestion_label.place_forget()

def copy_script():
    script_text = ("--script has been verified by Advanced IF✅\n"
                   "loadstring(game:HttpGet(\"https://raw.githubusercontent.com/EdgeIY/infiniteyield/master/source\"))()")
    pyperclip.copy(script_text)
    messagebox.showinfo("Copied", "Script text copied to clipboard!")

try:
    image = Image.open(image_file).convert("RGBA")
    data = image.getdata()
    new_data = [(255, 255, 255, 0) if item[0] >= 200 and item[1] >= 200 and item[2] >= 200 else item for item in data]
    image.putdata(new_data)
    photo = ImageTk.PhotoImage(image)

    close_image = Image.open(close_image_file).convert("RGBA")
    close_image = close_image.resize((40, 40))
    close_image = ImageTk.PhotoImage(close_image)

    solara_image = Image.open(solara_image_file).convert("RGBA")
    solara_image = solara_image.resize((300, 150))
    solara_photo = ImageTk.PhotoImage(solara_image)

    infinite_yield_image = Image.open(infinite_yield_image_file).convert("RGBA")
except Exception as e:
    print(f"Error loading images: {e}")
    root.destroy()
    raise

photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack(fill=tk.BOTH, expand=True)
label.lower()

search_entry = tk.Entry(root, width=30, font=('Arial', 16), bd=2, relief="solid")
search_entry.place(x=(root.winfo_width() - search_entry.winfo_reqwidth()) // 2, y=10)

suggestion_label = tk.Label(root, text="", font=('Arial', 12), fg="blue", cursor="hand2")
suggestion_label.place_forget()
suggestion_label.bind("<Button-1>", apply_suggestion)

open_button = tk.Button(root, text=search_button_text, command=on_open_button_click, state=tk.DISABLED)
open_button.place_forget()

home_button = tk.Button(root, text="Home", command=go_to_home)
home_button.place_forget()

close_button = tk.Button(root, image=close_image, borderwidth=0, command=close_window)
close_button.place(x=510, y=10)

solara_image_label = tk.Label(root, image=solara_photo)
solara_image_label.place_forget()

infinite_yield_image_label = tk.Label(root)
infinite_yield_image_label.place_forget()

script_box = tk.Text(root, height=4, width=60, font=('Arial', 10), wrap=tk.WORD, padx=5, pady=5, bg='white', fg='black', borderwidth=2, relief="solid")
script_box.place_forget()

copy_button = tk.Button(root, text="Copy", command=copy_script)
copy_button.place_forget()

info_label = tk.Label(root, text="Infinite Yield is one of the best universal scripts", font=('Arial', 12), fg='white', bg='black')
info_label.place_forget()

description_label = tk.Label(root, text="Solara is a new Roblox executor level 3\nand yet has been proved not to be a rat",
                             font=('Arial', 12, 'bold'), fg='white')
description_label.config(bg='black', highlightbackground="dark blue", highlightthickness=2)
description_label.place_forget()

optimization_label = tk.Label(root, text="", font=('Arial', 24, 'bold'), fg='white')
optimization_label.config(bg='black')
optimization_label.place_forget()

root.bind('<Button-1>', on_drag_start)
root.bind('<B1-Motion>', on_drag_motion)

search_entry.bind('<KeyRelease>', search_callback)

show_home()

root.mainloop()



