def suma(a:Int, b:Int)=a+b
def resta(a:Int, b:Int)=a-b
def producto(a:Int, b:Int)=a*b
def division(a:Int, b:Int)=a/b

def calculadora (a:Int, b:Int, c:String) = {
	c match{
	case "suma" => suma(a,b)
	case "resta" => resta(a,b)
	case "producto" => producto(a,b)
	case "division" => division(a,b)
}
}

print("la suma es: " +calculadora(3,2,"suma") + "\n")
print("la resta es: " +calculadora(3,2,"resta") + "\n")
print("el producto es: " +calculadora(3,2,"producto") + "\n")
print("la division es: " +calculadora(3,2,"division") + "\n")

