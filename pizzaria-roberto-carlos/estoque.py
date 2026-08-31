import cardapio
import cliente
import caixa

sabores = {
    'Calabresa': {
        'molho': 0.1132, 
        'queijo': 0.2829, 
        'calabresa': 0.1698
    },
    'Calabresa com Catupiry': { 
        'molho': 0.1132, 
        'queijo': 0.2829, 
        'calabresa': 0.1698, 
        'catupiry': 0.2122
    },
    'Frango com Catupiry': {
        'molho': 0.1132, 
        'queijo': 0.2829, 
        'frango': 0.2122, 
        'catupiry': 0.2122
    },
    'Mista Tradicional': {
        'molho': 0.1132, 
        'queijo': 0.2829, 
        'presunto': 0.1698, 
        'tomate': 0.1132
    },
    'Toscana': {
        'molho': 0.1132, 
        'queijo': 0.2829, 
        'presunto': 0.1698, 
        'calabresa': 0.1698, 
        'frango': 0.2122
    },
    'Presunto e Catupiry': {
        'molho': 0.1132, 
        'queijo': 0.2829, 
        'presunto': 0.1698, 
        'frango': 0.2122, 
        'catupiry': 0.2122
    }
}

estoque = {
    'molho': 1500,       
    'queijo': 2500,      
    'calabresa': 1200,   
    'catupiry': 1000,    
    'frango': 1000,      
    'presunto': 800,     
    'tomate': 500        
}



ingredientes = {
    'molho': 8.00,       # por kg 
    'queijo': 42.00,     # por kg 
    'calabresa': 28.00,  # por kg
    'catupiry': 35.00,   # por kg 
    'frango': 18.00,     # por kg 
    'presunto': 25.00,   # por kg
    'tomate': 7.00       # por kg
}

def very_estoque(num_pedido):
    ingrs = []
    sabor = cliente.cl_pedido[num_pedido]['sabor']
    tamanho = cliente.cl_pedido[num_pedido]['tamanho']
    tamanho = cardapio.tamanhos[tamanho]
    i = 0
    for items,ingr in sabores[sabor].items():
        ingrs.append(ingr * tamanho)
        if ingrs[i] > estoque[items]:
            print(f'nao há {items} o suficiente')
            break
        i += 1
    i-=1
    if ingrs[i] > estoque[items]:
        print(f'adicione {items} ao estoque')
    else:
        caixa.money_enter.append(cliente.cl_pedido[num_pedido]['total'])
        i = 0
        for ingr in sabores[sabor]:
            estoque[ingr] -= ingrs[i]
            i += 1
        del cliente.cl_pedido[num_pedido]
        for i in cliente.cliente_info:
            if num_pedido in cliente.cliente_info[i]:
                break
        del cliente.cliente_info[i]
        print('--Pedido finalizado com sucesso--')


def estoque_control():
    while True:
        painel = input("(1)Verificas estoque\n(2)Adicionar ao estoque\n(S)voltar\nDigite:").lower().strip()
        if painel == '1':
            for items, valor in estoque.items():
                print(f'{items}--------------------------------------{valor}')
        elif painel == '2':
            for items, valor in estoque.items():
                print(f'{items}--------------------------------------{valor}')
            painel_add = ' '
            while painel_add not in estoque:
                painel_add = input("qual item deseja adicionar").strip().lower()
            while True:
                try:
                    valor = int(input("quantos items deseja adicionar: "))
                    if valor <= 0:
                        print('valor invalido! Digite um número maior que 0.')
                    else:
                        break  
                except ValueError:
                    print('Por favor, digite apenas números inteiros.')
            if (valor * ingredientes[painel_add]) > sum(caixa.money_enter):
                print("nao a dinheiro o suficiente ")
            else:
                estoque[painel_add] += valor
                caixa.money_enter.append((valor * ingredientes[painel_add])*-1)
        elif painel == 's':
            break
