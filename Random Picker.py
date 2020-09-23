# Libraries

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import random
import os

# Initializing the window settings

title = "Game Picker"
sub = "Pick a list to find out the next game you'll play!"

root = tk.Tk()
root.title("Game Picker 1.0")

X = 800
Y = 300

main_screen = tk.Canvas(root, width = X, height = Y, relief = 'raised', bg = "black")
main_screen.pack()

# Initializing the file picker

ROM = ""
ROM_list = ""

# Functions
def getList(ready_list=None):
    global ROM
    global ROM_list
    try:
        if ready_list == None:
            ROM_list = filedialog.askopenfilename(filetypes=[("Lists", ".txt")])
            ROM = picker(ROM_list)
        else:
            ROM = picker(ready_list)
        
        cleaner = tk.Label(root, text="                                                                                             ", fg= "white", bg="black")
        cleaner.config(font=('helvetica', 30))
        main_screen.create_window(X//2, Y-120, window=cleaner)
        main_screen.create_window(X//2, Y-50, window=cleaner)
        
        ROM_status = tk.Label(root, text=ROM, fg= "white", bg="black")
        ROM_status.config(font=('helvetica', 18))
        main_screen.create_window(X//2, Y-50, window=ROM_status)
        if ROM != "":
            main_screen.create_window(X//3, Y-120, window=redoButton)
            main_screen.create_window(X//3*2, Y-120, window=okButton)
    except AttributeError:
        pass

def picker(list_file):
    try:
        with open(list_file) as f:
            return (random.choice(f.readlines()))
    except:
        pass

def reroll():
    global ROM_list
    getList(ROM_list)


# Initializing the labels

title_label = tk.Label(root, text=title, fg= "white", bg="black")
title_label.config(font=('helvetica', 30))

sub_label = tk.Label(root, text=sub, fg= "white", bg="black")
sub_label.config(font=('helvetica', 18))

browseButton = tk.Button(text="Import List", command=getList, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))

redoButton = tk.Button(text="Reroll!", command=reroll, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))

okButton = tk.Button(text="Ok!", command=exit, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))

# Drawing the window

main_screen.create_window(X//2, 50, window=title_label)
main_screen.create_window(X//2, 100, window=sub_label)
main_screen.create_window(X//2, Y-120, window=browseButton)

#print(random.choice(os.listdir()))

root.mainloop()
