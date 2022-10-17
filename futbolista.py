from persona import Persona
from deportista import Deportista
class Futbolista(Persona,Deportista):
    listaFutbolistas=[]
    def __init__(self,nombre,edad,altura,sexo,añosPracticando,golesMarcados,tarjetasRojas,piernaHabil):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,añosPracticando)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,goles):
        self._golesMarcados=goles
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,tarjetas):
        self._tarjetasRojas=tarjetas
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,pierna):
        self._piernaHabil=pierna
    def __str__(self):
        edad=str(self.edad)
        años=str(self.añosPracticando)
        deporte=self.deporte
        nombre=self.nombre
        texto= "Mi nombre es "+nombre+" soy profesional en el deporte "+deporte+" Tengo "+edad+" años de edad y llevo "+años+" años en el deporte"
        return texto
