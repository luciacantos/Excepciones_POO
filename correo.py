import re

class Correo:
    def __init__(self):
        self.correo_correcto = str("luciacantos@gmail.com")

    def validar(self):
        while True:
            correo = input("Introduce tu correo electrónico: ")
            if re.search(".*@.*\..*", correo): # método para comprobar que los caracteres sean correctos
                if self.correo_correcto == correo: # comprobar que las dos cadenas sean iguales
                    print("Bienvenido")
                    break
                else:
                    print("Cuenta bloqueada a causa de un ataque")
                    break
            else:
                print("Por favor, introduzca un formato correcto (xxx@xx.x)")


print(Correo().validar())

