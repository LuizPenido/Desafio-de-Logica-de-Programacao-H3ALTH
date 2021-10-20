# Desafio de lógica de programação H3ALTH
 
## Execução
Seja bem vindo!
Para executar este programa é bem fácil e há duas maneiras:
- A primeira é executando o arquivo main.​py na pasta raiz deste projeto. Basta dar dois cliques nele (se tiver o python instalado em sua máquina, claro) 🙂
- A segunda maneira é navegando até a pasta raíz, pelo terminal, e digitando o seguinte código:
        
```
python main.​py
```


Tudo acontece dentro da interface de linha de comando. Inclusive, a documentação também está lá!

---
## Documentação

Caso queira a documentação sem precisar abrir o programa, aqui está uma forma bem rápida de utilizar cada uma das funções (não se esqueça de incluir o arquivo referente a cada desafio):


### **desafio1.​py**

    highAndLow(string, dtype=int))

**Parâmetros**: 
- **string**: é a string com todos os números separados por espaço.
- **dtype**: é o tipo dos números contidos na string. Por padrão, assumi que os números são inteiros. Porém, se for desejado utilizar float basta trocar o valor do parâmetro.

**Retorno**: string com dois números separados por espaço. O primeiro número é o maior número de toda string passada no parâmetro e o segundo, o menor.

---
### **desafio2.​py**

    binary2decimal(bitArray)
**Parâmetros**: 
- **bitArray**: é um array em que cada posição é um bit, com o bit mais significativo na primeira posição e o menos signficativo na última.

**Retorno**: inteiro que representa o número passado no array convertido para base 10.

---
### **desafio3.​py**

    countPeopleOnTheBus(arrayBalance)

**Parâmetros**:
- **arrayBalance**:  array de arrays com dois números,que representam a quantidade de pessoas que entraram no ônibus, na primeira posição do array,e a quantidade de pessoas que saíram, na segunda posição do array. 

    **Exemplo**: 
    [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]

**Retorno**: inteiro que representa o número de pessoas dentro do ônibus ao fim de todas as paradas do ônibus.