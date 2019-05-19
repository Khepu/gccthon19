import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title('Hackthon 2019')


c1 = Checkbutton(root, text="1. Πόσο ήταν συνολικά το traffic που δέχτηκε ο server;", command=lambda: onClick(1))
c2 = Checkbutton(root, text="2. Πόσα requests προκάλεσαν 5xx server error;", command=lambda: onClick(2))
c3 = Checkbutton(root, text="3. Πόσες είναι οι ξεχωριστές IP που επισκέφτηκαν τον server;", command=lambda: onClick(3))
c2.deselect()
c3.deselect()


def onClick(args):

    if args == 1:
        l2 = Label(text="").pack()
        l1 = Label(text="1. To συνολικό traffic είναι 68400 request").pack()
        l3 = Label(text="").pack()
    elif args == 2:
        l1 = Label(text="").pack()
        l2 = Label(text="2.	Προκληθήκαν 3826 server errors").pack()
        l3 = Label(text="").pack()
    elif args == 3:
        l1 = Label(text="").pack()
        l3 = Label(text="3.	Είναι 20 IP").pack()
        l2 = Label(text="").pack()


c1.pack()
c2.pack()
c3.pack()


root.mainloop()