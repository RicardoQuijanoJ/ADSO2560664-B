class A1:   #   Se crea una clase (A1)
    def __init__(self): #   Se crea el constructor de la clase
        pass    
    def saludo(self):   #   se crea un metodo (saludo) que no recibe parametros 
        print('Hola desde A1')  #   se imprime un mensaje de texto

class A2:   #   se crea una clase (A2)
    def __init__(self): #   Se crea el constructor de la clase (A2)
        pass
    def saludo(self):   #   se crea un metodo (saludo) que no recibe parametros 
        print('Hola desde A2')  #   Se imprime un mensaje de texto

class B(A2,A1): #   se crea una clase (B) que recibe 2 parametros (A2,A1)
    def __init__(self): # Se crea el constructor de la clase (B)
        pass
    def saludo(self):   #   se crea un metodo (saludo) que no recibe parametros 
        print('Hola desde B')   #   Se imprime un mensaje de texto
    def __str__(self):  #   se crea el metodo que no recibe parametros
        return 'Soy un objeto de la clase B'    # se retorna una cadena de texto

obj=B() #   se crea un objeto (obj) que instancia la clase B 
print(obj.__str__())    #   se imprime el resultado de la invocación del metodo __str__
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())