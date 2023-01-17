

##  BIBLIOTECAS  ##
import random
from batle import batalhaPokemon

##  DUELO  ##


def duelar(jogador, inimigo):
    listaPokemonsJogador = jogador.listaPokemons
    listaPokemonsInimigo = inimigo.listaPokemons

    print("Player's Pokemon List:")
    jogador.mostrarPokemons()
    pokemon1 = int(
        input("Choose your Pokemon: "))
    print("\n")

    print("Enemy Pokemon list:")
    inimigo.mostrarPokemons()
    pokemon2 = random.randint(0, 2)
    batalhaPokemon(listaPokemonsJogador[pokemon1],
                   listaPokemonsInimigo[pokemon2], "duel", jogador)
