
## BIBLIOTECA ##
import random
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from dados import *

## CORES ##
co0 = "#444466"  # Preta
co1 = "#feffff"  # Branca
co2 = "#6f9fbd"  # Azul
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#ef5350"  # Vermelha


def main():
    ## JANELA ##
    janela = Tk()
    janela.title('')
    janela.geometry('550x510')
    janela.configure(bg=co1)

    ttk.Separator(janela, orient=HORIZONTAL).grid(
        row=0, columnspan=1, ipadx=272)

    style = ttk.Style(janela)
    style.theme_use("clam")

    ## FRAME ##
    frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
    frame_pokemon.grid(row=1, column=0)

    def trocar_pokemon(i):
        global imagem_pokemon, pok_imagem

        # FUNDO DO FRAME
        frame_pokemon['bg'] = pokemon[i]['tipo'][3]

        # TIPO POKEMON
        pok_nome['text'] = i
        pok_nome['bg'] = pokemon[i]['tipo'][3]
        pok_tipo['text'] = pokemon[i]['tipo'][1]
        pok_tipo['bg'] = pokemon[i]['tipo'][3]
        pok_id['text'] = pokemon[i]['tipo'][0]
        pok_id['bg'] = pokemon[i]['tipo'][3]

        imagem_pokemon = pokemon[i]['tipo'][2]

        ## IMAGEM ##
        imagem_pokemon = Image.open(imagem_pokemon)
        imagem_pokemon = imagem_pokemon.resize((238, 238))
        imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

        pok_imagem = Label(frame_pokemon, image=imagem_pokemon,
                           relief='flat', bg=pokemon[i]['tipo'][3], fg=co1)
        pok_imagem.place(x=60, y=50)

        pok_tipo.lift()

        # STATUS
        pok_hp['text'] = pokemon[i]['status'][0]
        pok_ataque['text'] = pokemon[i]['status'][1]
        pok_defesa['text'] = pokemon[i]['status'][2]
        pok_velocidade['text'] = pokemon[i]['status'][3]
        pok_total['text'] = pokemon[i]['status'][4]

        # HABILIDADES
        pok_hb_1['text'] = pokemon[i]['skills'][0]
        pok_hb_2['text'] = pokemon[i]['skills'][1]

    ## NOME ##
    pok_nome = Label(frame_pokemon, text='', relief='flat',
                     anchor=CENTER, font=('Fixedsys 20'), fg=co1)
    pok_nome.place(x=12, y=15)

    ## CATEGORIA ##
    pok_tipo = Label(frame_pokemon, text='', relief='flat',
                     anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
    pok_tipo.place(x=12, y=50)

    ## ID ##
    pok_id = Label(frame_pokemon, text='', relief='flat',
                   anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
    pok_id.place(x=12, y=75)

    ## STATUS ##
    pok_status = Label(janela, text='Status', relief='flat',
                       anchor=CENTER, font=('Verdana 20 bold'), bg=co1, fg=co0)
    pok_status.place(x=15, y=310)

    pok_hp = Label(janela, text='HP: 320', relief='flat',
                   anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
    pok_hp.place(x=15, y=360)

    pok_ataque = Label(janela, text='Attack: 600', relief='flat',
                       anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
    pok_ataque.place(x=15, y=380)

    pok_defesa = Label(janela, text='Defense: 500', relief='flat',
                       anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
    pok_defesa.place(x=15, y=400)

    pok_velocidade = Label(janela, text='Velocity: 300', relief='flat',
                           anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
    pok_velocidade.place(x=15, y=420)

    pok_total = Label(janela, text='Total: 1.720', relief='flat',
                      anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
    pok_total.place(x=15, y=450)

    ## HABILIDADES ##
    pok_habilidades = Label(janela, text='', relief='flat',
                            anchor=CENTER, font=('Verdana 20 bold'), bg=co1, fg=co0)
    pok_habilidades.place(x=180, y=310)

    pok_hb_1 = Label(janela, text='', relief='flat',
                     anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
    pok_hb_1.place(x=195, y=360)

    pok_hb_2 = Label(janela, text='', relief='flat',
                     anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
    pok_hb_2.place(x=195, y=380)

    ## BOTÕES ##

    ## Botão 1 ##
    imagem_pokemon_1 = Image.open('images/head-pikachu.png')
    imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
    imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

    b_pok_1 = Button(janela, command=lambda: trocar_pokemon('Pikachu'), image=imagem_pokemon_1, text='Pikachu', width=150, relief='raised',
                     overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
    b_pok_1.place(x=375, y=2)

    ## Botão 2 ##
    imagem_pokemon_2 = Image.open('images/head-electrode.png')
    imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
    imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

    b_pok_2 = Button(janela, command=lambda: trocar_pokemon('Electrode'), image=imagem_pokemon_2, text='Electrode', width=150, relief='raised',
                     overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
    b_pok_2.place(x=375, y=48)

    ## Botão 3 ##
    imagem_pokemon_3 = Image.open('images/head-bulbasaur.png')
    imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
    imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

    b_pok_3 = Button(janela, command=lambda: trocar_pokemon('Bulbasaur'), image=imagem_pokemon_3, text='Bulbasaur', width=150, relief='raised',
                     overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
    b_pok_3.place(x=375, y=94)

    ## Botão 4 ##
    imagem_pokemon_4 = Image.open('images/head-bellsprout.png')
    imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
    imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

    b_pok_4 = Button(janela, command=lambda: trocar_pokemon('Bellsprout'), image=imagem_pokemon_4, text='Bellsprout', width=150, relief='raised',
                     overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
    b_pok_4.place(x=375, y=140)

    ## Botão 5 ##
    imagem_pokemon_5 = Image.open('images/head-squirtle.png')
    imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
    imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

    b_pok_5 = Button(janela, command=lambda: trocar_pokemon('Squirtle'), image=imagem_pokemon_5, text='Squirtle', width=150, relief='raised',
                     overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
    b_pok_5.place(x=375, y=186)

    ## Botão 6 ##
    imagem_pokemon_6 = Image.open('images/head-psyduck.png')
    imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
    imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

    b_pok_6 = Button(janela, command=lambda: trocar_pokemon('Psyduck'), image=imagem_pokemon_6, text='Psyduck', width=150, relief='raised',
                     overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
    b_pok_6.place(x=375, y=232)

    ## Botão 7 ##
    imagem_pokemon_7 = Image.open('images/head-charmander.png')
    imagem_pokemon_7 = imagem_pokemon_7.resize((40, 40))
    imagem_pokemon_7 = ImageTk.PhotoImage(imagem_pokemon_7)

    b_pok_7 = Button(janela, command=lambda: trocar_pokemon('Charmander'), image=imagem_pokemon_7, text='Charmander', width=150, relief='raised',
                     overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
    b_pok_7.place(x=375, y=278)

    ## Botão 8 ##
    imagem_pokemon_8 = Image.open('images/head-vulpix.png')
    imagem_pokemon_8 = imagem_pokemon_8.resize((40, 40))
    imagem_pokemon_8 = ImageTk.PhotoImage(imagem_pokemon_8)

    b_pok_8 = Button(janela, command=lambda: trocar_pokemon('Vulpix'), image=imagem_pokemon_8, text='Vulpix', width=150, relief='raised',
                     overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
    b_pok_8.place(x=375, y=324)

    Lista_pokemon = ['Pikachu', 'Electrode', 'Bulbasaur',
                     'Bellsprout', 'Squirtle', 'Psyduck', 'Charmander', 'Vulpix']

    ##  ESCOLHER POKEMON  ##
    pokemon_escolhido = random.sample(Lista_pokemon, 1)
    trocar_pokemon(pokemon_escolhido[0])

    janela.mainloop()


if __name__ == "__main__":
    main()
