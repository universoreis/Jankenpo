import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

# cores/colors
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b" # background


# configurando a janela / set window
janela = Tk()
janela.title('Jankenpon')
janela.geometry('260x280')
janela.configure(bg=fundo)

# dividindo a janela / split window

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurando o frame cima / set up frame

app_1 = Label(frame_cima, text='Você / You', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=50, y=20)

app_ = Label(frame_cima, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=17)

app_2_pontos = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=170, y=20)
app_2 = Label(frame_cima, text='PC / CPU', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=150, y=70)
app_2_linha = Label(frame_cima, text='', height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

app_linha = Label(frame_cima, text='', width=255, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)

app_cpu = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
app_cpu.place(x=190, y=10)

global voce
global pc
global rounds
global points_you
global points_cpu

points_you = 0
points_cpu = 0
rounds = 5

# Função lógica do jogo / logic funcion of game

def jogar(i):
    global rounds
    global points_you
    global points_cpu

    if rounds > 0:
        print(rounds)
        opcoes = ['Pedra', 'Papel', 'Tesoura']
        cpu = random.choice(opcoes)
        you = i

        app_cpu['text'] = cpu
        app_cpu['fg'] = co1

    # caso for empate / draw game
        if you == 'Pedra' and cpu == 'Pedra':
            print('empate')
            app_linha['bg'] =co3
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
        elif you == 'Papel' and cpu == 'Papel':
            print('empate')
            app_linha['bg'] =co3
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
        elif you == 'Tesoura' and cpu == 'Tesoura':
            print('empate')
            app_linha['bg'] =co3
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0

    # você ganha / you win
        if you == 'Pedra' and cpu == 'Tesoura':
            print('Você Ganhou!')
            app_linha['bg'] =co0
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            points_you +=10
        elif you == 'Papel' and cpu == 'Pedra':
            print('Você Ganhou!')
            app_linha['bg'] =co0
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            points_you += 10
        elif you == 'Tesoura' and cpu == 'Papel':
            print('Você Ganhou!')
            app_linha['bg'] =co0
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            points_you += 10

    # voce perde / you lose
        if you == 'Tesoura' and cpu == 'Pedra':
            print('Você Perdeu!')
            app_linha['bg'] =co0
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co5
            points_cpu +=10
        elif you == 'Pedra' and cpu == 'Papel':
            print('Você Perdeu!')
            app_linha['bg'] =co0
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co5
            points_cpu += 10
        elif you == 'Papel' and cpu == 'Tesoura':
            print('Você Perdeu!')
            app_linha['bg'] =co0
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co5
            points_cpu += 10

    # Atualizando pontuação / update points
        app_1_pontos['text'] = points_you
        app_2_pontos['text'] = points_cpu

    # Atualizando numrero de chances / update rounds
        rounds -=1

    else:
        app_1_pontos['text'] = points_you
        app_2_pontos['text'] = points_cpu

    # chamando função terminar / call end funcion
        fim_do_jogo()

# Função iniciar o jogo / start game

def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()

# Configurando frame baixo / set down frame
    icon_1 = Image.open('images/pedra.png')
    icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo,command=lambda: jogar('Pedra'),width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15,y=60)

    icon_2 = Image.open('images/papel.png')
    icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo,command=lambda: jogar('Papel'),width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=95,y=60)

    icon_3 = Image.open('images/tesoura.png')
    icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo,command=lambda: jogar('Tesoura'),width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=170,y=60)

# Função terminar o jogo / end game
def fim_do_jogo():
    global rounds
    global points_you
    global points_cpu

    # reiniciando as variáveis para zero / restart variables to zero
    points_you = 0
    points_cpu = 0
    rounds = 5

    # Destruindo os botões de opção / delete option button
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    # Definindo o vencedor / set winner
    player_you = int(app_1_pontos['text'])
    player_cpu = int(app_2_pontos['text'])

    if player_you > player_cpu:
        app_winner = Label(frame_baixo, text='YOU WIN!', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co4)
        app_winner.place(x=5, y=60)
    elif player_you < player_cpu:
        app_winner = Label(frame_baixo, text='YOU LOSE!', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co5)
        app_winner.place(x=5, y=60)
    else:
        app_winner = Label(frame_baixo, text='DRAW GAME!', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
        app_winner.place(x=5, y=60)

    def jogar_denovo():
        app_1_pontos['text'] = '0'
        app_2_pontos['text'] = '0'
        app_winner.destroy()

        b_jogar_denovo.destroy()

        iniciar_jogo()

    b_jogar_denovo = Button(frame_baixo, command=jogar_denovo, width=10, text='PLAY', bg=fundo, fg=co0, font=('Ivy 10 italic'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_jogar_denovo.place(x=80, y=140)

b_jogar = Button(frame_baixo, command=iniciar_jogo, width=10, text='PLAY', bg=fundo, fg=co0, font=('Ivy 10 italic'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=80,y=140)

janela.mainloop()