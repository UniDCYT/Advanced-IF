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

# Set the working directory to the directory where the script is located
os.chdir(os.path.dirname(sys.argv[0]))

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
    open_button.place_forget()  # Ensure the button is hidden by default
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
    messagebox.showinfo("Copied", "Script copied to clipboard!")

background_image = Image.open(image_file)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

home_button = tk.Button(root, text="Home", command=go_to_home)
close_button = tk.Button(root, image=ImageTk.PhotoImage(Image.open(close_image_file)), command=close_window)
close_button.place(x=510, y=10)

search_entry = tk.Entry(root, font=("Arial", 14), width=30)
search_entry.bind('<Return>', lambda event: search_callback())
search_entry.bind('<KeyRelease>', lambda event: search_callback())
search_entry.place(x=(root.winfo_width() - search_entry.winfo_reqwidth()) // 2, y=10)

suggestion_label = tk.Label(root, text="", font=("Arial", 10), fg="gray", cursor="hand2")
suggestion_label.bind("<Button-1>", apply_suggestion)

open_button = tk.Button(root, text=search_button_text, state=tk.DISABLED, command=on_open_button_click)

solara_image = Image.open(solara_image_file)
solara_photo = ImageTk.PhotoImage(solara_image)
solara_image_label = tk.Label(root, image=solara_photo)

infinite_yield_image = Image.open(infinite_yield_image_file)
infinite_yield_photo = ImageTk.PhotoImage(infinite_yield_image)
infinite_yield_image_label = tk.Label(root, image=infinite_yield_photo)

description_label = tk.Label(root, text="Solara: A Comprehensive Tool", font=("Arial", 14), wraplength=400)

script_box = tk.Text(root, font=("Arial", 10), height=6, width=50, wrap=tk.WORD, state=tk.DISABLED)
copy_button = tk.Button(root, text="Copy Script", command=copy_script)
info_label = tk.Label(root, text="This script has been verified by Advanced IF✅", font=("Arial", 10))

optimization_label = tk.Label(root, text="", font=("Arial", 20, "bold"))

# Start with the Home view
show_home()

root.mainloop()
      
