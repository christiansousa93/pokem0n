

##  IMPORTAÇÕES  ##
import json
import requests

listaPokemon = []

##  CLASSES  ##


class Pokemon:
    def __init__(self, pokemon):
        self.nome = pokemon["name"]
        self.tipo = pokemon["types"][0]["type"]["name"]
        self.habilidade = pokemon["abilities"][0]["ability"]["name"]
        self.hp = pokemon["stats"][0]["base_stat"]
        self.ataque = pokemon["stats"][1]["base_stat"]
        self.defesa = pokemon["stats"][2]["base_stat"]
        self.ataqueEspecial = pokemon["stats"][3]["base_stat"]
        self.defesaEspecial = pokemon["stats"][4]["base_stat"]
        self.velocidade = pokemon["stats"][5]["base_stat"]
        self.altura = pokemon["height"]
        self.peso = pokemon["weight"]

        self.listaVantagens = json.loads(requests.get(pokemon["types"][0]["type"]["url"]).content)[
            "damage_relations"]["double_damage_to"]
        self.vantagens = []
        for nome in self.listaVantagens:
            self.vantagens.append(nome["name"])

        self.listaDesvantagens = json.loads(requests.get(pokemon["types"][0]["type"]["url"]).content)[
            "damage_relations"]["double_damage_from"]
        self.desvantagens = []
        for nome in self.listaDesvantagens:
            self.desvantagens.append(nome["name"])


##  FUNÇÕES  ##


    def getPokemon(self):
        return f"""
    Name: {self.nome}
    HP: {self.hp}
    Class: {self.tipo}
    Skills: {self.habilidade}
    Attack: {self.ataque}
    Defense:{self.defesa}
    Special Atack: {self.ataqueEspecial}
    Special Defense: {self.defesaEspecial}
    Velocity: {self.velocidade}
    Height: {self.altura}
    Weight: {self.peso}
    Benefits: {self.nomesVantagens}
    Disadvantages: {self.nomesDesvantagens}"""

##  ATAQUE  ##
    def atacar(self):
        print(f"The {self.nome} attack with {self.habilidade}")


##  API  ##
resultados = json.loads(requests.get(
    "https://pokeapi.co/api/v2/pokemon?offset=0&limit=55").content)["results"]

for item in resultados:
    listaPokemon.append(Pokemon(json.loads(requests.get(item["url"]).content)))


##  POKEMONS  ##
listaPokemonsNivel1 = [listaPokemon[0], listaPokemon[3], listaPokemon[6], listaPokemon[9], listaPokemon[12], listaPokemon[15], listaPokemon[18], listaPokemon[20], listaPokemon[22], listaPokemon[24], listaPokemon[26],
                       listaPokemon[28], listaPokemon[31], listaPokemon[34], listaPokemon[36], listaPokemon[38], listaPokemon[40], listaPokemon[42], listaPokemon[45], listaPokemon[47], listaPokemon[49], listaPokemon[51], listaPokemon[53]]
listaPokemonsNivel2 = [listaPokemon[1], listaPokemon[4], listaPokemon[7], listaPokemon[10], listaPokemon[13], listaPokemon[16], listaPokemon[19], listaPokemon[21], listaPokemon[23], listaPokemon[25], listaPokemon[27],
                       listaPokemon[29], listaPokemon[32], listaPokemon[35], listaPokemon[37], listaPokemon[39], listaPokemon[41], listaPokemon[43], listaPokemon[46], listaPokemon[48], listaPokemon[50], listaPokemon[52], listaPokemon[54]]
listaPokemonsNivel3 = [listaPokemon[2], listaPokemon[5], listaPokemon[8], listaPokemon[11],
                       listaPokemon[14], listaPokemon[17], listaPokemon[30], listaPokemon[33], listaPokemon[44]]
