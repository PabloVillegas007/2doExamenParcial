suma = lambda x,y:x+y
resta = lambda x,y:x-y
producto = lambda x,y:x*y
division = lambda x,y:x/y
def calculadora(x,y,op):
    if(op=="suma"):
        return suma(x,y)
    elif(op=="resta"):
        return resta(x,y)
    elif(op=="producto"):
        return producto(x,y)
    elif(op=="division"):
        return division(x,y)

print ("La suma es : ", calculadora(3,2,"suma"))
print ("La resta es : ", calculadora(3,2,"resta"))
print ("El producto es :", calculadora(3,2,"producto"))
print ("La division es : ",calculadora(3,2,"division"))
