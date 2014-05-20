#test8
import Tkinter as tk
import datetime
 
def dt_ins():
    e.delete(0, tk.END)
    e.insert(0, str(datetime.datetime.now()))
 
root = tk.Tk()
root.title("Datetime Test")
root.geometry('240x60+200+200')
e = tk.Entry(root)
b = tk.Button(root, text="Test!", command=dt_ins)
e.pack()
b.pack()
root.mainloop()
