def calculadora(x,y,op):
    if(op=="suma"):
        return suma(x,y)
    elif(op=="resta"):
        return resta(x,y)
    elif(op=="producto"):
        return producto(x,y)
    elif(op=="division"):
        return division(x,y)
def suma(x,y): return "La suma es: " + str(x+y)
def resta(x,y): return "La resta es: " + str(x-y)
def producto(x,y): return "El producto es: " + str(x*y);
def division(x,y): return "La division es: " + str(x/y);

print(calculadora(5,5,"suma"))
print(calculadora(5,5,"resta"))
print(calculadora(5,5,"producto"))
print(calculadora(5,5,"division"))
