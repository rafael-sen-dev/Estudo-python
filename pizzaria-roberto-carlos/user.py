import cliente
import cardapio

def pedido():
    n_ped = len(cliente.cl_pedido) + 1
    for item, valor in cardapio.pizzas.items() :
        print(f" {item} + {valor['custo']}")
    pedid ='pp'
    while pedid not in cardapio.pizzas :
        pedid = input("Escolha o sabor")
    valor = 0.0
    for item, valor in cardapio.bordas.items():
       print (f'{item}{valor}')
    borda = 'oo'
    while borda not in cardapio.bordas:
        borda = input('Escolha uma borda')
    for item, valor in cardapio.refri.items():
        print(f'{item}{valor}')
    refri ='oo'
    while refri not in cardapio.refri:
        refri = input('Escolha o refrigerante')
    print(
        'Pequena : 25 cm x 25 cm = 625 cm²' 
        '\nMedia: 30 cm x 30 cm = 900 cm²' 
        '\nGrande: 35 cm x 35 cm = 1.225 cm²' 
        '\nFamilia: 40 cm x 40 cm = 1.600 cm²') 
    tamanho = ('kk')
    while tamanho not in cardapio.tamanhos:
        tamanho = input('escolha o tamanho da pizza').title().strip()
    obs = input('Alguma obicervação?')
    cliente.cl_pedido[n_ped] = {'sabor' : pedid,
                                'borda' : borda,
                                'refri' : refri,
                                'tamanho' : tamanho,
                                'observaçao' : obs}
    return n_ped




def log_user():
    nome = input("Digite seu nome completo")
    email = input("digite seu email")
    tel = input("digite seu numero de telefone")
    cliente.cliente_info[nome] = [email , tel,pedido()]
    cliente.nota_cl(nome)

