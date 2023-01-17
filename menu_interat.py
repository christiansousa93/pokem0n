## BIBLIOTECA ##
from tkinter import *
from tkinter import messagebox
import tkinter as tk


import main
import pokedex
import credits


def Close():
    root.destroy()


def Botao1():
    main()
    return


def Botao2():
    return (pokedex)


def Botao3():
    print(credits)


## MENU ##
root = Tk()
root.geometry("1024x768")

bg = PhotoImage(file="images/background_menu.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)

frame1 = Frame(root)
frame1 = Frame(root, bg='#05a5e1')
frame1.pack(pady=200)


# Botões
button1 = Button(frame1, text="Battle Pokemon", relief='raised', overrelief=RIDGE,
                 compound=CENTER, anchor=NW, padx=5, font=('Rockwell 30'), bg='#ed5564', command=Botao1)
button1.pack(pady=5)


button2 = Button(frame1, text="Pokedex", relief='raised', overrelief=RIDGE,
                 compound=CENTER, anchor=NW, padx=5, font=('Rockwell 30'), bg='#ed5564', command=Botao2)
button2.pack(pady=5)


button3 = Button(frame1, text="Credits", relief='raised', overrelief=RIDGE,
                 compound=CENTER, anchor=NW, padx=5, font=('Rockwell 30'), bg='#ed5564', command=Botao3)
button3.pack(pady=5)


button4 = Button(frame1, text="Quit", relief='raised', overrelief=RIDGE,
                 compound=CENTER, anchor=NW, padx=5, font=('Rockwell 30'), bg='#ed5564', command=Close)
button4.pack(pady=5)


frame1.mainloop()
