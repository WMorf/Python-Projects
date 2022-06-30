#
# Python: 3
#
# Author: Wesley Morford
#
#


import tkinter
from tkinter import *
from tkinter import filedialog as fd 


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        # window settings
        self.master = master
        self.master.geometry('{}x{}'.format(500, 150))
        self.master.title('Check files')

        self.varFolder = StringVar()

        def Browse():
            name = fd.askdirectory() 
            self.varFolder.set(name)
            print(name)


        # column 0 buttons

        self.btnBrowseTop = Button(self.master, text='Browse...', width=12, height=1, command = Browse)
        self.btnBrowseTop.grid(row=0, column=0,padx=(20,0), pady=(50,0), sticky=W)


        # entry fields

        self.txtBrowseTop = Entry(self.master, textvariable=self.varFolder, width=35, font=("Helvetica", 12), fg='black')
        self.txtBrowseTop.grid(row=0, column=1,padx=(30,0), pady=(50,0))


        # close button

        self.btnClose = Button(self.master, text='Close Program', width=12, height=2, command = self.close)
        self.btnClose.grid(row=1, column=0,padx=(20,0), pady=(10, 0), sticky=SW)
        
    def close(self):
        self.master.destroy()



'''        
class fileModal():
    def __init__ (self, parent, pop):
        Frame.__init__ (self)

        self.pop = pop
        self.top = Toplevel(parent)
        self.popUp.title("Confirmation")
        self.popUp.geometry("300x150")
        self.popUp.config(bg="white")
'''

        
    


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
