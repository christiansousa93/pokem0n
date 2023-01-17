

##  IMPORTAÇÕES  ##

import os
import random

from duel import duelar
from catch import capturar
from pokemon import listaPokemonsNivel1
from trainer import Jogador, Inimigo, adicionarPokemon


##  CADASTROS  ##
# Cadastro jogador


def cadastrarJogador(lista, nome, nivel):
    global jogador
    listaPokemonsJogador = []
    pokemonsJogador = adicionarPokemon(listaPokemonsJogador, lista, nivel)
    jogador = Jogador(pokemonsJogador, nome, nivel)

# Cadastro adversário


def cadastrarInimigo():
    global inimigo
    listaPokemonsInimigo = []
    fim = 0
    if (jogador.experiencia < 10):
        fim = 23
    else:
        fim = 9

    pokemonsInimigo = adicionarPokemon(listaPokemonsInimigo, [random.randint(
        0, fim), random.randint(0, fim), random.randint(0, fim)], jogador.experiencia)

    inimigo = Inimigo(pokemonsInimigo, jogador.experiencia)


# COMEÇANDO O JOGO


print("Welcome!")

nomeJogador = input("Type your name: ")

print("Choose 3 pokemons!")

for i in range(len(listaPokemonsNivel1)):
    print(f"{i}: {listaPokemonsNivel1[i].nome}")


pokemonsEscolhidos = []
for i in range(3):
    opcao = int(input(f"What do you want to do now {i+1}º pokemon: "))
    pokemonsEscolhidos.append(opcao)

cadastrarJogador(pokemonsEscolhidos, nomeJogador, 1)
cadastrarInimigo()


escolhaMenu = ""
while (escolhaMenu != "0"):
    print("Menu")
    print(f"{nomeJogador}, what do you want to do now?")
    escolhaMenu = input(f"""
        1 - Catch Pokemon
        2 - Show Pokemons
        3 - Seek a battle
        4 - Show XP
        0 - Quit\n""")
    os.system("cls") or None

    if (escolhaMenu == "1"):
        capturar(jogador)
    elif (escolhaMenu == "2"):
        jogador.mostrarPokemons()
    elif (escolhaMenu == "3"):
        duelar(jogador, inimigo)
        cadastrarInimigo()
    elif (escolhaMenu == "4"):
        print(f"Your XP is: {jogador.experiencia}")
