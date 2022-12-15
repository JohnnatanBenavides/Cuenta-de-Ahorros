from Class_Cuenta import Cuenta


class Beneficio(Cuenta):
    def __init__(self, nombre, apellido, cedula, edad, cantidadAhorro):
        Cuenta .__init__(self, nombre, apellido, cedula, edad, cantidadAhorro)

    def validarBeneficio(self):
        return self.edad >=18 and self.edad<28

    def mostrarBeneficio(self):
        interes = self.cantidadAhorro * 0.05
        print(f"Eres Beneficiario su saldo con interes del 5% es: ${self.cantidadAhorro+interes}")

