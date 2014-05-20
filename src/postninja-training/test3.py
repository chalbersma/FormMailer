#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2011 halbersma <halbersma@HALBERSMA-VAIO>
#       

from Tkinter import *

root = Tk()

def callback(event):
	print "clicked at", event.x, event.y
	
frame = Frame(root, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
