# TKINTER Module is used for making buttons, windows, labels etc. It is a standard module for making GUI.
import tkinter as tk
# Time module provides time related functions.(strftime is used when you want to format time and date on your own.)
from time import strftime
# Now will make a root window with the help of TKINTER module. 
# This is the window where we display our things (in this case date and time).

# Now we'll set the title of the root.
root = tk.Tk()
root.title("DIGITAL CLOCK")   # setting title of the root.

# Now we will introduce function that will update date and time and display them in the label- 
# label - wo element jo text ya element ko display karta hai.
def time():
    string = strftime('%H:%M:%S:%p\n%D')   # %H , %M , %S , %p , %D are for hour, minutes, second, am/pm and date respectively.
    label.config(text = string)
    label.after(1000,time)

label = tk.Label(root, font=('Calibri', 50 , 'bold'), background='green', foreground='red')
label.pack(anchor='center')

time()

root.mainloop()



