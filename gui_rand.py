""" Importing Tkinter """
import tkinter as tk
from tkinter import Button, Label
from wiki_app import *

# Main root window
root = tk.Tk()
root.title("Randow Wikipedia Article")

# Label 
button_label = Label(root, text="Press the button to generate a Wikipedia page")

# Button
gen_button = Button(root, text="Generate", command=gen_rand, bg="#F9E178")

# Grid
button_label.grid(row=0, column=0, padx=5, pady=5)
gen_button.grid(row=1, column=0, pady=5, padx=5)

if __name__ == '__main__':
    root.mainloop()
