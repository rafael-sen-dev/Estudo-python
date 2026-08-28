pizaria = "Roberto Carlos"
cardapio = ["Pizzeria Artesanal","Pizza 1846","Pizzaria Que Bella","Esfiharia Tio Pepi","Pizzaria Italiana"]
valor = [35,40,45,40,60]
all_pedidos = []
all_quantidades = []
total_pp = []
name = input("Olá Digite o seu nome:").lower()
while True:
    print(f"Olá {name.title()} bem vindo a pizaria {pizaria}\n O que deseja pedir hoje.\n {cardapio}\n {valor}")
    pedido = input().title()
    if pedido in cardapio:
        while True:
            try:
                quantidade = int(input("Digite a quantidade de itens: "))
                if quantidade <= 0:
                    print("Por favor, digite um número maior que zero.")
                elif quantidade > 0:
                    all_pedidos.append(pedido)
                    all_quantidades.append(quantidade)
                    break
            except ValueError:
                    print("Entrada inválida! Digite um número inteiro.")
        while True:
            mais_pedido = input("deseja mais alguma coisa, se sim digite 'y' se nao digite 'n':")
            if mais_pedido.strip().lower() == "n":
                very = 0
                break
            elif mais_pedido.lower().strip() == "y":
                very = 1
                break
            else:
                print("digite 'y' ou 'n'.")
        if very == 0:
            break
    else:
        print(f"Desculpa nao temos {pedido} no nosso cardapio, tente novamente")
i = 0
for ped in all_pedidos:
    numero_p = cardapio.index(all_pedidos[i])
    total_pp.append(valor[numero_p] * all_quantidades[i])
    print (f"O valor de {all_quantidades[i]} {all_pedidos[i]} é de: $ {total_pp[i]}Rs")
    i += 1
total = sum(total_pp)
while True:
    estudante = input("Tem direito  desconto por estudante? -Sim- ou -Nao:")
    if estudante.lower().strip() == "sim":
        total = total * 0.9
        break
    elif estudante.lower().strip() == "nao":
        break
    else:
        print("Digite 'sim' ou 'nao' sem acento.")
print (f"O falor total a ser pago e de $ {total}Rs")