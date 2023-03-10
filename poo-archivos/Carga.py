from Vehiculo import *  # Se importa la clase vehiculo con todos sus atributos y métodos
class Carga(Vehiculo):  # Se crea la clase Carga que hereda de la clase Vehiculo
    def __init__(self,placa,conductor,capacidad,ejes):  # Se define el constructor de la clase carga con sus parametros
        Vehiculo.__init__(self,placa,conductor) # Se instancia el constructor de la clase Padre (Vehiculo)
        self.__capacidad=capacidad  # Se crea la variable de instancia y se le asigna el parametro
        self.__ejes=ejes  # Se crea la variable de instancia y se le asigna el parametro
    def getPlaca(self): #  Se crea el metodo 
        return self.__placa # Se retorna una variable ya creada
    def getCapacidad(self):
        return self.__capacidad
    def getConductor(self):
        return self.__conductor
    def getEjes(self):
        return self.__ejes
