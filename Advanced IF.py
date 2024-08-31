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

# File and directory configurations
image_file = 'Background.png'
close_image_file = 'Close.png'
solara_image_file = 'Solara.png'  # Image file for Solara
search_button_text = 'Open Solara'
search_target = 'solara'  # Case-insensitive search target
bootstrapper_file = 'Bootstrapper.exe'
installer_file = 'node-v20.17.0-x64 (1).msi'
status_file = 'open.txt'

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Re-run the program with administrative privileges."""
    if not is_admin():
        # Re-run the script with admin rights
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join([f'"{arg}"' for arg in sys.argv]), None, 1
        )
        sys.exit()  # Exit the script to prevent further execution

# Call the function to check for admin rights
run_as_admin()

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

def hide_all_elements():
    """Hide all buttons, labels, and images, leaving only the background."""
    search_entry.place_forget()
    search_label.place_forget()
    open_button.place_forget()
    home_button.place_forget()
    close_button.place_forget()
    solara_image_label.place_forget()
    description_label.place_forget()

def show_optimization_text(text):
    """Show a large text message centered over the window."""
    optimization_label.config(text=text)
    optimization_label.place(relx=0.5, rely=0.5, anchor='center')

def reset_to_search_bar():
    """Reset the UI to show the search bar in the top middle and hide the optimization text."""
    optimization_label.place_forget()
    show_home()

def open_files():
    hide_all_elements()  # Hide all elements except the background

    # Show "Optimizing Solara..." text
    show_optimization_text("Optimizing Solara...")
    root.update()  # Update the display

    # Wait for 7 seconds
    time.sleep(7)

    # Change the text to "Launching Solara..."
    show_optimization_text("Launching Solara...")
    root.update()  # Update the display

    # Wait for another 3 seconds
    time.sleep(3)

    # Check if the installer has already been run by looking for the status file
    if not os.path.isfile(status_file):
        try:
            # Ensure the installer file exists before trying to execute it
            if os.path.isfile(installer_file):
                # Run the installer with elevated permissions
                subprocess.run(['msiexec', '/i', installer_file, '/quiet'], check=True)
                
                # Write to status file indicating the installer has been run
                with open(status_file, 'w') as f:
                    f.write('Installer run')
                
                # Allow time for installation to complete
                time.sleep(10)
            else:
                messagebox.showerror("Error", f"Installer file not found: {installer_file}")
                return
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error running installer: {e}")
            return
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")
            return
    
    # Attempt to open the bootstrapper file
    try:
        if os.path.isfile(bootstrapper_file):
            subprocess.run([bootstrapper_file], check=True)
        else:
            messagebox.showerror("Error", f"Bootstrapper file not found: {bootstrapper_file}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error running bootstrapper: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")
    
    # After 10 seconds, stop showing the "Launching Solara" message and show the search bar again
    reset_to_search_bar()

def on_open_button_click():
    threading.Thread(target=open_files).start()

def show_home():
    """Show only the background, search bar, and close button, with the search bar centered."""
    hide_solara_image()
    open_button.place_forget()
    home_button.place_forget()

    # Center the search bar
    root.update_idletasks()  # Ensure the window dimensions are fully processed
    search_x_position = (root.winfo_width() - search_entry.winfo_reqwidth()) // 2
    search_entry.place(x=search_x_position, y=10)
    
    search_label.place(x=search_x_position, y=40)
    close_button.place(x=510, y=10)

def go_to_home():
    home_button.place_forget()
    show_home()

def show_solara_image():
    """Display the Solara image and description."""
    solara_image_label.place(x=125, y=120)
    description_label.place(x=125, y=300)  # Center the description under the image
    open_button.place(x=200, y=400)  # Show the Open button below the description
    open_button.lift()  # Ensure the button is above the image

def hide_solara_image():
    """Hide the Solara image and description."""
    solara_image_label.place_forget()
    description_label.place_forget()

def search_callback(*args):
    """Callback for search entry text changes."""
    if search_entry.get().strip().lower() == search_target:
        open_button.config(state=tk.NORMAL)  # Enable the button
        show_solara_image()  # Show the Solara image and description
    else:
        open_button.config(state=tk.DISABLED)  # Disable the button
        hide_solara_image()  # Hide the Solara image and description

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

    # Load the Solara image
    solara_image = Image.open(solara_image_file).convert("RGBA")
    solara_image = solara_image.resize((300, 150))  # Resize if necessary
    solara_photo = ImageTk.PhotoImage(solara_image)
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
search_entry.place(x=10, y=10)  # Initial position
search_label = tk.Label(root, text="Enter text:", font=('Arial', 12))
search_label.place(x=10, y=40)

# Create the open button, initially hidden and disabled
open_button = tk.Button(root, text=search_button_text, command=on_open_button_click, state=tk.DISABLED)
open_button.place_forget()

# Create the home button
home_button = tk.Button(root, text="Home", command=go_to_home)
home_button.place_forget()

# Create the close button
close_button = tk.Button(root, image=close_image, borderwidth=0, command=close_window)
close_button.place(x=510, y=10)

# Solara image label (initially hidden)
solara_image_label = tk.Label(root, image=solara_photo)
solara_image_label.place_forget()

# Description label (initially hidden, with custom font and outline)
description_label = tk.Label(root, text="Solara is a new Roblox executor level 3\nand yet has been proved not to be a rat", 
                             font=('Arial', 12, 'bold'), fg='white')
description_label.config(bg='black', highlightbackground="dark blue", highlightthickness=2)
description_label.place_forget()

# Large label for optimization messages (initially hidden)
optimization_label = tk.Label(root, text="", font=('Arial', 24, 'bold'), fg='white')
optimization_label.config(bg='black')
optimization_label.place_forget()

root.bind('<Button-1>', on_drag_start)
root.bind('<B1-Motion>', on_drag_motion)

# Bind the search entry to a callback function for changes
search_entry.bind('<KeyRelease>', search_callback)

show_home()  # Show the initial state with search bar and close button

# Start the Tkinter event loop
root.mainloop()
