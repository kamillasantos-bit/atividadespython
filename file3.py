#atividade_soma
soma = 0
num = int(input("Digite um número (0 para sair): "))
while num != 0:
    soma += num
    num = int(input("Digite um número (0 para sair): "))
print ("A soma dos números digitados é:", soma)

#atividade_senha
senha = ""
while senha != "python123":
    senha = input("Digite a senha:")
    print("Você acertou a senha!")