calculadora :: String -> Int -> Int -> Int
calculadora cad x y
    | cad =="suma" = x + y
    | cad == "resta" = x - y 
    | cad == "producto" = x * y
    | cad == "division" = x `div` y
