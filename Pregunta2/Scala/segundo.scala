val suma1:(Int, Int)=> Int = (x,y)=>x+y
val resta1:(Int, Int)=> Int = (x,y)=>x-y
val producto1:(Int, Int)=> Int = (x,y)=>x*y
val division1:(Int, Int)=> Int = (x,y)=>x/y

def calculadora1 (x:Int, y:Int, op:String) ={
     op match{
     case "suma" => suma1(x,y)
     case "resta" => resta1(x,y)
     case "producto" => producto1(x,y)
     case "division" => division1(x,y)
     }
     }

// a.toFloat/b

print("la suma es: " +calculadora1(10,2,"suma") + "\n")
print("la resta es: " +calculadora1(10,2,"resta") + "\n")
print("el producto es: " +calculadora1(10,2,"producto") + "\n")
print("la division es: " +calculadora1(10,2,"division") + "\n")