# Python Ver:   3.10.4
#
# Author:       Wesley Morford
#
# Purpose:      Phonebook Demo, demonstrating OOP, Tkinter GUI module,    
#               using Tkinter Parent and Child relationships
#
# Tested OS:    Code written and tested to work with Windows 10


from tkinter import messagebox
from tkinter import *
import tkinter as tk



# import other phonebook modules
import student_gui
import student_func

# Frame is the Tkinter frame class our class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # master frame config
        self.master = master
        self.master.minsize(500,300) #(ht,wh)
        self.master.maxsize(500,300)
        # center window centers app on user's screen
        student_func.center_window(self,500,300)
        self.master.title("Student Tracker")
        self.master.configure(bg="#F0F0F0")
        # built in catch if users clicks corner 'x' on window
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_func.ask_quit(self))
        # arg = self.master

        # load in the gui widgets from seperate module
        student_gui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
