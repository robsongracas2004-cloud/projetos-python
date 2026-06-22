# # n = int(input("Digite o numero: "))

# # if n % 2 == 0:
# #     print(f"Seu numero é par chefe")
# # else:
# #     print("Seu numero é impar")


# n = float(input("Digite o primeiro numero: "))
# n1 = float(input("Digite o segundo: "))

# if n == n1:
#     print(f"Os numeros {n} e {n1} são iguais")
# elif n >= n1:
#     print(f"O numero {n} é maior que {n1}. ")
# elif n1 >= n:
#     print(f"O numero {n1} é maior que {n}. ")
while True: 
    genero = (input("Digite seu genero "))

    if genero == "Masculino":
        peso_h = float(input("Digite seu peso: "))
        altura_h = float(input("Digite sua altura: "))
        peso_ideal = (peso_h * altura_h) - 58
        print(f"Seu peso ideal é: {peso_ideal}")
        break
    elif genero == "feminino":
        peso_f = float(input("Digite seu peso: "))
        altura_f = float(input("Digite sua altura"))
        peso_ideal = (peso_h * altura_h) -44.7
        print(f"Seu peso ideal é: {peso_ideal}")
        break
    else:
        print("Entrada invalida")
