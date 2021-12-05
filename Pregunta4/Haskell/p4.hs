sumaj::  Int -> Int -> Int
sumaj = (\x y -> x + y)

resta::  Int -> Int -> Int
resta = (\x y -> x - y)

producto::  Int -> Int -> Int
producto = (\x y -> x * y)

division:: Fractional a => a-> a -> a
division = (\x y -> x / y)


calculadora f = f
 