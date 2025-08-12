# Bibliotecas: OS vou usar para conseguir limpar o terminal e não ficar muita coisa junta confundiondo o usuario; random vai ser usado para fazer a escolhar aleatoria do computador.
import random
import os

# Esse def é importante já que ele não vai deicar que muitas informações fiquem na telo confundindo o usuario e deixando a tela poluida.
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def dificuldade():
    print('\033[1;49;33m=-'*25 + '=\033[0m')
    print('Escolha a dificuldade:\n[1] Fácil (Números de 0 a 10, 5 tentativas)\n[2] Médio (Números de 0 a 50, 7 tentativas)\n[3] Difícil (Números de 0 a 100, 10 tentativas)')
    print('\033[1;49;33m=-'*25 + '=\033[0m')
 #Nesse while usei é um tipo de return que tenho que aprender a usar ja que facilita muito na leitura e agiliza o codigo.
    while True:
        try:
            escolha_nivel = int(input('Digite o número da dificuldade que deseja: '))
            if escolha_nivel == 1:
                limpar_tela()
                return 0, 10, 5
            elif escolha_nivel == 2:
                limpar_tela()
                return 0, 50, 7
            elif escolha_nivel == 3:
                limpar_tela()
                return 0, 100, 10
            else:
                print('Escolha apenas 1, 2 ou 3.')
        except  ValueError:
            print('\033[1;49;31mDigite apenas números.\033[0m')

def chute_usuario(minimo, maximo):
    while True:
        try:
            chute = int(input(f'Entre {minimo} e {maximo} qual número você escolhe?: '))
            if minimo <= chute <= maximo:
                return chute
            else:
                print(f'\033[1;49;31mO número escolhido deve estar entre {minimo} e {maximo}.\033[0m')
        except ValueError:
            print('\033[1;49;31mDigite apenas números validos.\033[0m') 

def jogador_adivinha():
    limpar_tela()
    minimo, maximo, limite =  dificuldade()
    numero_correto = random.randint(minimo, maximo)
    tentativas = 0
    correto = False

    print('Já pensei em um número. Consegue acertar qual é?')
    print('\033[1;49;33m=-'*25 + '=\033[0m')

    while tentativas < limite:
        chute = chute_usuario(minimo, maximo)
        tentativas += 1

        if chute < numero_correto:
            print(f'MEu número é MAIOR que {chute}.')
        elif chute > numero_correto:
            print(f'MEU número é MENOR que {chute}.')
        else:
            limpar_tela()
            print(f'\033[1;49;32mParabéns! Você acertou o número {numero_correto} em {tentativas} tentativas!\033[0m')
            correto = True
            break
    if not correto:
        print(f'\033[1;49;34mFim de jogo! O número era {numero_correto}.\033[0m')

def regras():
    print('Quando eu perguntar responda:')
    print('\033[1;49;33m=-'*25 + '=\033[0m')
    print("'=' se eu ACERTEI")
    print("'-' se o SEU núumero for MENOR que meu palpite")
    print("'+' se o SEU número for MAIOR que o palpite")
    print('\033[1;49;33m=-'*25 + '=\033[0m')

def maquina_adivinha():
    print('Pense em um número que vou tentar acertar.')
    minimo, maximo, limite = dificuldade()
    tentativas = 0
    acertou = False

    regras()

    while minimo <= maximo:
        palpite = (minimo + maximo) // 2
        tentativas += 1
        print(f'Meu palpite é: {palpite}')
        resposta = input("É esse o número? (+ / - / = / se precisar de ajuda digite: ? ): ")

        if resposta == '=':
            limpar_tela()
            print(f'\033[1;49;32mAcertei o número em {tentativas} tentativas!\033[0m')
            acertou = True
            break
        elif resposta == '+':
            minimo = palpite + 1
        elif resposta == '-': 
            maximo = palpite - 1
        elif resposta == '?':
            regras()
        else:
            print("\033[1;49;31mResponda apenas com '=', '+', '-' ou '?'\033[0m")
    if not acertou:
        print('\033[1;49;31mAlgo deu errado! Suas respostas não batem com as possibilidades possíveis.\033[0m')

# Parte "grafica".
def menu():
    primeira_vez = False
    while True:
        if primeira_vez == False:
            limpar_tela()
            print('Bem-Vindo ao Adivinhe o Número')
            primeira_vez = True
        print('Modos de jogo:')
        print('\033[1;49;33m=-'*15 + '=\033[0m')
        print('[1] Você adivinha o número')
        print('[2] Amáquina adivinha o número')
        print('[3] Sair')
        print('\033[1;49;33m=-'*15 + '=\033[0m')

        escolha = input('Digite 1, 2 ou 3: ').strip()
        limpar_tela()
        if escolha == '1': 
            jogador_adivinha()
        elif escolha == '2':
            maquina_adivinha()
        elif escolha == '3':
            certeza_saida = input('\033[1;49;35mTem certeza que deseja sair?\033[0m (s/n): ').strip().lower()
            if certeza_saida != 'n':
                print('Obrigado e até a próxima!')
                break
        else:
            print('\033[1;49;31mEscolha apenas 1, 2 ou 3.\033[0m')

if __name__ == "__main__":
    menu()
