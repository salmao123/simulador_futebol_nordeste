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

    def simular_tudo(self):
        input("--- Simular temporada ---")

        for camp in self.campeonatos:
            camp.simular_temporada()

        self.times.sort(key=lambda t: (t.pontos, t.gols, t.forca), reverse=True)
        print()
        print("Classificados:")

        for n in range(8):
            t = self.times[n]
            print(f"{t.nome} --- {t.gols} --- {t.pontos}")

        l1 = self.times[0]
        l2 = self.times[1]
        l3 = self.times[2]
        l4 = self.times[3]
        l5 = self.times[4]
        l6 = self.times[5]
        l7 = self.times[6]
        l8 = self.times[7]

        lampions = Mata_Mata(l1, l8, l3, l6, l2, l7, l4, l5)

        lampions.simular_mata_mata()


class Time():

    def __init__(self, nome, forca):
        self.nome = nome
        self.forca = forca
        self.jogos = 0
        self.pontos = 0
        self.gols = 0

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
            "Gols": [t.gols for t in self.times],
            "Pontos": [t.pontos for t in self.times]
        })

        print(tabela.sort_values(by="Pontos", ascending=False))

    def simular_temporada(self):
        print()
        input(f"Simular Campeonato {self.nome}")
        qtd = 0
        for time in self.times:
            time.jogos = 0
            time.pontos = 0
            time.gols = 0
            qtd += 1
        rodadas = 0
        while rodadas < int(qtd * 3):
            print()
            print(f"--- Rodada {rodadas + 1} ---")
            print()
            times = self.times.copy()

            # input("Simular rodada")

            for j in range(int(qtd / 2)):
                casa = random.choice(times)
                times.remove(casa)
                fora = random.choice(times)
                times.remove(fora)
                
                partida = Partida(casa, fora)
                partida.jogar_partida()
                partida.resultado()
                print()

            rodadas += 1

            self.mostrar_tabela()

        print("Fim")

class Mata_Mata():

    def __init__(self, chave_A1, chave_A2, chave_A3, chave_A4, chave_B1, chave_B2, chave_B3, chave_B4):
        self.chave_A1 = chave_A1
        self.chave_A2 = chave_A2
        self.chave_A3 = chave_A3
        self.chave_A4 = chave_A4
        self.chave_B1 = chave_B1
        self.chave_B2 = chave_B2
        self.chave_B3 = chave_B3
        self.chave_B4 = chave_B4

    def simular_mata_mata(self):
        print()
        input("Simular Campeonato Nordestino")

        print()
        print("--- Quartas ---")

        jogo1 = Partida(self.chave_A1, self.chave_A2)
        jogo1.mostrar()
        jogo1.jogar_partida_mata_mata()
        self.chave_C1 = jogo1.classificado

        jogo2 = Partida(self.chave_A3, self.chave_A4)
        jogo2.mostrar()
        jogo2.jogar_partida_mata_mata()
        self.chave_C2 = jogo2.classificado

        jogo3 = Partida(self.chave_B1, self.chave_B2)
        jogo3.mostrar()
        jogo3.jogar_partida_mata_mata()
        self.chave_D1 = jogo3.classificado

        jogo4 = Partida(self.chave_B3, self.chave_B4)
        jogo4.mostrar()
        jogo4.jogar_partida_mata_mata()
        self.chave_D2 = jogo4.classificado

        print()
        print("--- Semi ---")

        jogo5 = Partida(self.chave_C1, self.chave_C2)
        jogo5.mostrar()
        jogo5.jogar_partida_mata_mata()
        self.chave_E1 = jogo5.classificado

        jogo6 = Partida(self.chave_D1, self.chave_D2)
        jogo6.mostrar()
        jogo6.jogar_partida_mata_mata()
        self.chave_E2 = jogo6.classificado

        print()
        print("--- Final ---")

        jogo7 = Partida(self.chave_E1, self.chave_E2)
        jogo7.mostrar()
        jogo7.jogar_partida_mata_mata()
        self.campeao_lampions = jogo7.classificado

        print()
        print(f"{self.campeao_lampions.nome} campeão!!!")

class Agregado():

    def __init__(self, time_A, time_B):
        pass

class Partida():

    def __init__(self, casa, fora):
        self.casa = casa
        self.fora = fora
        self.gols_casa = 0
        self.gols_fora = 0
        self.gols_casa_penaltis = 0
        self.gols_fora_penaltis = 0

    def mostrar(self):
        print()
        print(f"{self.casa.nome} VS {self.fora.nome}")
        input()

    def placar(self):
        print(f"{self.casa.nome} {self.gols_casa} X {self.gols_fora} {self.fora.nome}")

    def placar_penaltis(self):
        print(f"{self.casa.nome} {self.gols_casa_penaltis} X {self.gols_fora_penaltis} {self.fora.nome}")

    def jogar_partida(self):

        for c in range(8):
            dado = random.randint(1, 180)
            if dado >= 180 - self.casa.forca - 18:
                self.gols_casa += 1

        for f in range(8):
            dado = random.randint(1, 180)
            if dado >= 180 - self.fora.forca:
                self.gols_fora += 1

        self.placar()

    def jogar_partida_mata_mata(self):
        for c in range(8):
            dado = random.randint(1, 180)
            if dado >= 180 - self.casa.forca - 18:
                self.gols_casa += 1

        for f in range(8):
            dado = random.randint(1, 180)
            if dado >= 180 - self.fora.forca:
                self.gols_fora += 1

        self.placar()

        if self.gols_casa == self.gols_fora:
            print("penaltis")
            restante = 5
            penaltis = True
            while penaltis:
                dado = random.randint(1, 100)
                if dado <= 75:
                    self.gols_casa_penaltis += 1
                
                dado = random.randint(1, 100)
                if dado <= 60:
                    self.gols_fora_penaltis += 1

                restante -= 1

                if restante < abs(self.gols_casa_penaltis - self.gols_fora_penaltis):
                    break

                if restante < 1:
                    restante += 1

            self.placar_penaltis()
            if self.gols_casa_penaltis > self.gols_fora_penaltis:
                self.classificado = self.casa
            else:
                self.classificado = self.fora

        else:
            if self.gols_casa > self.gols_fora:
                self.classificado = self.casa
            else:
                self.classificado = self.fora


    def resultado(self):
        if self.gols_casa > self.gols_fora:
            self.casa.pontos += 3
        elif self.gols_fora > self.gols_casa:
            self.fora.pontos += 3
        else:
            self.casa.pontos += 1
            self.fora.pontos += 1

        self.casa.gols += self.gols_casa
        self.fora.gols += self.gols_fora

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
        print(f"4 - Simular Tudo")
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
                partida.jogar_partida()
                partida.resultado()

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

        elif resposta == "4":
            mundo.simular_tudo()

        elif resposta == "0":
            rodar = False

        else:
            print("Resposta inválida")
            print("Tente digitar um número válido")


menu(rodar)

print("Programa finalizado")