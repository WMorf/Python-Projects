
import os


fPath = 'C:\\A\\'

def FindText():
    files = os.listdir(fPath)
    for i in files:
        file = i
        if file.endswith(".txt"):
            newpath = os.path.join(fPath, file)
            mod = os.path.getmtime(newpath)
            print(file)
            print(mod)
    






















if __name__ == "__main__":
    FindText()
