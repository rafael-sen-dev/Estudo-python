cliente_info = {}
cl_pedido = { }

def nota_cl(nome):
    for item, valor in cliente_info.items():
            print(f'{item}\n{valor[0]}\n{valor[1]}\n{valor[2]}')
            num_pedido = valor[2]
            for num, pedido  in cl_pedido.items():
                if num == num_pedido:
                    for ped, sab in pedido.items():
                         print(ped,sab
                        '\n--Seu pedido foi confirmado aguarde')