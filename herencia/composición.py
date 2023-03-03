class Curso:    #   Se crea la clase Curso
    def __init__(self,titulo):  #   Se crea el constructor de la clase Curso con un parametro (titulo)
        self.__titulo=titulo    #   Se le asigna el parametro al atributo

    def getTitulo(self):    #   Se crea un metodo llamado getTitulo y no recibe parametro
        return self.__titulo    #   Se retorna el dato almacenado en la variable 

class Aprendiz: #   Se crea una clase Aprendiz
    def __init__(self,nombre):  #   Se crea el constructor de la clase Aprendiz con un parametro (nombre)
        self.__nombre=nombre    #   Se le asigna el parametro (nombre) a la variable (self.__nombre)
        self.__cursos=[]    #   Se crea una lista llamada curso inicialmente vacia

    def agregarCurso(self,nombreCursito): # Se crea un metodo (agregarCurso) y recibe un parametro (nombreCursito)
        cursito=Curso(nombreCursito)    #   Se crea una variable para instanciar la clase Curso que recibe el parametro del metodo (agregarCurso)
        self.__cursos.append(cursito)   #

    def getCursos(self):
        return self.__cursos
    
ap=Aprendiz('Sofia')
ap.agregarCurso('Python Basico')
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos():
    print(c.getTitulo())
