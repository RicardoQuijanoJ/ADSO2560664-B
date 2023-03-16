def edad(): # se crea una función llamada edad y no recibe parametros
    try:    #se presume que el bloque de código que esta en el try puede generar error
        tuedad=int(input("introduce tu edad"))  #se crea una variable que recibe un dato entero, osea un numero
        print(f'tu edad es  {tuedad}')  # se imprime en formato (plantilla literal) la edad que digito
        #print('Tu edad es ',tuedad)
    except ValueError as e: # se maneja el error ValueError con el alias e
        print(e)    # se imprime la definicion del error
        print("La edad debe ser un valor numerico...")  # se imprime un mensaje para recordarle al usuario como debe de escribir
        edad()  # se invoca de nuevo la función (recursividad)
    else:   # si no hay error entra al else
        print('Viene por el else')  # se imprime una linea de texto mostrando un mensaje

edad()  # se llama la funcion