# File: test6.py

def body(self, master):

    Label(master, text="First:").grid(row=0, sticky=W)
    Label(master, text="Second:").grid(row=1, sticky=W)

    self.e1 = Entry(master)
    self.e2 = Entry(master)

    self.e1.grid(row=0, column=1)
    self.e2.grid(row=1, column=1)

    self.cb = Checkbutton(master, text="Hardcopy")
    self.cb.grid(row=2, columnspan=2, sticky=W)

body();
