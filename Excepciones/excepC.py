def try_syntax(numerator, denominator): #se define una funcion llamada try_syntax y recibe 2 parametros
    try:    #se presume que el bloque de código que esta en el try puede generar error
        print(f'In the try block: {numerator}/{denominator}')   #Se imprime un texto en un formato (plantilla literal) mostrando los 2 parametros
        result = numerator / denominator    # se hace la operación
    except ZeroDivisionError as zde:    #se maneja la excepción de division por 0 
        print(zde)  # se imprime el error
    else:   # si no hay error entonces entra a este bloque de código
        print('The result is:', result) # Se imprime el resultado de la división
        return result   # retorna el resultado
    finally:    # Es opcional y sirve tmbien para dar por terminada la excepción y mostrar algo
        print('Exiting')    # imprime una linea de código
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 0))    # imprime el resultado del llamado de la función enviandole los parametros (11 y 0)