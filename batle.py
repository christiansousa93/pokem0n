

##  IMPORTAÇÕES  ##
import random

##  BATALHA  ##


def batalhaPokemon(pokemonDoJogador, pokemonInimigo, modo, jogador):

    # Checar vantagem
    def checarVantagens(vantagens, inimigo):
        vantagem = False
        if (inimigo.tipo in vantagens):
            vantagem = True
        return vantagem

    [hpPokemonJogador, hpPokemonInimigo] = [
        pokemonDoJogador.hp, pokemonInimigo.hp]
    # Acertos
    [acertosPokemonJogador, acertosPokemonInimigo] = [0, 0]
    contRound = 1

    vantagemPokemonJogador = checarVantagens(
        pokemonDoJogador.vantagens, pokemonInimigo)
    vantagemPokemonInimigo = checarVantagens(
        pokemonInimigo.vantagens, pokemonDoJogador)

    [modificadorVantagemPokemonJogador, modificadorVantagemPokemonInimigo] = [0, 0]

    if (vantagemPokemonJogador):
        modificadorVantagemPokemonJogador = 10
    if (vantagemPokemonInimigo):
        modificadorVantagemPokemonInimigo = 10

    # Loop de batalha
    while hpPokemonJogador > 0 and hpPokemonInimigo > 0:

        [tentativaPokemonJogador, tentativaPokemonInimigo] = [
            random.random() - 0.5, random.random() - 0.5]

        if (tentativaPokemonJogador > 0 and hpPokemonJogador > 0):
            hpPokemonInimigo -= (pokemonDoJogador.ataque - (
                pokemonInimigo.defesa * 0.65)) + modificadorVantagemPokemonJogador + (5 * jogador.experiencia)
            acertosPokemonJogador += 1

        if (tentativaPokemonInimigo > 0 and hpPokemonInimigo > 0):
            hpPokemonJogador -= (pokemonInimigo.ataque - (
                pokemonDoJogador.defesa * 0.65)) + modificadorVantagemPokemonInimigo
            acertosPokemonInimigo += 1

        print(f"""
              Round {contRound}
              {pokemonDoJogador.nome} got a total of {acertosPokemonJogador} attacks
              {pokemonInimigo.nome} got a total of {acertosPokemonInimigo} attacks
              Life of {pokemonDoJogador.nome} = {round(hpPokemonJogador, 2)}
              Life of {pokemonInimigo.nome} = {round(hpPokemonInimigo, 2)}""")

        contRound += 1

    # Pokemon inimigo ganhou?
    if (hpPokemonJogador <= 0 and hpPokemonInimigo > hpPokemonJogador):
        print(f"{pokemonInimigo.nome} won from {pokemonDoJogador.nome} and left {round(hpPokemonInimigo, 2)} health points")
    # Pokemon do jogador ganhou?
    elif (hpPokemonInimigo <= 0 and hpPokemonJogador > hpPokemonInimigo):
        print(f"{pokemonDoJogador.nome} won from {pokemonInimigo.nome} and left {round(hpPokemonJogador, 2)} health points")
        if (modo == "catch"):
            print(f"{pokemonInimigo.nome} catched")
            # Adiciona o pokemon capturado
            jogador.listaPokemons.append(pokemonInimigo)
        elif (modo == "duel"):
            jogador.experiencia += 1
    else:
        print("The Pokemons tied!")
