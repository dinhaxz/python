lado1 = float(input("informe o valor do primeiro lado: "))
lado2 = float(input("informe o valor do segundo lado: "))
lado3 = float(input("informe o valor do terceiro lado: "))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    if lado1 == lado2 == lado3:
        tipo = "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
        

    print(f"É um triagulo e é do tipo {tipo}!")
else:
    print("Isso não é um triângulo válido\nseção encerrada..")
