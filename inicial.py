anoCerto = True
while (anoCerto == True):
    print("Digite o ano que nasceu: ")
    try: 
        ano = int(input())
        if (ano > 2024) or (ano < 1800):
            print("Ano inválido")
        else:
            idade = 2024 - ano
            print("Insira seu nome completo: ")
            nome = str(input())
            print(f"Obrigado {nome}, sua idade é: {idade}")
            anoCerto = False
    except ValueError:
        print("Ano inválido, por favor insira um número inteiro.")