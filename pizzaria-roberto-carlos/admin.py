import cliente
import estoque
import caixa

sinbolic_user = { 'admin' : '102030'}


def log_admin():
    while True:
        login = input("digite seu usuario").strip().lower()
        senha = input('digite sua senha').strip().lower()
        if senha not in sinbolic_user.values() or login not in sinbolic_user:
            print('login ou senha invalidos tente novamente')
        elif senha in sinbolic_user.values() and login in sinbolic_user:
            print('login realizado com suceso') 
            break


def interface_admin():
    while True:
        interface = input('Digite:\n\t(1)Para estoque\n\t(2)Para verificar pedidos\n\t(3)Para ver caixa\n\t (S)Para sair').lower().strip()
        if interface == '1' :
            estoque.estoque_control()
        elif interface == '2':
            cliente.pedidos()
        elif interface == '3':
            caixa.caixa_control()
        elif interface == 's':
            break