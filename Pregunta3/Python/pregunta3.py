print ("introduzca la cadena: ")
cadena = input()
lista=[]
for i in cadena:
    if i!=" ":
        lista.append(i) 

lista2=[]
cad=""
for i in cadena:
    if i != " ": 
        cad = cad + i
    else:
        lista2.append(cad)
        cad = ""
lista2.append(cad)
    
print(lista2)
print(lista)
# print(cadena.split())



