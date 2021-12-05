def calculadora(v1,v2,operacion):
    return operacion(v1,v2)
def sumar(x1,x2):
    return x1+x2
def restar(x1,x2):
    return x1-x2
def multiplicar(x1,x2):
    return x1*x2
def dividir(x1,x2):
    return x1/x2

while True:
    print ("1. Sumar")
    print ("2. Restar")
    print ("3. Multiplicar")
    print ("4. Dividir")
    opcion = input("--> ")
    a = int(input("Introduce 1er numero: "))
    b = int(input("Introduce 2do numero: "))
    if opcion == "1":
        print(calculadora(a,b,sumar))
    elif opcion == "2":
        print(calculadora(a,b,restar))
    elif opcion == "3":
        print(calculadora(a,b,multiplicar))
    elif opcion == "4":
        print(calculadora(a,b,dividir))
    else:
        print("Saliendo de la aplicacion")






