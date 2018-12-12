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

class WinKernel(tk.Frame):

    def __init__(self, parent, canvas=None):

        self.frame = tk.Frame.__init__(self, parent)

        self.parent = parent

        self.canvas = canvas
        self.image = self.canvas.get_image()

        self.l1 = tk.Label(parent, text="a", padx=20)
        self.l1.pack(side=tk.LEFT)

        self.e1 = tk.Entry(parent)
        self.e1.pack(side=tk.LEFT)

        self.f1 = tk.Frame(parent)

        self.b1 = tk.Button(self.f1, text="Ok", command=self.cb_ok)
        self.b1.pack(side=tk.LEFT) 

        self.b2 = tk.Button(self.f1, text="Cancel", command=self.cb_cancel)
        self.b2.pack(side=tk.LEFT)

        self.f1.pack(side=tk.BOTTOM)

    def cb_resize(self, event=None):
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

  app = WinKernel(root, root.ic)
  app.mainloop()

