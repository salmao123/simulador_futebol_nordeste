import random
import pandas as pd

class Mundo():

    def __init__(self):
        self.campeonatos = []

    def adicionar_campeonato(self, campeonato):
        self.campeonatos.append(campeonato)

    def todos_times(self):
        self.times = []
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
        qtd = 0
        for time in self.times:
            time.jogos = 0
            time.pontos = 0
            qtd += 1
        rodadas = 0
        while rodadas < int(qtd * 3):
            print()
            print(f"--- Rodada {rodadas + 1} ---")
            print()
            times = self.times.copy()

            for j in range(int(qtd / 2)):
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
        for c in range(4):
            dado = random.randint(1, 180)
            if dado >= 180 - self.casa.forca - 18:
                self.gols_casa += 1

        for f in range(4):
            dado = random.randint(1, 180)
            if dado >= 180 - self.fora.forca:
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

al1 = Time("CSA", 21)
al2 = Time("CRB", 22)
al3 = Time("ASA", 17)
al4 = Time("Murici", 14)
al5 = Time("Coruripe", 11)
al6 = Time("CSE", 13)
al7 = Time("Jacioba", 8)
al8 = Time("CEO", 6)

se1 = Time("Confiança", 20)
se2 = Time("Sergipe", 19)
se3 = Time("Itabaiana", 17)
se4 = Time("Lagarto", 15)
se5 = Time("Dorense", 10)
se6 = Time("Falcon", 13)
se7 = Time("América-SE", 8)
se8 = Time("Freipaulistano", 6)

pe1 = Time("Sport", 24)
pe2 = Time("Náutico", 20)
pe3 = Time("Santa Cruz", 21)
pe4 = Time("Retrô", 18)
pe5 = Time("Salgueiro", 15)
pe6 = Time("Central", 14)
pe7 = Time("Afogados", 12)
pe8 = Time("Petrolina", 9)

pb1 = Time("Botafogo-PB", 21)
pb2 = Time("Campinense", 19)
pb3 = Time("Treze", 20)
pb4 = Time("Sousa", 17)
pb5 = Time("Nacional-PB", 14)
pb6 = Time("Auto Esporte", 8)
pb7 = Time("CSP", 12)
pb8 = Time("Serrano-PB", 9)

rn1 = Time("América-RN", 20)
rn2 = Time("ABC", 21)
rn3 = Time("Globo", 14)
rn4 = Time("Potiguar", 15)
rn5 = Time("Alecrim", 11)
rn6 = Time("Santa Cruz-RN", 16)
rn7 = Time("Força e Luz", 8)
rn8 = Time("ASSU", 6)

ba1 = Time("Bahia", 24)
ba2 = Time("Vitória", 23)
ba3 = Time("Bahia de Feira", 17)
ba4 = Time("Jacuipense", 16)
ba5 = Time("Juazeirense", 18)
ba6 = Time("Itabuna", 13)
ba7 = Time("Doce Mel", 10)
ba8 = Time("Barcelona-BA", 8)

ce1 = Time("Fortaleza", 24)
ce2 = Time("Ceará", 23)
ce3 = Time("Ferroviário", 19)
ce4 = Time("Floresta", 16)
ce5 = Time("Iguatu", 14)
ce6 = Time("Guarani-J", 9)
ce7 = Time("Maracanã", 12)
ce8 = Time("Barbalha", 7)

ma1 = Time("Sampaio Correa", 21)
ma2 = Time("Moto Club", 19)
ma3 = Time("Maranhão", 18)
ma4 = Time("Imperatriz", 16)
ma5 = Time("Pinheiro", 14)
ma6 = Time("Cordino", 9)
ma7 = Time("IAPE", 12)
ma8 = Time("Tuntum", 7)

pi1 = Time("Altos", 20)
pi2 = Time("River-PI", 19)
pi3 = Time("Flamengo-PI", 17)
pi4 = Time("Parnahyba", 15)
pi5 = Time("4 de Julho", 13)
pi6 = Time("Picos", 11)
pi7 = Time("Oeirense", 9)
pi8 = Time("Corisabba", 7)


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
alagoano.adicionar_time(al7)
alagoano.adicionar_time(al8)

sergipano.adicionar_time(se1)
sergipano.adicionar_time(se2)
sergipano.adicionar_time(se3)
sergipano.adicionar_time(se4)
sergipano.adicionar_time(se5)
sergipano.adicionar_time(se6)
sergipano.adicionar_time(se7)
sergipano.adicionar_time(se8)

pernanbucano.adicionar_time(pe1)
pernanbucano.adicionar_time(pe2)
pernanbucano.adicionar_time(pe3)
pernanbucano.adicionar_time(pe4)
pernanbucano.adicionar_time(pe5)
pernanbucano.adicionar_time(pe6)
pernanbucano.adicionar_time(pe7)
pernanbucano.adicionar_time(pe8)

paraibano.adicionar_time(pb1)
paraibano.adicionar_time(pb2)
paraibano.adicionar_time(pb3)
paraibano.adicionar_time(pb4)
paraibano.adicionar_time(pb5)
paraibano.adicionar_time(pb6)
paraibano.adicionar_time(pb7)
paraibano.adicionar_time(pb8)

potiguar.adicionar_time(rn1)
potiguar.adicionar_time(rn2)
potiguar.adicionar_time(rn3)
potiguar.adicionar_time(rn4)
potiguar.adicionar_time(rn5)
potiguar.adicionar_time(rn6)
potiguar.adicionar_time(rn7)
potiguar.adicionar_time(rn8)

bahiano.adicionar_time(ba1)
bahiano.adicionar_time(ba2)
bahiano.adicionar_time(ba3)
bahiano.adicionar_time(ba4)
bahiano.adicionar_time(ba5)
bahiano.adicionar_time(ba6)
bahiano.adicionar_time(ba7)
bahiano.adicionar_time(ba8)

cearense.adicionar_time(ce1)
cearense.adicionar_time(ce2)
cearense.adicionar_time(ce3)
cearense.adicionar_time(ce4)
cearense.adicionar_time(ce5)
cearense.adicionar_time(ce6)
cearense.adicionar_time(ce7)
cearense.adicionar_time(ce8)

maranhense.adicionar_time(ma1)
maranhense.adicionar_time(ma2)
maranhense.adicionar_time(ma3)
maranhense.adicionar_time(ma4)
maranhense.adicionar_time(ma5)
maranhense.adicionar_time(ma6)
maranhense.adicionar_time(ma7)
maranhense.adicionar_time(ma8)

piauiense.adicionar_time(pi1)
piauiense.adicionar_time(pi2)
piauiense.adicionar_time(pi3)
piauiense.adicionar_time(pi4)
piauiense.adicionar_time(pi5)
piauiense.adicionar_time(pi6)
piauiense.adicionar_time(pi7)
piauiense.adicionar_time(pi8)


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
        print(f"3 - Campeonato Customizado")
        print(f"0 - Sair")
        resposta = input(": ")
        print()

        if resposta == "1":
            try:
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
                
            except:
                print("Resposta inválida")
                print("Tente digitar um número válido")

        elif resposta == "2":
            idx = 0
            for campeonato in mundo.campeonatos:
                print(f"{idx} - {campeonato.nome}")
                idx += 1

            print("Escolha o campeonato")
            escolha = int(input(": "))

            camp = mundo.campeonatos[escolha]

            camp.simular_temporada()

        elif resposta == "3":
            customizado = Campeonato("Meu Campeonato", "Customizado")
            try:
                quantidade = int(input("Quantidade de times: "))

                idx = 0
                for time in mundo.times:
                    print(f"{idx} - {time.nome}")
                    idx += 1

                print("Escolha os times")

                escolhidos = []

                for q in range(quantidade):
                    numero = int(input(": "))

                    if numero in escolhidos:
                        print("Time já escolhido")
                        continue

                    escolhidos.append(numero)

                    time_custom = mundo.times[numero]

                    customizado.adicionar_time(time_custom)

                customizado.simular_temporada()
                    

            except:
                print("Resposta inválida")
                print("Tente digitar um número válido")

        elif resposta == "0":
            rodar = False

        else:
            print("Resposta inválida")
            print("Tente digitar um número válido")


menu(rodar)

print("Programa finalizado")