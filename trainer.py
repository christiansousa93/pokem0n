

##  IMPORTAÇÕES  ##
from pokemon import listaPokemonsNivel1
from pokemon import listaPokemonsNivel2
from pokemon import listaPokemonsNivel3

##  TREINADOR  ##


class Treinador:
    def __init__(self, listaPokemons):
        self.listaPokemons = listaPokemons

    def mostrarPokemons(self):
        print("Your Pokemons: ")
        for i in range(len(self.listaPokemons)):
            print(
                f"Pokemon {i}: {self.listaPokemons[i].nome} | HP: {self.listaPokemons[i].hp} | Attack: {self.listaPokemons[i].ataque} | Defense: {self.listaPokemons[i].defesa}")


class Jogador(Treinador):
    def __init__(self, listaPokemons, nome, experiencia):
        super().__init__(listaPokemons)
        self.nome = nome
        self.experiencia = experiencia


class Inimigo(Treinador):
    def __init__(self, listaPokemons, nivel):
        super().__init__(listaPokemons)
        self.nivel = nivel


def adicionarPokemon(lista, pokemons, nivel):
    if nivel <= 5:
        for pokemon in pokemons:
            lista.append(listaPokemonsNivel1[pokemon])
    elif nivel >= 6 and nivel <= 10:
        for pokemon in pokemons:
            lista.append(listaPokemonsNivel2[pokemon])
    elif nivel > 10:
        for pokemon in pokemons:
            lista.append(listaPokemonsNivel3[pokemon])
    return lista
