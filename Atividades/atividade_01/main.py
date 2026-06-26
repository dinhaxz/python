while True:
    numero = int(input("Digite um número inteiro: "))

    # Laço que gera a tabuada de 1 até 10.
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    resposta = input("Deseja ver outra tabuada? (s/n): ").lower()

    if resposta != "s":
        print("Obrigado por usar o programa. Até a próxima!")
        break