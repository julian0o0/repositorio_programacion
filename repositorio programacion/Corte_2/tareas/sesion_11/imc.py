class Persona:
    def __init__(self, nombre, peso, altura):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def determinar_escala(self):
        imc = self.calcular_imc()
        if imc < 16.0:
            return "Infrapeso: Delgadez severa"
        elif 16.0 <= imc < 16.9:
            return "Infrapeso: Delgadez moderada"
        elif 17.0 <= imc < 18.4:
            return "Infrapeso: Delgadez leve"
        elif 18.5 <= imc < 24.9:
            return "Normal"
        elif 25.0 <= imc < 29.9:
            return "Sobrepeso"
        elif 30.0 <= imc < 34.9:
            return "Obesidad: Tipo I"
        elif 35.0 <= imc < 40.0:
            return "Obesidad: Tipo II"
        else:
            return "Obesidad: Tipo III (Mórbida)"
persona1 = Persona("Pedro Caceres", 97, 1.88)
persona2 = Persona("Maria Pérez", 47, 1.60)
persona3 = Persona("Julian Dominguez", 58, 1.58)
persona4 = Persona("Jessica Fuentes", 73, 1.70)

personas = [persona1, persona2, persona3, persona4]

for persona in personas:
    imc = persona.calcular_imc()
    escala = persona.determinar_escala()
    print(f"{persona.nombre} - IMC: {imc:.2f} - Escala: {escala}")