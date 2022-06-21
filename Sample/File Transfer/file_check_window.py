#
# Python: 3
#
# Author: Wesley Morford
#
#

import tkinter
from tkinter import *
from tkinter import filedialog as fd
import shutil
import time
import os


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        # window settings
        self.master = master
        self.master.geometry('{}x{}'.format(550, 200))
        self.master.title('Check files')


        # source and output loacation variables
        self.varFolderSrc = StringVar()
        self.varFolderOut = StringVar()


        def BrowseSrc():
            name = fd.askdirectory() 
            self.varFolderSrc.set(name +'/')
            print(name)

        def BrowseOut():
            name = fd.askdirectory() 
            self.varFolderOut.set(name +'/')
            print(name)

        def CheckFiles():
            source = self.varFolderSrc.get()
            destination = self.varFolderOut.get()
            files = os.listdir(source)
            
            for i in files:
                if i.endswith('.txt'):
                    # move the files represented by 'i' to their new destination if criteria met
                    name = i
                    mod = os.path.getmtime(source + i)
                    local_time = time.ctime(mod)
                    print(name + "- Last modification time:", local_time)
                    #print(name + str(mod))
                    #copare mod time to see if modded within 24 hrs
                    #shutil.move(source+i, destination)
                    # add files moved to listbox


        # column 0 buttons

        self.btnBrowseTop = Button(self.master, text='Source Folder', width=12, height=1, command = BrowseSrc)
        self.btnBrowseTop.grid(row=0, column=0,padx=(20,0), pady=(50,0), sticky=W)
            
        self.btnBrowseBot = Button(self.master, text='Output Folder', width=12, height=1, command = BrowseOut)
        self.btnBrowseBot.grid(row=1, column=0,padx=(20,0), pady=(10,0), sticky=W)

        self.btnCheck = Button(self.master, text='Check for files...', width=12, height=2, command = CheckFiles)
        self.btnCheck.grid(row=2, column=0,padx=(20,0), pady=(10, 0), sticky=SW)

        # entry fields

        self.txtBrowseTop = Entry(self.master,text=self.varFolderSrc, width=42, font=("Helvetica", 12), fg='black')
        self.txtBrowseTop.grid(row=0, column=1,padx=(30,0), pady=(50,0))

        self.txtBrowseBot = Entry(self.master,text=self.varFolderOut, width=42, font=("Helvetica", 12), fg='black')
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
