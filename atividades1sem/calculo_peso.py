peso = (float(input("Digite seu peso: ")))

if peso <= 50:
    print(f"Seu peso é {peso}, você da categoria 'PALHA' ")
elif peso <= 59.99:
    print(f"Seu peso é {peso}, você da categoria 'Pluma' ")
elif peso <= 75.99:
    print(f"Seu peso é {peso}, você da categoria 'Leve' ")
elif peso <= 87.99:
    print(f"Seu peso é {peso}, você da categoria 'Pesado' ")
elif peso >= 88:
    print(f"Seu peso é {peso}, você da categoria 'Super pesado' ")
else:
    print("Entrada invalida")
