def separaCaracteres(c:String) : List[Char] = {
     c.toList}


def separaPalabras(c:String) : Array[java.lang.String] = {
     c.split(" ")
}


print ("Separado en Caracteres : " + separaCaracteres("Pablo Villegas Yujra") + "\n")
print ("Separado en palabras : " + separaPalabras("Pablo Villegas Yujra"))
      
