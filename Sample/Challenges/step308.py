#
# Python: 3
#
# Author: Wesley Morford
#
#
#


import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        # window settings
        self.master = master
        self.master.geometry('{}x{}'.format(550, 190))
        self.master.title('Check files')

        self.varFile1 = StringVar()
        self.varFile1 = StringVar()

        # column 0 buttons

        self.btnBrowseTop = Button(self.master, text='Browse...', width=12, height=1)
        self.btnBrowseTop.grid(row=0, column=0,padx=(20,0), pady=(50,0), sticky=W)
        
        self.btnBrowseBot = Button(self.master, text='Browse...', width=12, height=1)
        self.btnBrowseBot.grid(row=1, column=0,padx=(20,0), pady=(10,0), sticky=W)

        self.btnCheck = Button(self.master, text='Check for files...', width=12, height=2)
        self.btnCheck.grid(row=2, column=0,padx=(20,0), pady=(10, 0), sticky=SW)

        # entry fields

        self.txtBrowseTop = Entry(self.master,text=self.varFile1, width=42, font=("Helvetica", 12), fg='black')
        self.txtBrowseTop.grid(row=0, column=1,padx=(30,0), pady=(50,0))

        self.txtBrowseBot = Entry(self.master,text=self.varFile1, width=42, font=("Helvetica", 12), fg='black')
        self.txtBrowseBot.grid(row=1, column=1,padx=(30,0), pady=(10,0))

        # close button

        self.btnClose = Button(self.master, text='Close Program', width=12, height=2, command = self.close)
        self.btnClose.grid(row=2, column=1,padx=(20,0), pady=(10, 0), sticky=SE)

    def close(self):
        self.master.destroy()



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
