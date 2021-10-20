
#dtype é o tipo de número passado na string: pode ser int ou float
def highAndLow(stringNumbers, dtype=int):
    #TRATATIVAS INICIAIS
    #Convertendo a string em uma lista onde cada posição é um único número
    #Por padrão, é convertido para inteiro
    numbers = [dtype(number) for number in stringNumbers.split(" ")]

    #INÍCIO DO ALGORITMO
    bigger = smaller = numbers[0]

    for number in numbers:
        if(number < smaller):
            smaller = number
        else:
            #Caso o número seja menor, não há porque verificar se ele é 
            #maior que o maior número já encontrado. Nunca seria verdade.
            #Isto aumenta levemente a eficiência do programa, principalmente
            #para entradas muito grandes
            if(number > bigger):
                bigger = number

    return "{} {}".format(bigger, smaller)