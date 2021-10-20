import os

import desafio1
import desafio2
import desafio3

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

#SAUDAÇÕES
limparTela()
print("Olá, seja bem vindo!")
print("Todos os 3 desafios estão incluído neste programa.")
print("Você pode utilizá-los através dessa CLI ou importando cada um e experimentando por si mesmo cada módulo.")
print("1- Através desta interface de linha de comando.")
print("2- Através da importação manual de cada módulo. A documentação está aqui :)")
print("")
choice = int(input("Digite o número que represente a forma de utilização preferida por você para a avaliação dos desafio: "))


if(choice == 2):
    limparTela()
    print("Abaixo está a explicação para a utilização de cada uma das funções do desafio.")
    print("")


    print("desafio1.py")
    print("highAndLow(string, dtype=int))")
    print("    PARÂMETROS: ")
    print("    'string' é a string com todos os números separados por espaço.")
    print("    'type' é o tipo dos números contidos na string. Por padrão, assumi que os números são inteiros. Porém, se for desejado utilizar float basta trocar o valor do parâmetro.")
    print("RETORNO: ")
    print("    É retornada uma string com dois números separados por espaço. O primeiro número é o maior número de toda string passada no parâmetro e o segundo o menor.")
    print("-------------------------------------")
    print("")


    print("desafio2.py")
    print("binary2decimal(bitArray)")
    print("    PARÂMETROS: ")
    print("    'bitArray' é um array em que cada posição é um bit, com o bit mais significativo na primeira posição e o menos signficativo na última.")
    print("RETORNO: ")
    print("    O número do array em base 10.")
    print("-------------------------------------")
    print("")


    print("desafio3.py")
    print("countPeopleOnTheBus(arrayBalance)")
    print("    PARÂMETROS: ")
    print("    'arrayBalance' array de arrays com dois números, que representam a quantidade de pessoas que entraram no ônibus, na primeira posição do array, e a quantidade de pessoas que saíram, na segunda posição do array.")
    print("RETORNO: ")
    print("    Um inteiro que representa o número de pessoas dentro do ônibus ao fim de todas as paradas do ônibus")
    print("-------------------------------------")

    input("Pressione enter para sair...")
else:
    stop = False
    while (stop == False):
        limparTela()
        print("Por enquanto, temos estes desafios disponíveis ")

        print("1- desafio1.py")
        print("    Descobrir o maior e menor número dentro de uma string de vários números separados por espaço.")

        print("2- desafio2.py")
        print("    Converter um array que simboliza um número na base 2 para a base 10.")

        print("3- desafio3.py")
        print("    Calcular a quantidade de pessoas ao fim da linha do ônibus, dado o número de pessoas que saíram e entraram em cada parada.")

        print("0- SAIR")
        print("")

        choice = int(input("Digite qual desafio deseja executar: "))
        if(choice == 0):
            limparTela()
            break

        if(choice == 1):
            while(True):
                limparTela()
                stringDeNumeros = input("Digite a string, sem aspas, que contém os números inteiros separados por espaço: ")
                try:
                    print(desafio1.highAndLow(stringDeNumeros))

                    print("")
                    choice = int(input("Deseja voltar ao menu pricipal? 1 para sim, 0 para não: "))
                    if(choice==1):
                        break
                except:
                    print("Há algo errado com a entrada. Vamos tentar novamente :)")
                    input("Pressione enter para continuarmos...")
            pass

        if(choice == 2):
            while(True):
                limparTela()
                stringComArray = input("Digite a string, sem aspas, que representa o array com o número escrito na base 2: ")
                try:
                    print(desafio2.binary2decimal(eval(stringComArray, {})))
                    print("")
                    choice = int(input("Deseja voltar ao menu pricipal? 1 para sim, 0 para não: "))
                    if(choice==1):
                        break
                except:
                    print("Há algo errado com a entrada. Vamos tentar novamente :)")
                    input("Pressione enter para continuarmos...")
            pass

        if(choice == 3):
            while(True):
                limparTela()
                stringComArray = input("Digite a string, sem aspas, que representa o array com dois números em cada posição, onde o primeiro é a quantidade de pessoas que entraram no ônibus e o segundo número é a quantidade de pessoas que saíram do ônibus: ")
                try:
                    print(desafio3.countPeopleOnTheBus(eval(stringComArray, {})))
                    print("")
                    choice = int(input("Deseja voltar ao menu pricipal? 1 para sim, 0 para não: "))
                    if(choice==1):
                        break
                except:
                    print("Há algo errado com a entrada. Vamos tentar novamente :)")
                    input("Pressione enter para continuarmos...")
                
                
