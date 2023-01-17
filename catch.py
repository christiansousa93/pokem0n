

##  IMPORTAÇÕES  ##
from batle import batalhaPokemon
from pokemon import listaPokemonsNivel1
from pokemon import listaPokemonsNivel2
from pokemon import listaPokemonsNivel3


##  CAPTURAR  ##
def capturar(jogador):
    print("Player's Pokemon List")
    jogador.mostrarPokemons()
    pokemonJogador = int(
        input("Choose your Pokemon: "))

    print("\n")

    print("List of available wild pokemons")
    if jogador.experiencia <= 5:
        for i in range(len(listaPokemonsNivel1)):
            print(
                f" {i} Name: {listaPokemonsNivel1[i].nome} | HP: {listaPokemonsNivel1[i].hp} | Attack: {listaPokemonsNivel1[i].ataque} | Defense: {listaPokemonsNivel1[i].defesa}")
    elif jogador.experiencia >= 6 and jogador.experiencia <= 10:
        for i in range(len(listaPokemonsNivel2)):
            print(
                f" {i} Name: {listaPokemonsNivel2[i].nome} | HP: {listaPokemonsNivel2[i].hp} | Attack: {listaPokemonsNivel2[i].ataque} | Defense: {listaPokemonsNivel2[i].defesa}")
    elif jogador.experiencia > 10:
        for i in range(len(listaPokemonsNivel3)):
            print(
                f" {i} Name: {listaPokemonsNivel3[i].nome} | HP: {listaPokemonsNivel3[i].hp} | Attack: {listaPokemonsNivel3[i].ataque} | Defense: {listaPokemonsNivel3[i].defesa}")
    pokemonSelvagem = int(
        input("Choose the pokemon you want to capture: "))


##  BATALHA  ##
    if jogador.experiencia <= 5:
        batalhaPokemon(jogador.listaPokemons[pokemonJogador],
                       listaPokemonsNivel1[pokemonSelvagem], "catch", jogador)
    elif jogador.experiencia >= 6 and jogador.experiencia <= 10:
        batalhaPokemon(jogador.listaPokemons[pokemonJogador],
                       listaPokemonsNivel2[pokemonSelvagem], "catch", jogador)
    elif jogador.experiencia > 10:
        batalhaPokemon(jogador.listaPokemons[pokemonJogador],
                       listaPokemonsNivel3[pokemonSelvagem], "catch", jogador)
