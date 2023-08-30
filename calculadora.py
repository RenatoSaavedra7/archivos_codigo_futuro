# funcion suma

def sumar (a,b):
    return a + b

# funcion resta

def restar (a, b):
    return a - b 

# funcion multiplicación
def multiplicar (a , b):
    return a * b 

# funcion división
def dividir (a , b):
    return a / b

def calculadora():
    operación=input("QUE OPERACIÓN DEBE REALIZAR(+,-,*./)")

    num1= float(input("INGRESE EL PRIMER NÚMERO:"))
    num2= float(input("INGRESE EL SEGUNDPO NÚMERO:"))

    if operación == "+":
        print("el resultado es :", sumar (num1, num2))

    elif operación == "-":
        print("el resultado es :",restar (num1, num2))



    elif operación=="*":
        print("el resultado es :", multiplicar (num1, num2))
    elif operación=="/":
        print("el resultado es :", dividir (num1, num2))
    else:
        print("operación no valida")
calculadora()
