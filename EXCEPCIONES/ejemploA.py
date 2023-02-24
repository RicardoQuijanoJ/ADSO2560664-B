try:    #se presume que el bloque de código que esta en el try puede generar error
    #print(1/1))    
    raise SyntaxError   # Hacer que se genere un error de Sintaxis
except SyntaxError: # Manejar el error
    print('Cierra el parentesis')   # imprime un mensaje de error