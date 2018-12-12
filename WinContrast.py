#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Basic user interface in tkinter.

Author: Daniel Dantas
Last edited: July 2018
"""

# python 3
import tkinter as tk

#python 2
#import Tkinter as tk

import my
import math as m
import os

from PIL import Image
from PIL import ImageTk

import ImgCanvas as ic

ROOT_TITLE = "Contrast"

class WinContrast(tk.Frame):

    def __init__(self, parent, canvas=None):

        self.frame = tk.Frame.__init__(self, parent)

        self.parent = parent

        self.canvas = canvas
        self.image = self.canvas.get_image()

        self.l1 = tk.Label(parent, text="Angular coefficient r", pady=20)
        self.l1.pack()

        self.s1 = tk.Scale(parent, from_=0, to=5, length=512, tickinterval=0.5, orient=tk.HORIZONTAL, command=self.cb_threshold, resolution=0.01)
        self.s1.set(1.0)
        self.s1.pack()

        self.l2 = tk.Label(parent, text="Linear coefficient m", pady=20)
        self.l2.pack()

        self.s2 = tk.Scale(parent, from_=0, to=255, length=512, tickinterval=16, orient=tk.HORIZONTAL, command=self.cb_threshold)
        self.s2.set(128)
        self.s2.pack()

        self.f1 = tk.Frame(parent)

        self.b1 = tk.Button(self.f1, text="Ok", command=self.cb_ok)
        self.b1.pack(side=tk.LEFT) 

        self.b2 = tk.Button(self.f1, text="Cancel", command=self.cb_cancel)
        self.b2.pack(side=tk.LEFT)

        self.f1.pack()

    def cb_threshold(self, event=None):
        print("%f, %d" % (self.s1.get(), self.s2.get()))
        r = self.s1.get()
        m = self.s2.get()
        result = my.contrast(self.image, r, m)
        self.canvas.set_preview(result)

    def cb_ok(self, event=None):
        self.canvas.ok_preview()
        self.parent.destroy()

    def cb_cancel(self, event=None):
        self.canvas.cancel_preview()
        self.parent.destroy()

        


############################################################
# Main function
############################################################

if __name__ == "__main__":

  root = tk.Tk()
  root.rowconfigure(0, weight=1)
  root.columnconfigure(0, weight=1)
  root.title(ROOT_TITLE)
  root.minsize(600, 270)
  
  win = tk.Toplevel(root)
  root.ic = ic.ImgCanvas(win)
  win.title = "ImgCanvas"
  img = my.imread("lena.tiff")
  root.ic.set_image(img)

  app = WinThresh(root, root.ic)
  app.mainloop()

