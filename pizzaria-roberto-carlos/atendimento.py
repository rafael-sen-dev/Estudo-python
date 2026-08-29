pizaria = "Roberto Carlos"

cardapio = {
            'Pizzeria Artesanal' : 35,
            "Pizza 1846" : 40 ,
            "Pizzaria Que Bella" : 45, 
            "Esfiharia Tio Pepi" : 40,
            "Pizzaria Italiana" : 60,
            }

all_pedidos = []

total_pp = []

name = input("Olá Digite o seu nome:").lower()
mais_pedido = "z"
print(f"Olá {name.title()} bem vindo a pizaria {pizaria}\n")

#aqui recebemos o pedido na variavel pedido e verificamos se esta no cardapio.

while mais_pedido != "n"
    mais_pedido = "z"
    print(f"O que deseja pedir hoje.\n {cardapio}")
    pedido = input().title().strip()

    #com o pedido sendo valido podemos pedir a quantidade e validala

    if pedido in cardapio:
        while True:
            try:
                quantidade = int(input("Digite a quantidade de itens: "))
                if quantidade <= 0:
                    print("Por favor, digite um número maior que zero.")
                elif quantidade > 0:
                    all_pedidos.append([pedido,quantidade])
                    break
            except ValueError:
                    print("Entrada inválida! Digite um número inteiro.")
        #verificaçao de continuaçao
        while mais_pedido not in ['y','n']:
            mais_pedido = input("deseja mais alguma coisa, se sim digite 'y' se nao digite 'n' "
            "\n--caso essa mansagen apareça novamente verifique a escrita--:").lower().strip()

    else:
        print(f"Desculpa nao temos {pedido} no nosso cardapio, tente novamente")

# processamento e exibiçao de subtotais

for pedid in all_pedidos:
    preco = cardapio[pedid[0]]
    pedid.append(preco * pedid[1])
    print (f"O valor de {pedid[1]} {pedid[0]} é de: $ {pedid[2]}Rs")
    total_pp.append(pedid[2])
total = sum(total_pp)

#validaççao de desconto de estudante

estudante = " "
while estudante not in ['sim','nao']:
    estudante = input("Tem direito a desconto de estudante? -Sim- ou -Nao:").lower().strip()
    if estudante == "sim":
        total = total * 0.9
    elif estudante != "nao":
        print("Digite 'sim' ou 'nao' sem acento.")

#recibo final organizado

for pedid in all_pedidos:
    print (f"{pedid[0]} x{pedid[1]}Un Vl-unit: {cardapio[pedid[0]]} total: $ {pedid[2]}Rs")
print (f"O falor total a ser pago e de $ {total}Rs")