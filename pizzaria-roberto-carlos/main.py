import admin
import user

while True:
    login = input("deseja fazer um pedido ou login \n Digite 'P'para pedido 'L' para login e 'S' para sair\n\tDigite:").lower().strip()
    if login == "p":
        user.log_user()
    elif login == "l":
        admin.log_admin()
        admin.interface_admin()
    elif login == 's':
        break