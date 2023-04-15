import re

class Correo:
    def __init__(self):
        self.correo_correcto = str("luciacantos@gmail.com")

    def validar(self):
        while True:
            correo = input("Introduce tu correo electrónico: ")
            if re.search(".*@.*\..*", correo):
                if self.correo_correcto == correo:
                    print("Bienvenido")
                    break
                else:
                    print("Cuenta bloqueada a causa de un ataque")
                    break
            else:
                print("Por favor, introduzca un formato correcto (xxx@xx.x)")
                

