# TAKE Screenshot using python

import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()

canvas1 = tk.Canvas(root,width=200,height = 200)
canvas1.pack()

def takeScreenshot():
    mySS = pyautogui.screenshot()
    save_path = asksaveasfilename()
    mySS.save(save_path+"_ss.png")

myButton = tk.Button(text="Take SS",command=takeScreenshot,font=10)
canvas1.create_window(100,100,window=myButton)

root.mainloop()

