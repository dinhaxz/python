# Solicita ao usuário a cor do semáforo.
# Digite a cor em letras minúsculas: verde, amarelo ou vermelho.
cor = input("Digite a cor do semáforo: ")

# Verifica a cor informada e exibe a ação correspondente.
if cor == "verde":
    print("Pode avançar com atenção.")
elif cor == "amarelo":
    print("Atenção! Prepare-se para parar.")
elif cor == "vermelho":
    print("Pare! Aguarde o sinal verde.")
else:
    # Caso a cor não seja uma das opções válidas.
    print("Cor inválida. Digite verde, amarelo ou vermelho.")