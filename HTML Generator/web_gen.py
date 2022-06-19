#
# Python:  3
#
# Author:  Wesley Morford
#
# Purpose: Create webpage using user input from web_gui.py window

import webbrowser
import os


# string to print in h1 tags
bannerStr = 'Stay tuned for our amazing summer sale!'

def PushWeb(bannerStr):
    # open/create html file and overwrite with new string
    with open('static_web.html', 'w') as f:
        f.write("<html><body><h1>{}</h1></body></html>".format(bannerStr))
        f.close()

def OpenWeb():
    # print contents to console
    f = open('static_web.html', 'r')
    webbrowser.open('file://' + os.path.realpath('static_web.html'))
    print(f.read())



if __name__ == "__main__":
    PushWeb()
    OpenWeb()
