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
        cursito=Curso(nombreCursito)    #   Se crea un objeto (cursito) que instancia la clase Curso que recibe el parametro del metodo (agregarCurso)
        self.__cursos.append(cursito)   #   Se agrega en la lista (cursos) de esta clase (Aprendiz)  el dato (cursito)

    def getCursos(self):    #   Se crea un metodo llamado getCursos
        return self.__cursos    #   retorna la lista (cursos) de esta clase (Aprendiz)
    
ap=Aprendiz('Sofia')    #   se crea un objeto (ap) que instancia la clase Aprendiz y envia como paramentro un dato(Sofia)
ap.agregarCurso('Python Basico')    #   desde el objeto (ap) se invoca el metodo (agregarCurso) de la clase que anteriormente fue instanciado y se le envia como parametro el dato
ap.agregarCurso('Python Intermedio')    #   desde el objeto (ap) se invoca el metodo (agregarCurso) de la clase que anteriormente fue instanciado y se le envia como parametro el dato

for c in ap.getCursos():    #   se crea un ciclo en donde la variable (c) va a tomar el dato de las posiciones de la lista invocada en el metodo (ap.getCursos)
    print(c.getTitulo())    #   Se imprime la variable (c) 