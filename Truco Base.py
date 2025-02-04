from time import sleep
from random import randint

team2 = team1 = 0  # times
total1 = total2 = 0  # valor carta atual
pdt1 = pdt2 = 0    # ponto dos turnos
pri=''             # fez a primeira

#------------------DEFS-------------------------------------------------------
def div(msg):                              #Definição de variavel para divisão
    print('='*30)#fodase
    print(msg)
    print('=' * 30)

#-----------------PROGRAMA PRINCIPAL------------------------------------------
div("O jogo começou")
while team1 < 12 and team2 < 12:           #Jogo em si
    pdt1 = pdt2 = 0
    print("Embaralhando as cartas")
    for c in range (1,4):                  #Para cada turno (fazer 3 vezes)

        div(f"TURNO {c}")

        #------------------------CARTAS---------------------------------------
        total1 = total2 = 0                  #valor carta atual

        total1 = randint(1,9)
        total2 = randint(1,9)

        div(f'O valor das cartas do time 1 é:[{total1}]\nO valor das cartas do time 2 é:[{total2}]')

        if total1>total2:                    #se o valor da carta atual do time 2 for maior do que o time1
            if c == 1:                     #se for o primeiro turno
                pri = "pri1"
            print(f"o Time 1  venceu o turno {c}")
            pdt1 +=1
            print(f"o Time 1 tem {pdt1} pontos de turno")
            if pdt1==2:                    #se o ponto de turno do time 1 for igual a 2
                print("A equipe 1 venceu a rodada")
                team1 += 1
                break
        if total2>total1:                    #se o valor da carta atual do time 2 for maior do que o time1
            if c == 1:                     #se for o primeiro turno
                pri = "pri2"
            print(f"o Time 2 venceu o turno {c}")
            pdt2 +=1
            print(f"o Time 2 tem {pdt2} pontos de turno")
            if pdt2==2:                    #se os pontos de turno do time 2 for igual a dois
                print("A equipe 2 venceu a rodada")
                team2 += 1
                break
        if total1==total2:                   #EMPATE
            print("Empate")
            if c==1:                       #se for o primeiro turno
                pdt1=pdt2=1
            elif c==2:                     #se for o segundo turno
                if pdt1>pdt2:              #se o time1 tiver mais pontos de turno
                    print('O time 1 ganhou a rodada por que fez a primeira')
                    team1 += 1
                    break
                elif pdt2>pdt1:            #se o time2 tiver mais pontos de turno
                    print('O time 2 ganhou a rodada por que fez a primeira')
                    team2 += 2
                    break
            elif c==3:                     #se for o turno 3
                print("Os times empataram o ultimo turno")
                if pdt1 == pdt2:
                    print("os times empataram 3  vezes")
                    break
                elif pri in 'pri1':        #se o time 1 ganhou a primeira
                    print("o time 1 ganhou a rodada pois fez a primeira")
                    pdt1 = pdt2 = 0
                    team1 = team1 + 1
                    break
                elif pri in 'pri2':        #se o time 2 ganhou a primeira
                    print("o time 2 ganhou a rodada pois fez a primeira")
                    pdt1 = pdt2 = 0
                    team2 = team2 + 1
                    break
                break
    div(f"o time 1 tem {team1} pontos\no time 2 tem {team2} pontos")
#-----------Finalização--------------------------------------------------------
if team1 >= 12:                            #se o time 1 tem 12 ou mais pontos
    div('o time 1 Ganhou!!!')
if team2 >= 12:                            #se o time 2 tem 12 ou mais pontos
    div('o time 2 Ganhou!!!')
