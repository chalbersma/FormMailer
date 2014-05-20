
import Tkinter as tk
import time
 
def dt_ins():
    e.delete(0, tk.END)
    e.insert(0, time.asctime())
 
root = tk.Tk()
root.title("time test")
root.geometry('240x60+200+200')
e = tk.Entry(root)
b = tk.Button(root, text="Test!", command=dt_ins)
e.pack(fill= tk.BOTH, expand = tk.YES)
b.pack()
root.mainloop()
