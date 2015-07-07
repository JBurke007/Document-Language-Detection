# from Tkinter import *
# 
# root = Tk()
# 
# root.title("Language Detection")
# root.geometry("400x400") 
# 
# app = Frame(root)
# app.grid()
# 
# label = Label(app, text = "This is a label")
# 
# label.grid()
# root.mainloop()


#!/usr/bin/env python
#-*- coding:utf-8-*-

from Tkinter import *
from tkMessageBox import *

MainWindow = Tk()
MainWindow.geometry("155x300+150+100")

def Button1Click():
    print "Hello Visual Python IDE... "

Button1 = Button(text = "Button Text", command = Button1Click)
Button1 .place(relx = 0.5, rely = 0.5, relheight = 0.20)

mainloop()