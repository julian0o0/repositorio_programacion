class Ciudadano:
    def __init__(self, nombre, cedula, edad):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_cedula(self):
        return self.__cedula

    def set_cedula(self, cedula):
        if len(str(cedula)) == 8 or len(str(cedula)) == 10:
            self.__cedula = cedula
        else:
            print("La cédula debe tener 8 o 10 dígitos")

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un número positivo y mayor que 0")

    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}, Cédula: {self.__cedula}, Edad: {self.__edad}")

    def es_mayor_de_edad(self):
        return self.__edad >= 18
ciudadano1 = Ciudadano("Juan", 12345678, 25)
ciudadano1.mostrar_informacion()
print("¿Es mayor de edad?", ciudadano1.es_mayor_de_edad())

ciudadano1.set_cedula(123)
ciudadano1.set_edad(-5)