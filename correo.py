import re

class Correo:
    def __init__(self):
        self.correo_correcto = str("luciacantos@gmail.com")

    def validar(self):
        while True:
            correo = input("Introduce tu correo electrónico: ")
            if correo == "":
                print("'' es una entrada incorrecta. Introduzca una dirección de correo.")
            else:
                if re.search(".*@.*\..*", correo): # método para comprobar que los caracteres sean correctos
                    if self.correo_correcto == correo: # comprobar que las dos cadenas sean iguales
                        usuario = correo.split("@")[0]
                        print("Bienvenid@ " + usuario.capitalize())
                        break
                    else:
                        print("Cuenta bloqueada a causa de un ataque")
                        break
                else:
                    print("Una dirección de correo debe tener el formto xxx@xxx.xx")


Correo().validar() # al quitar print no devuelve el valor None
