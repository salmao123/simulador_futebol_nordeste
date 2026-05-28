import random
import pandas as pd

class Mundo():

    def __init__(self):
        self.campeonatos = []
        self.times = []

    def adicionar_campeonato(self, campeonato):
        self.campeonatos.append(campeonato)

    def todos_times(self):
        for x in self.campeonatos:
            for y in x.times:
                self.times.append(y)

class Time():

    def __init__(self, nome, forca):
        self.nome = nome
        self.forca = forca
        self.jogos = 0
        self.pontos = 0

class Campeonato():

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.times = []

    def adicionar_time(self, time):
        self.times.append(time)

    def mostrar_tabela(self):
        tabela = pd.DataFrame({
            "Times": [t.nome for t in self.times],
            "Jogos": [t.jogos for t in self.times],
            "Pontos": [t.pontos for t in self.times]
        })

        print(tabela.sort_values(by="Pontos", ascending=False))

    def simular_temporada(self):
        rodadas = 0
        while rodadas < 10:
            print()
            print(f"--- Rodada {rodadas + 1} ---")
            print()
            times = self.times.copy()

            for j in range(3):
                casa = random.choice(times)
                times.remove(casa)
                fora = random.choice(times)
                times.remove(fora)
                
                partida = Partida(casa, fora)
                partida.jogar_tempo()
                partida.jogar_tempo()
                partida.placar()
                partida.resultado()
                print()

            rodadas += 1

        self.mostrar_tabela()

        print("Fim")


class Partida():

    def __init__(self, casa, fora):
        self.casa = casa
        self.fora = fora
        self.gols_casa = 0
        self.gols_fora = 0

    def mostrar(self):
        print(f"{self.casa.nome} VS {self.fora.nome}")

    def placar(self):
        print(f"{self.casa.nome} {self.gols_casa} X {self.gols_fora} {self.fora.nome}")

    def jogar_tempo(self):
        for c in range(5):
            dado = random.randint(1, 100)
            if dado >= 100 - self.casa.forca - 10:
                self.gols_casa += 1

        for f in range(5):
            dado = random.randint(1, 100)
            if dado >= 100 - self.fora.forca:
                self.gols_fora += 1

    def resultado(self):
        if self.gols_casa > self.gols_fora:
            self.casa.pontos += 3
        elif self.gols_fora > self.gols_casa:
            self.fora.pontos += 3
        else:
            self.casa.pontos += 1
            self.fora.pontos += 1

        self.casa.jogos += 1
        self.fora.jogos += 1


mundo = Mundo()

al1 = Time("CSA", 9)
al2 = Time("CRB", 10)
al3 = Time("ASA", 7)
al4 = Time("Murici", 5)
al5 = Time("Coruripe", 5)
al6 = Time("CSE", 4)

se1 = Time("Confiança", 10)
se2 = Time("Sergipe", 9)
se3 = Time("Itabaiana", 9)
se4 = Time("Lagarto", 7)
se5 = Time("Dorense", 4)
se6 = Time("América de Propriá", 3)

pe1 = Time("Sport", 12)
pe2 = Time("Náutico", 10)
pe3 = Time("Santa Cruz", 9)
pe4 = Time("Retrô", 9)
pe5 = Time("Salgueiro", 7)
pe6 = Time("Central", 5)

pb1 = Time("Botafogo-PB", 10)
pb2 = Time("Campinense", 9)
pb3 = Time("Treze", 9)
pb4 = Time("Sousa", 7)
pb5 = Time("Nacional de Patos", 5)
pb6 = Time("Auto Esporte", 4)

rn1 = Time("América-RN", 10)
rn2 = Time("ABC", 10)
rn3 = Time("Globo", 7)
rn4 = Time("Potiguar de Mossoró", 7)
rn5 = Time("Baraúnas", 5)
rn6 = Time("Santa Cruz-RN", 4)

ba1 = Time("Bahia", 12)
ba2 = Time("Vitória", 11)
ba3 = Time("Atlético de Alagoinhas", 7)
ba4 = Time("Jacuipense", 7)
ba5 = Time("Juazeirense", 7)
ba6 = Time("Fluminense de Feira", 5)

ce1 = Time("Fortaleza", 12)
ce2 = Time("Ceará", 12)
ce3 = Time("Ferroviário", 9)
ce4 = Time("Floresta", 7)
ce5 = Time("Icasa", 5)
ce6 = Time("Guarany de Sobral", 5)

ma1 = Time("Sampaio Correa", 10)
ma2 = Time("Moto Club", 9)
ma3 = Time("Maranhão", 9)
ma4 = Time("Imperatriz", 7)
ma5 = Time("Pinheiro", 5)
ma6 = Time("Cordino", 5)

pi1 = Time("Altos", 10)
pi2 = Time("River-PI", 9)
pi3 = Time("Fluminense-PI", 7)
pi4 = Time("Parnahyba", 7)
pi5 = Time("4 de Julho", 5)
pi6 = Time("Picos", 4)


alagoano = Campeonato("Alagoano", "Estadual")
sergipano = Campeonato("Sergipano", "Estadual")
pernanbucano = Campeonato("Pernanbucano", "Estadual")
paraibano = Campeonato("Paraibano", "Estadual")
potiguar = Campeonato("Potiguar", "Estadual")
bahiano = Campeonato("Bahiano", "Estadual")
cearense = Campeonato("Cearense", "Estadual")
maranhense = Campeonato("Maranhense", "Estadual")
piauiense = Campeonato("Piauiense", "Estadual")

alagoano.adicionar_time(al1)
alagoano.adicionar_time(al2)
alagoano.adicionar_time(al3)
alagoano.adicionar_time(al4)
alagoano.adicionar_time(al5)
alagoano.adicionar_time(al6)

sergipano.adicionar_time(se1)
sergipano.adicionar_time(se2)
sergipano.adicionar_time(se3)
sergipano.adicionar_time(se4)
sergipano.adicionar_time(se5)
sergipano.adicionar_time(se6)

pernanbucano.adicionar_time(pe1)
pernanbucano.adicionar_time(pe2)
pernanbucano.adicionar_time(pe3)
pernanbucano.adicionar_time(pe4)
pernanbucano.adicionar_time(pe5)
pernanbucano.adicionar_time(pe6)

paraibano.adicionar_time(pb1)
paraibano.adicionar_time(pb2)
paraibano.adicionar_time(pb3)
paraibano.adicionar_time(pb4)
paraibano.adicionar_time(pb5)
paraibano.adicionar_time(pb6)

potiguar.adicionar_time(rn1)
potiguar.adicionar_time(rn2)
potiguar.adicionar_time(rn3)
potiguar.adicionar_time(rn4)
potiguar.adicionar_time(rn5)
potiguar.adicionar_time(rn6)

bahiano.adicionar_time(ba1)
bahiano.adicionar_time(ba2)
bahiano.adicionar_time(ba3)
bahiano.adicionar_time(ba4)
bahiano.adicionar_time(ba5)
bahiano.adicionar_time(ba6)

cearense.adicionar_time(ce1)
cearense.adicionar_time(ce2)
cearense.adicionar_time(ce3)
cearense.adicionar_time(ce4)
cearense.adicionar_time(ce5)
cearense.adicionar_time(ce6)

maranhense.adicionar_time(ma1)
maranhense.adicionar_time(ma2)
maranhense.adicionar_time(ma3)
maranhense.adicionar_time(ma4)
maranhense.adicionar_time(ma5)
maranhense.adicionar_time(ma6)

piauiense.adicionar_time(pi1)
piauiense.adicionar_time(pi2)
piauiense.adicionar_time(pi3)
piauiense.adicionar_time(pi4)
piauiense.adicionar_time(pi5)
piauiense.adicionar_time(pi6)


mundo.adicionar_campeonato(alagoano)
mundo.adicionar_campeonato(sergipano)
mundo.adicionar_campeonato(pernanbucano)
mundo.adicionar_campeonato(paraibano)
mundo.adicionar_campeonato(potiguar)
mundo.adicionar_campeonato(bahiano)
mundo.adicionar_campeonato(cearense)
mundo.adicionar_campeonato(maranhense)
mundo.adicionar_campeonato(piauiense)


mundo.todos_times()


rodar = True

def menu(rodar):
    while rodar:
        print()
        print(f"1 - Jogo amistoso")
        print(f"2 - Campeonato")
        print(f"0 - Sair")
        resposta = input(": ")
        print()

        if resposta == "1":
            idx = 0
            for time in mundo.times:
                print(f"{idx} - {time.nome}")
                idx += 1

            print("Escolha os times")
            time1 = int(input(": "))
            time2 = int(input(": "))

            casa = mundo.times[time1]
            fora = mundo.times[time2]

            partida = Partida(casa, fora)
            partida.mostrar()
            input()
            partida.jogar_tempo()
            input("Fim do Primeiro tempo")
            partida.placar()
            input()
            partida.jogar_tempo()
            input("Fim de Jogo")
            partida.placar()
            partida.resultado()
            input()

        elif resposta == "2":
            idx = 0
            for campeonato in mundo.campeonatos:
                print(f"{idx} - {campeonato.nome}")
                idx += 1

            print("Escolha o campeonato")
            escolha = int(input(": "))

            camp = mundo.campeonatos[escolha]

            camp.simular_temporada()


menu(rodar)