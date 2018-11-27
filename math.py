print("Digita um número ae meu consagrado")
x = int(input("Número 1 é esse: "))
y = int(input("Número 2 é esse: "))
print("Prontinho, agora escolhe o que tu quer fazer com eles")
print("1 - Somar")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
escolha = int(input("Seu comando: "))
while(escolha > 0):
    if (escolha == 1):
        print("A soma dá", x+y, "meu amiguinho")
        escolha = 0
    elif (escolha == 2):
        print("A subtração dá", x-y, "meu amiguinho")
        escolha = 0
    elif(escolha == 3):
        print("A multiplicação dá", x*y, "meu amiguinho")
        escolha = 0
    elif(escolha == 4):
        print("A divisão dá", x/y, "meu amiguinho")
        escolha = 0
    else:
        print("opora tu digitou o número errado")
        break
else:
    print("Valeu por usar meu script para suas fórmulas matemágicas kek flw flw")
