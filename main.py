from Class_Beneficio import Beneficio

#beneficiario = Beneficio("Johnnatan","Benavides",1085339929,24,1150000)
#beneficiario.consignar()

from Class_Beneficio import Beneficio
import platform
import os

ban = True

print(f"*** Bienvenido a su cuenta de ahorros ***")
print("-------------------------------------------")
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
cedula = input("ingrese su cedula: ")
edad = input("ingrese su edad: ")
saldo = input("ingrese su saldo: ")
print("\n\n")

beneficiario = Beneficio(nombre, apellido, cedula, int(edad), int(saldo))
print("Ingreso exitoso...")
print("-------------------------------------------\n")

while(ban):

    opcion = input("Por favor ingrese la opcion que desea realizar\n"
                   "1. Consignar.\n"
                   "2. Retirar.\n"
                   "3. Resumen de la Cuenta\n"
                   "4. Validar si es Beneficiario\n"
                   "5. Salir\n\n\n")

    match opcion:
        case "1":
            beneficiario.consignar()
            os.system("pause")
        case "2":
            beneficiario.retirar()
            os.system("pause")
        case "3":
            beneficiario.resumen()
            os.system("pause")
        case "4":
            if(beneficiario.validarBeneficio()):
                beneficiario.mostrarBeneficio()
                os.system("pause")
            else:
                print("No seres beneficiario")
                os.system("pause")
        case "5":
            ban = False
            print("Saliendo...")
        case _:
            print("Opcion incorrecta, por favor vuelve a intentarlo")




