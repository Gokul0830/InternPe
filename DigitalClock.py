from tkinter import *
from tkinter.ttk import *
from time import localtime, strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%I:%M:%S %p', localtime())  # Use '%I' for 12-hour format
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background='cyan', foreground="black")
label.pack(anchor='center')
time()

mainloop()
