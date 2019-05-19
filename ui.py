import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title('Hackthon 2019')
root.geometry("500x600")

title_Q_1 = tk.Label(root, text="Γενικά", bg="red", fg="white")
title_Q_2 = Label(root, text="Something", bg="blue", fg="white")

c1 = Checkbutton(root, text="1. Πόσο ήταν συνολικά το traffic που δέχτηκε ο server;", command=lambda: onClick(1))
c2 = Checkbutton(root, text="2. Πόσα requests προκάλεσαν 5xx server error;", command=lambda: onClick(2))
c3 = Checkbutton(root, text="3. Πόσες είναι οι ξεχωριστές IP που επισκέφτηκαν τον server;", command=lambda: onClick(3))


def icon():
    print("ok")
    photo_pie = PhotoImage(file="Pie.png")
    label = Label(root, image=photo_pie)
    label.img=photo_pie
    label.pack()


button_pie = Button(root, text="Το σύνολο των server requests ανά χώρα", command=icon)


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


title_Q_1.pack(fill=tk.X)
c1.pack()
c2.pack()
c3.pack()
title_Q_2.pack(fill=tk.X)
button_pie.pack()


root.mainloop()