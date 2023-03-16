numero=int(input("Ingrese un numero para calcular el mes: "))
if numero<=31:
    print("Enero")
elif numero >31 and numero <= 60:
    print("Febrero")
elif numero >60 and numero <= 91:
    print("Marzo")
elif numero > 91 and numero <= 121:
    print("Abril")
elif numero > 121 and numero <= 152:
    print("Mayo")
elif numero > 152 and numero <= 182:
    print("Junio")
elif numero > 182 and numero <= 213:
    print("Julio")     
elif numero > 213 and numero <= 244:
    print("Agosot")
elif numero > 244 and numero <= 270:
    print("Septiembre")
elif numero > 270 and numero <= 301:
    print("Octubre")
elif numero > 301 and numero <=  331:
    print("Noviembre")
elif numero > 331 and numero <= 362:
    print("Diciembre")          
else :
    print("ERROR")
                