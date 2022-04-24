    ## tkinter builds widgets
from tkinter import *
from tkinter.ttk import *

# from time import strftime
from datetime import datetime

root = Tk()
root.title("Clock")

label = Label(root, font=("Times New Roman", 50), background="#000", foreground="magenta" )
label.pack(anchor='center')

def time():

    now = datetime.now() # current date and time

    # year = now.strftime("%Y")
    # month = now.strftime("%m")
    # day = now.strftime("%d")
    # time = now.strftime("%H:%M:%S")
    # date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    month = now.strftime('%m')
    print(month[1])

    string = now.strftime('%m %d %H:%M %p')
    label.config(text=string)
    # label.after(5000, time)

    print('%m')

time()

mainloop()