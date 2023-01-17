

## BIBLIOTECA ##
from tkinter import *
from tkinter import messagebox


def main():
    ## MENU ##
    root = Tk()
    root.geometry("1024x768")

    bg = PhotoImage(file="images/background_menu.png")
    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)

    frame1 = Frame(root)
    frame1 = Frame(root, bg='#05a5e1')
    frame1.pack(pady=200)

    credd = Button(frame1, text="Game developer by Christian Sousa, Curso de Desenvolvedor de Sistema, SENAC, Profº Tarik", relief='raised', overrelief=RIDGE,
                   compound=CENTER, anchor=NW, padx=5, font=('Rockwell 15'), bg='#ed5564')
    credd.pack(pady=5)

    frame1.mainloop()
