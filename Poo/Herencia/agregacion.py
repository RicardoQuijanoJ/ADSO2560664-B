class Aprendiz: #   Se crea una clase Aprendiz
    def __init__(self,nombre):  #   Se crea el constructor de la clase Aprendiz con un parametro (nombre)
        self.__nombre=nombre    #   Se le asigna el parametro al atributo
        self.__cursos=[]    #   se crea una lista vacia llamada (cursos)

    def agregarCurso(self,titulo):  # se crea un metodo (agregarCurso) que recibe como parametro un dato (titulo)
        self.__cursos.append(titulo)    # se le agrega a la lista creada en el constructor de la clase (Aprendiz) el dato que recibe como parametro (titulo)

    def getCursos(self):    #   Se crea un metodo llamado getCursos
        return self.__cursos    #   retorna la lista (cursos) de esta clase (Aprendiz)

class Curso:    #   Se crea la clase Curso
    def __init__(self,titulo):  #   Se crea el constructor de la clase Curso con un parametro (titulo)
        self.__titulo=titulo    #   Se le asigna el parametro al atributo

    def getTitulo(self):    #   Se crea un metodo llamado getTitulo y no recibe parametro
        return self.__titulo    #   Se retorna el dato almacenado en la variable 
    
a=Aprendiz('Martha')    #   se crea un objeto (a) que instancia la clase Aprendiz y envia como paramentro un dato(Martha)
c1=Curso('Python Intermedio')   #   se crea un objeto (c1) que instancia la clase Curso y envia como paramentro un dato(Python Intermedio)
c2=Curso('Python Basico')   #   se crea un objeto (c2) que instancia la clase Curso y envia como paramentro un dato(Python Basico)
c3=Curso('Introduccion a Java') #   se crea un objeto (c3) que instancia la clase Curso y envia como paramentro un dato(Introduccion a Java)

a.agregarCurso(c1)  #   Desde el objeto (a) se invoca el metodo de la Clase (Aprendiz) y se le agrega un dato (c1) a este
a.agregarCurso(c2)  #   Desde el objeto (a) se invoca el metodo de la Clase (Aprendiz) y se le agrega un dato (c2) a este
a.agregarCurso(c3)  #   Desde el objeto (a) se invoca el metodo de la Clase (Aprendiz) y se le agrega un dato (c3) a este

print(a.getCursos())    #   se imprime el espacio de memoria de los datos de la lista al invocar el metodo (a.getCursos())

for curso in a.getCursos(): #   se crea un ciclo en donde la variable (curso) va a tomar el dato de las posiciones de la lista invocada en el metodo (ap.getCursos)
    print(curso.getTitulo())    #   Se imprime la variable (curso)