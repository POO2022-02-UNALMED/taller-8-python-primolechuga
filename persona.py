
class Persona:
    def __init__(self,nombre,edad,altura,sexo):
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        self.sexo=sexo
    
    def getNombre(self):
        return self.nombre
    def setNombre(self, nombre):
        self.nombre=nombre
    def getEdad(self):
        return self.edad
    def setEdad(self, Edad):
        self.edad=Edad
    def getAltura(self):
        return self.altura
    def setAltura(self, Altura):
        self.altura=Altura
    def getSexo(self):
        return self.sexo
    def setSexo(self, Sexo):
        self.sexo=Sexo
    