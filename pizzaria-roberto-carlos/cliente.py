import estoque

cliente_info = {}
cl_pedido = { }

def nota_cl(nome):
    for item, valor in cliente_info.items():
            if nome == item:
                print(f'{item}\n{valor[0]}\n{valor[1]}\n{valor[2]}')
                num_pedido = valor[2]
                for num, pedido  in cl_pedido.items():
                    if num == num_pedido:
                        for ped, sab in pedido.items():
                             print(f'{ped} {sab}\n--Seu pedido foi confirmado aguarde-')

def pedidos():
    for item, valor in cliente_info.items():
        print("--------------------------------------------------------")
        print(f'{item}\n{valor[0]}\n{valor[1]}\n{valor[2]}')
        num_pedido = valor[2]
        for num, pedido  in cl_pedido.items():
            if num == num_pedido:
                for ped, sab in pedido.items():
                    print(f'{ped} {sab}')
                    print("--------------------------------------------------------")
    while True:
        painel = input('digite:\n\t(1)Para concluir pedido\n(S)para sair\nDigite:').strip().lower()
        if painel == '1':
            num_pedido == input("Digite o num do pedido par concluir").strip().lower()
            estoque.very_estoque(num_pedido)
        elif painel == 's':
            break

