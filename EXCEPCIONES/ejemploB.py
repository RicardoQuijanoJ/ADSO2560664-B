values = (1, 0) # se crea una tupla con el nombre vaules en donde tiene 2 elementos
#x,y=19,30
#print(divmod(10,3))
try:    #se presume que el bloque de código que esta en el try puede generar error
    q, r = divmod(*values)  # se crean 2 variables (q y r) en el cual va a estar el resultado de la función divmod
    #print('q=',q)
    print(f'q={q}') #   se imprime el resultado de q, utilizando plantillas literales
    print(f'r={r}') #   se imprime el resultado de r, utilizando plantillas literales
except (ZeroDivisionError, TypeError) as e: # Se maneja el error ya sea division por 0 o por tipo de dato y se asigna un alias al error llamado e
    print(type(e), e)   # se imprime el error: el tipo de error, y su significado