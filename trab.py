# CHAT COM BOT - ADQUIRIR INGRESSO

print(" Olá Player! Vou te conduzir para o melhor momento do ano: CLUB VORTEX!")
print("Por favor, informe o seu nome completo!")
nome = input("Informe seu nome completo:")

# dias disponiveis 

while True:
    print(f"Certo {nome}. Estaremos te esperando nos dias 17 e 18 de Maio!")

    print("Escolha os dias que deseja participar.")

    dia = input("Informe aqui: (EX: 17,18 OU 17 E 18)").strip()

    if dia == "17" or dia == "18":
        print(f"Será um prazer contar com sua presença no {dia} de Maio!")
        break # encerrar loop se for valido
    
    elif dia == "17 e 18":
        print(f"Será um prazer contar com sua presença nos {dia} de Maio!")

        break # encerrar loop se for valido

    else:
        print(" Não entendi. Por favor,digite novamente:")

# APURAÇÃO DE DADOS

print(f"{nome},irei precisar de alguns dados para finalizar seu cadastro.")

print(" Me informe seu CPF:")
cpf = input(":")

print("Me informe sua cidade:")
cidade = input("")

print("Informe seu Email:")
Email = input("")

while True:
    idade = input("Digite sua idade: ").strip()

    if idade.isdigit():
        idade = int(idade)
        print(f"Idade registrada: {idade} anos")
        break  # Encerra o loop se for válida
    else:
        print("Digite apenas números.")

#FIM DE CADASTRO

print(f"Certo {nome}. Obrigado por escolher o CLUB VORTEX. Vejo você em breve, em {dia} de Maio!")
