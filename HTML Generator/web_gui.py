#
# Python:  3
#
# Author:  Wesley Morford
#
# Purpose: Take input from entry field and generate webpage using web_gen.py


import tkinter
from tkinter import *
import web_gen


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        # window settings
        self.master = master
        self.master.geometry('{}x{}'.format(500, 150))
        self.master.title('WebPage Generator')

        self.varBanner = StringVar()

        # get text from entry field and create WebPage using input text
        def GetBanner():
            name = self.txtBanner.get()
            web_gen.PushWeb(name)
            web_gen.OpenWeb()
            print(name)

        # column 0 button

        self.btnBanner = Button(self.master, text='Create Banner', width=12, height=1, command = GetBanner)
        self.btnBanner.grid(row=0, column=0,padx=(20,0), pady=(50,0), sticky=W)


        # entry field

        self.txtBanner = Entry(self.master, textvariable=self.varBanner, width=35, font=("Helvetica", 12), fg='black')
        self.txtBanner.grid(row=0, column=1,padx=(30,0), pady=(50,0))


        # close button

        self.btnClose = Button(self.master, text='Close Program', width=12, height=2, command = self.close)
        self.btnClose.grid(row=1, column=0,padx=(20,0), pady=(10, 0), sticky=SW)
        
    def close(self):
        self.master.destroy()


        
    


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
