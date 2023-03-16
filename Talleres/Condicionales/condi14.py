num1 = int(input("Escriba primer número\n"))
num2 = int(input("Escriba segundo número\n"))
num3 = int(input("Escriba tercer número\n"))
if num1 == num2:
    if num1 == num3:
        print("los números son iguales")
    else:
        print("El número del medio es: ",num1)
    
elif num2 == num3:
    print("El número del medio es: ",num2)
elif num3 == num1:
    print("El número del medio es: ",num1)
elif num1 < num2:
    if num1 < num3:
        if num2 < num3:
            print("el numero del medio es :",num2)
        else:
            print("el numero del medio es: ",num3)
elif num2 < num3:
    if num2 < num1:
        if num3 < num1:
            print("el numero del medio es :",num3)
        else:
            print("el numero del medio es: ",num1)
elif num3 < num2:
    if num3 < num1:
        if num2 < num1:
            print("el numero del medio es :",num2)
        else:
            print("el numero del medio es: ",num1)