from Class_Usuario import Usuario


class Cuenta(Usuario):
    #Constructor
    def __init__(self, nombre, apellido, cedula, edad, cantidadAhorro):
        Usuario .__init__(self, nombre, apellido, cedula, edad)
        self.cantidadAhorro = cantidadAhorro

    #Metodos get
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.Apellido

    def getEdad(self):
        return self.edad

    def getCedula(self):
        return self.cedula

    def getCantidadAhorro(self):
        return self.cantidadAhorro

    #Metodos set
    def setCantidadAhorro(self, cantidadAhorro):
        self.cantidadAhorro = cantidadAhorro

    #metodo para mostrar resumen del cliente
    def resumen(self):
        print(f"Hola! {self.nombre} {self.apellido}\n"
              f"estos son tus datos:\n"
              f"--------------------\n"
              f"CC: {self.cedula}\n"
              f"edad: {self.edad}\n"
              f"Saldo: ${self.cantidadAhorro}")

    def consignar(self):
        ban = True
        while(ban):
            valorConsignar = input("digite el valor que desea consignar: ")
            if(int(valorConsignar)>0):
                self.cantidadAhorro += (int(valorConsignar))
                print(f"Consignacion exitosa! su saldo actual es de: ${self.cantidadAhorro}")
                ban = False
            else:
                print("Error en la consignacion, ingresa un valor mayor que 0 (cero)")

    def retirar(self):
        valorRetirar = input("digite el valor que desea retirar: ")
        if (int(valorRetirar) <= self.cantidadAhorro):
            self.cantidadAhorro -= int(valorRetirar)
            print(f"Retiro exitoso! su saldo actual es de: ${self.cantidadAhorro}")
        else:
            print("Saldo insuficiente...")



