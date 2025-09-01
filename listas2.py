#1
numeros = ["1", "2", "3", "4", "5"]
print(numeros)

#2
cores = ["azul", "verde", "vermelho", "amarelo"]
print("Segunda cor:", cores [1])
print("Ultima cor:", cores[-1])

#3
# Lista com três frutas
frutas = ["maçã", "banana", "laranja"]

# Substituindo a segunda fruta (índice 1) por "abacaxi"
frutas[1] = "abacaxi"

# Exibindo a lista atualizada
print(frutas)

#4
# Lista vazia para armazenar os números
numeros = []

# Loop para coletar 5 números do usuário
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Exibindo a lista completa
print("A lista completa de números é:", numeros)


#5
lista = [8, 3, 10, 1, 7]

lista.sort()

print(lista)

#6
lista = []
for i in range(5):

    n = int(input("Digite um número:"))
    lista.append(n)

soma = sum(lista)

print(lista)
print(soma)

#7

#8
letras = ["a", "b", "c", "d"]
quant = letras.count("a")
print(quant)

#9
numeros = ["1", "2", "3"]

numeros.remove("3")
print(numeros)

#10
N = int(input("insira um número inteiro "))
pares = []
for i in range (1, N+1):
    if i % 2==0:
     pares.append(i)
     print("Números pares de 1 até", N, ":", pares)


#11
dias = ("segunda", "terça", "quarta", "quinta", "sexta")

print("O terceiro dia da semana é:", dias[2])

#12
#dias da semana

dias_tupla = ('segunda', 'terça', 'quarta', 'quinta', 'sexta')
print(dias_tupla[2])

dias_tupla.append('domingo')

#13
# Lista com os dias da semana até sexta-feira
dias_lista = ["segunda", "terça", "quarta", "quinta", "sexta"]

dias_tupla = tuple(dias_lista)

print("Lista:", dias_lista)
print("Tupla:", dias_tupla)

#14
#3 Tupla com valores numéricos
t = (5, 10, 15, 20)

soma = sum(t)

print("Soma dos valores da tupla:", soma)