import tkinter as tk
from tkinter import colorchooser

def choose_color():
    color_code = colorchooser.askcolor(title="Choose a color")
    if color_code:
        hex_color = color_code[1]
        rgb_color = color_code[0]

        color_label.config(text=f"HEX: {hex_color}\nRGB: {rgb_color}")
        color_box.config(bg=hex_color)

# Create the main window
window = tk.Tk()
window.title("Color Selector")
window.geometry("300x200")
window.resizable(False, False)

# Button to open the color chooser
choose_btn = tk.Button(window, text="Choose Color", command=choose_color, font=("Arial", 12))
choose_btn.pack(pady=20)

# Label to display color values
color_label = tk.Label(window, text="No color selected", font=("Arial", 10))
color_label.pack(pady=10)

# Frame to display the selected color visually
color_box = tk.Label(window, width=20, height=2, bg="white", relief="solid", bd=1)
color_box.pack(pady=5)

# Run the GUI
window.mainloop()
