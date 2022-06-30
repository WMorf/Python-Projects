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
from datetime import datetime
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
        self.varCount = StringVar()


        def BrowseSrc():
            name = fd.askdirectory() 
            self.varFolderSrc.set(name +'/')
            print(name +'/')

        def BrowseOut():
            name = fd.askdirectory() 
            self.varFolderOut.set(name +'/')
            print(name +'/')


        def CheckFiles():
            source = self.varFolderSrc.get()
            destination = self.varFolderOut.get()
            files = os.listdir(source)
            count = 0 # counts how many files were moved\
            self.varCount.set("")
            

            # move the files represented by 'i' to their new destination if criteria met
            for i in files:
                if i.endswith('.txt'):
                    name = i
                    mod = os.path.getmtime(source + i)
                    mod_time = time.ctime(mod)
                    # returns hours since last modification 
                    age = (round((time.time() - os.path.getmtime(source+i)) / 60)) / 60 

                    if age <= 24:
                        #copare mod time to see if modded within 24 hrs
                        shutil.move(source+i, destination)
                        print("{} was moved - {} hours old".format(name,age))
                        # add count of files moved to label
                        count += 1
                        
                    if count > 0:
                        countTxt = "{} files were moved".format(count)
                        print("{} files were moved".format(count))
                        self.varCount.set(countTxt)


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
        self.txtBrowseBot.grid(row=1, column=1, padx=(30,0), pady=(10,0))

        # close button

        self.btnClose = Button(self.master, text='Close Program', width=12, height=2, command = self.close)
        self.btnClose.grid(row=2, column=1,padx=(20,0), pady=(10, 0), sticky=SE)

        # label display count of files moved

        self.lblCount = Label(master, textvariable=self.varCount)
        self.lblCount.grid(row=3, column=1)

    def close(self):
        self.master.destroy()
            







if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
