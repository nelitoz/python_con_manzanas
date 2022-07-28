class Padre:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print ("Hola")

class Hijo(Padre):
    def __init__(self,nombre, apellido, escuela):
        super().__init__(nombre,apellido)
        self.escuela = escuela

    def intro(self):
        super().saludo()

