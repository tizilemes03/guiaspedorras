--Guia 4 Recursividad Tizi
--Ejercicio 1
fibonacci :: Integer -> Integer
fibonacci n|n==0 =0
           |n==1 =1
           |otherwise = fibonacci(n-1) + fibonacci(n-2)
-- la funcion se define recursivamente y se va llamando a si misma hasta reducirse en los casos base
--con pattern matching
fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib(n-1) + fib(n-2)

-- Ej 2 parte entera
parteEntera :: Float -> Int
parteEntera r |0<=r && r<1 = 0
              |r>=1 = 1 + parteEntera(r-1)
              |otherwise = -1 + parteEntera(r+1)

-- Ej 3 esdivisible
-- problema esdivisible {(n,m:N):Bool}
-- requiere {n y m mayores a 0}
-- asegura {res es verdadero si el numero m divide a n, en caso contrario devuelve false}

esdivisible :: Int -> Int -> Bool
esdivisible n m|n==0 = True
               |n<m =False
               |n==m =True 
               |m<0 = esdivisible (n+m) m
               |otherwise = esdivisible (n-m) m

-- Ej 4 sumaImpares
nesimoimpar :: Int -> Int 
nesimoimpar n = 2*n-1

sumaimpares :: Int -> Int 
sumaimpares n|n==1 =1
             |n==0 =0
             |otherwise = nesimoimpar n + sumaimpares (n-1)

-- Ej 5 mediofact
mediofact :: Int -> Int 
mediofact n |n==1 =1
            |n==2 =2
            |n==0 =1
            |otherwise= n * mediofact(n-2)

-- Ej 6 sumadigitos
sumadigitos :: Int -> Int 
sumadigitos n|n<10 = n
             |otherwise= sumadigitos (mod n 10) + sumadigitos (div n 10)
             
--agregado random sumacantdigitos
cantdigitos :: Int -> Int 
cantdigitos n|n<10 = 1
             |otherwise= cantdigitos (mod n 10) + cantdigitos (div n 10)
             
-- Ej 7 Funcion todosDigitosIguales con recursividad
ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacarUltimo :: Int -> Int
sacarUltimo  n = div n 10

todosDigitosIguales :: Int -> Bool
todosDigitosIguales n|n<10 = True
                     |ultimoDigito n /= ultimoDigito (sacarUltimo n) = False
                     |otherwise = ultimoDigito n== ultimoDigito(sacarUltimo n) && todosDigitosIguales(sacarUltimo n)

-- Ejercicio 8: i-esimodigito 
-- iesimodigito (n:Z,i:N):Z
-- requiere {n>=0 && 1<=i<= Cantdigitos(n)}
-- asegura: { resultado = (n div 10 ** cantDigitos(n)−i) mod 10 }
--problema cantDigitos (n: Z) : N {
--requiere: { n ≥ 0 }
--asegura: { n = 0 → resultado = 1}
--asegura: { n =/ = 0 → (n div 10 **resultado−1 > 0 ∧ n div 10resultado = 0) }
iesimodigito :: Int -> Int -> Int
iesimodigito n i |cantdigitos n == i = ultimoDigito n 
                 |otherwise = iesimodigito (sacarUltimo n) i

--Ejercicio 9: esCapicua
-- escapicua {n:N}:Bool
-- requiere {n es un número mayor o igual a 0}
-- asegura {res = True <-> n es un nùmero capicùa}
-- primer digito y el ultimo son iguales.
primerdigito :: Int -> Int 
primerdigito n |n<10 =n
               |otherwise= div n (10 ^((cantdigitos n)-1))

escapicua :: Int -> Bool 
escapicua n|n<10 =True
           |otherwise= ultimoDigito n == primerdigito n && escapicua(primerdigito(sacarUltimo n))

-- Ejercicio 10:
-- a) La Geomètrica de 2
-- sumageo2
--requiere
--asegura
sumageo2 :: Int -> Int -> Int 
sumageo2 2 i |i==0 = 1
             |otherwise= 2^i + sumageo2 2 (i-1)
-- b) La Geometrica de q^i con i entre 1 y n
--
--
--
sumageo :: Int -> Int -> Int 
sumageo n q |n==1 =q
            |otherwise = q^n + sumageo (n-1) q
-- c)  La Geometrica de q^i con i entre 1 y 2n
--
--
--
sumageo2n :: Int -> Int -> Int 
sumageo2n n q =sumageo (2*n) q
--d) La Geometrica de q^i con i entre n y 2n
--sumageo2nn {n,q:Z}
--
sumageo2nn :: Int -> Int -> Int 
sumageo2nn n q =sumageo2n q n - sumageo (n-1) q 

-- Ejercicio 11: aproximador del numero e
-- eaprox  {n:Z}:R 
-- requiere {n es mayor igual a 0}
-- asegura {resultado es la sumatoria de 1/factorial(i) con i entre 0 y n}
-- factorial(x) (n:Z):Z
-- requiere {n mayor o igual a 0}
-- asegura {resultado en el producto de todos los numeros naturales hasta n sin repetirse}

factorial :: Integer -> Integer
factorial n|n==0 =1 
           |n>0 = n * factorial (n-1)
-- para que matchee factorail con eaprox debo definir factorial para float
-- Preguntar en que caso precisamos el frominteger
factorialf :: Integer -> Float 
factorialf n |n==0 = 1.0
             |n>0 = fromInteger n * factorialf (n-1)

eaprox :: Integer -> Float
eaprox n|n==0 =1
        |otherwise= (1 / factorialf n) + eaprox n-1   
--b)
e :: Float 
e = eaprox 9 

--Ejercicio 12:
--Especificación: 
raizde2Aprox :: Integer -> Float 
raizde2Aprox n= (recursiondef n) - 1.0

recursiondef :: Integer -> Float 
recursiondef n |n==1 = 2.0
               |n>1 = 2.0 + (1/recursiondef (n-1))

--Ejercicio 13:
-- sumatoriadoble 
sumatoriadoble :: Int -> Int -> Int
sumatoriadoble n m|n==0 =0
                  |otherwise= sumatoriainterna n m + sumatoriadoble (n-1) m

sumatoriainterna :: Int-> Int -> Int 
sumatoriainterna n m|m==0 =0
                    |otherwise= n^m + sumatoriainterna n (m-1)
--agregado lol por error de ejercicio 14
productodesumageo :: Int -> Int -> Int -> Int 
productodesumageo n m q|n==0 && m==0 =0 
                        |otherwise= (sumageo n q) * (sumageo m q)
-- con sumageo ya definida, al ser "q" la base definida para ambas sumatorias, la recursividad se aplica sobre el exponente que va variando.
--Ejercicio 14:
--sumatoriapotencias
sumatoriapotencias :: Int -> Int -> Int -> Int 
sumatoriapotencias q n m|n==1 =q^(m+1)
                        |otherwise= sumavariable q n m + sumavariable q (n-1) m  
sumavariable :: Int -> Int -> Int -> Int 
sumavariable q n m|m==1 =q^(n+1) 
                  |otherwise= q^(n+m) + sumavariable q n (m-1) 

--Ejercicio 15
sumaRacionales :: Integer -> Integer -> Float 
sumaRacionales n m| n==0 =0
                  |n==1 && m==1 =1
                  | otherwise= sumatoriaq n m + sumaRacionales (n-1) m
sumatoriaq :: Integer -> Integer -> Float 
sumatoriaq n m|m==0 =0
              |n==1 && m==1 =1
              |otherwise = (fromInteger n)/(fromInteger m) + sumatoriaq n m-1 

--Ejercicio 16 a)menordivisor
menordivisor :: Int -> Int 
menordivisor p|p==1 =1
              |p==2 =2
              |otherwise= divisor p 2
divisor :: Int-> Int -> Int 
divisor x y |x==y =y
            |mod x y==0 =y 
            |otherwise = divisor x (y+1)
--b) esPrimo
esPrimo :: Int -> Bool 
esPrimo p|menordivisor p==p =True 
         |menordivisor p==1 =False 
         |otherwise=False 
--c)  sonCoprimos 
sonCoprimos :: Int -> Int -> Bool 
sonCoprimos p q|(menordivisor p) /= (menordivisor q) && ((mod p (menordivisor q)) /=0) && (mod q (menordivisor p) /=0) = True 
               |otherwise= False 
--d) nesimoprimo
nesimoPrimo :: Int -> Int 
nesimoPrimo i= nesimoPrimoaux 2 i 

quePrimo :: Int -> Int
quePrimo 2 = 1
quePrimo n|esPrimo n ==True =1 + quePrimo (n-1)
          |otherwise= quePrimo (n-1) 
--para poder arrancar con el 2 como primer primo e ir sumando cantidad de primos y saber donde parar defino:
nesimoPrimoaux :: Int -> Int -> Int 
nesimoPrimoaux n i|quePrimo n==i =n 
                   |otherwise= nesimoPrimoaux (n+1) i 

--Ejercicio 17:
--problema esFibonacci (n: Z) : B {
--requiere: { n ≥ 0 }
--asegura: { resultado = true ↔ n es alg´un valor de la secuencia de Fibonacci definida en el ejercicio 1}
--}
--escribo un fibonacci para el 17
fibonacci17 :: Integer -> Integer 
fibonacci17 0 =0
fibonacci17 1 =1 
fibonacci17 n|n>1 = fibonacci17 (n-1) + fibonacci17 (n-2)

fibocompara2 :: Integer -> Integer -> Bool 
fibocompara2 _ (-1) = False 
fibocompara2 n m|n== fibonacci17(m) =True 
                |otherwise= fibocompara2 n (m-1)

esfibonacci :: Integer -> Bool 
esfibonacci n= fibocompara2 n 32

--Ejercicio 18: 
esPar :: Int -> Bool 
esPar n|mod n 2 ==0 =True 
       |otherwise=False 

mayordgpar :: Int -> Int 
mayordgpar n = comparacionnum n (-1)

comparacionnum :: Int -> Int -> Int 
comparacionnum n m|n==0 =m 
                  |esPar(ultimoDigito n) && (ultimoDigito n) >m = comparacionnum (ultimoDigito n) (sacarUltimo n)
                  |otherwise= comparacionnum (sacarUltimo n) m 


