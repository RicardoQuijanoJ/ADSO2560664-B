num1 = int(input("Escriba primer número\n"))
num2 = int(input("Escriba segundo número\n"))
num3 = int(input("Escriba tercer número\n"))
if num1 == num2:
    if num1 == num3:
        print("los números son iguales")
    else:
        print ("Hay 2 numeros iguales")
elif num2 == num3:
    print ("Hay 2 numeros iguales")
elif num1 == num3:
    print ("Hay 2 numeros iguales")
else:
    print ("todos los números son diferentes")