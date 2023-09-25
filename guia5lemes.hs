import System.Win32 (COORD(xPos))
-- ej 1.1
longitud ::[t] -> Int
longitud [] = 0
longitud s = 1 + longitud(tail s) 
-- ej 1.2 ultimo
ultimo :: [t] -> t
ultimo s |longitud s==1 =head s
         |otherwise = ultimo(tail s) 
-- ej 1.3 principio 
principio :: [t] -> [t] 
principio [x] = []
principio (x:xs) = (x : principio xs)
-- ej 1.4 reversivo 
reversivo :: [t] -> [t]
reversivo [x] = ultimo [x] : []
reversivo (x:xs) = ultimo (x:xs): reversivo (principio (x:xs)) 

-- Ejercicio 2 2.1
pertenece :: (Eq t) => t -> [t] -> Bool 
pertenece a s|s==[] =False 
             |a== (head s) = True
             |otherwise= pertenece a (tail s) 

-- ej 2.2 todosIguales 
todosiguales :: (Eq t) => [t] -> Bool 
todosiguales [] = False
todosiguales [x]= True 
todosiguales (x:xs) = x == head xs && x == ultimo xs && todosiguales (principio xs) 
-- ej 2.3 
todosdistintos :: (Eq t) => [t] -> Bool 
todosdistintos [] = False 
todosdistintos [x] = True 
todosdistintos (x:y:xs) |x/=y = todosdistintos (y:xs) && todosdistintos (x:xs)
                        |x==y = False 

-- ej 2.4hayrepetidos
-- escrito con pattern matching, ver como escribirlo con los guardas por mi mismo
hayrepetidos :: (Eq t) => [t] -> Bool               
hayrepetidos [] = False
hayrepetidos (x:xs) = pertenece x xs || hayrepetidos xs 

-- ej 2.5 quitar
quitar :: (Eq t) => t -> [t] -> [t]
quitar _ [] = []
quitar y (x:xs)|y == x = xs 
               |otherwise = quitar y xs

-- ej 2.6 quitartodos 
quitartodos :: (Eq t) => t -> [t] -> [t]
quitartodos _ [] = []
quitartodos a (x:xs)|a==x = quitartodos a xs 
                    |otherwise = (x:quitartodos a xs)
                     
-- ej 2.7
-- eliminarRepetidos :: (Eq t) => [t] -> [t] que deja en la lista una única aparición de cada elemento, eliminando las repeticiones adicionales
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos []=[]
eliminarRepetidos (x:y:xs)|hayrepetidos (x:y:xs) == True && x==y = (x: quitartodos y (x:y:xs)) 
                          |otherwise= x : eliminarRepetidos (quitartodos x (x:y:xs))

--chequear como arreglarlo para hacerlo mas corto
--ej 2.8 contienemismos
contienemismos :: (Eq t) => [t] -> [t] -> Bool
contienemismos a b = versipertenecen a b && versipertenecen b a 
--creo funcion que evalue los elemtos de una funcion si pertenecen elementos entre ellos y despues las comparo en contienemismos

versipertenecen :: (Eq t) => [t] -> [t] -> Bool 
versipertenecen [] _ = True 
versipertenecen a b = pertenece (head a) b && versipertenecen (tail a) b 

--ej 2.9 escapicua
escapicua :: (Eq t) => [t] -> Bool 
escapicua s|reversivo s == s =True 
           |otherwise= False 

--Ejercicio 3 
--como va de i=0 hasta |s|-1 suma todo elemento de la lista
sumatoria :: [Integer] -> Integer 
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs 

--ej 3.2 productoria
productoria :: [Integer] -> Integer 
productoria [] = 1 
productoria (x:xs) = x * productoria xs 

--ej 3.3 maximo
maximo :: [Integer]-> Integer
maximo [x] = x 
maximo (x:y:xs)|x>=y = maximo (x:xs) 
               |otherwise = maximo (y:xs)

--ej 3.4 sumarN
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n [] = []
sumarN n (x:xs) = (x+n: sumarN n xs)

--ej 3.5 sumarElPrimero 
sumarElprimero :: [Integer] -> [Integer]
sumarElprimero (x:xs) = sumarN x (x:xs)

--ej 3.6 sumarElultimo
sumarElUltimo :: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo(x:xs)) (x:xs)

--ej 3.7 pares
pares :: [Integer] -> [Integer]
pares [] = []
pares (x:xs)|esPar x == True = (x : pares xs)
            |otherwise = pares xs 
esPar :: Integer -> Bool
esPar x|mod x 2 ==0 = True
       |otherwise = False 

--ej 3.8 multiplosdeN
{--
multiplosDeN :: Integer -> [Integer] -> [Integer] que dado un numero n y una lista xs, devuelve una lista
con los elementos de xs multiplos de n
--}

multiplosdeN :: Integer -> [Integer] -> [Integer]
multiplosdeN n [] = []
multiplosdeN n (x:xs)| mod x n ==0 = (x : multiplosdeN n xs)
                     |otherwise = multiplosdeN n xs 

--ej 3.9 ordenar :: [Integer] -> [Integer] que ordena los elementos de la lista en forma creciente
-- contiene funciones auxiliares tal vez excesivas

ordenar :: [Integer] -> [Integer]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs)= (menordelista (x:xs) : ordenar (quitari (menordelista(x:xs)) (x:xs))) 

quitari :: Integer -> [Integer] -> [Integer]
quitari _ [] = []
quitari y (x:xs)|y == x = quitari y xs 
               |otherwise = x: quitari y xs

menordelista :: [Integer] -> Integer 
menordelista [x] = x 
menordelista xs = (menorelemento (head xs) (tail xs)) 

menorelemento :: Integer -> [Integer] -> Integer 
menorelemento x [] = x 
menorelemento x (y:xs)|x>y = menorelemento y xs 
                      |otherwise = menorelemento x xs
-----------------------EJERCICIO 4 LOCO -------------------

{--ej 1: sacarBlancosRepetidos :: [Char] -> [Char], que reemplaza cada subsecuencia de blancos contiguos de la primera lista por un solo blanco en la lista resultado.
lo que hace el pibe es agarrar y los espacios demás que hayan, los elimina xq estan al re pedo --}
sacarblancosrepetidos :: [Char] -> [Char] 
sacarblancosrepetidos [] = []
sacarblancosrepetidos [x] = [x]
sacarblancosrepetidos (x:y:xs)|x==y && x==' ' = sacarblancosrepetidos (y:xs)
                              |otherwise = (x:sacarblancosrepetidos (y:xs))
--si arranca con doble blanco, solo saca uno por eso me deja por ejemplo " hi"

{--ej 2: contarPalabras :: [Char] -> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que tiene.--}
contarPalabras :: [Char] -> Integer 
contarPalabras (xs) = cuentablancos (espacioinifinout (sacarblancosrepetidos xs)) + 1
--uso un acumulativo pues en el caso de que haya una sola palabra solo sumo 1
--defino funciones auxiliares para sacar los espacios del principio y del fin, trabajando sobre una lista q le aplico sacarblancosrepetidos.
espaciofinalout :: [Char] -> [Char]
espaciofinalout []= []
espaciofinalout [x]|x==' ' = []
                   |otherwise = [x]
espaciofinalout (x:xs) = (x:espaciofinalout xs)
--estaba mal el caso de un solo elemento que es fundamental al pasar de char en char!
espacioinifinout :: [Char] -> [Char]
espacioinifinout [] = []
espacioinifinout (x:xs)|x==' ' = espaciofinalout xs
                       |otherwise= (x:espaciofinalout xs)
 
--en realidad me falto la funcion que si reconoce un espacio, sabe que luego hay una palabra y le asigna un acumulativo, entonces la defino.
cuentablancos :: [Char] -> Integer 
cuentablancos []= 0
cuentablancos (x:xs)|x==' ' = 1 + cuentablancos xs 
                    |otherwise = cuentablancos xs 

--ej 4.3 palabras :: [Char] -> [[Char]], que dada una lista arma una nueva lista con las palabras de la lista original
--primero hago el armador de primera palabra
primerapalabra :: [Char] -> [Char]
primerapalabra [] = []
primerapalabra (x:xs)|x==' '= []
                     |otherwise = (x:primerapalabra xs)
--primero la defino así, pero como la voy a usar sobre sacarblancosrepetidos e inifinout no habrá problema 
--(pongo a prueba)
devolvedordeprimera :: [Char] -> [Char]
devolvedordeprimera (x:xs) = primerapalabra (espacioinifinout (sacarblancosrepetidos (x:xs)))

--ahora tengo que definir la auxiliar que vaya sacando la primera palabra ya armada
sacarprimera :: [Char] -> [Char]
sacarprimera [] = []
sacarprimera (x:xs)|x==' '= xs
                   |otherwise = sacarprimera xs
{--creo la función que me va ir creando char por char los elementos de la nueva lista con palabras, (parece rara pero después PALABRAS es
la que se encarga de usar inifinout y sacarblancosrepetidos --}
armadorpalabras :: [Char] -> [[Char]]
armadorpalabras [] = []
armadorpalabras (x:xs) = primerapalabra (x:xs) : armadorpalabras (sacarprimera (x:xs))

palabras :: [Char] -> [[Char]]
palabras (x:xs) = armadorpalabras (espacioinifinout (sacarblancosrepetidos (x:xs)))
--luego intentar usando ++ ya que me va uniendo listas

--ejercicio 4.3 palabramaslarga :: [Char] -> [Char], que dada una lista de caracteres devuelve su palabra m´as larga.
{--uso la función que separa a las palabras y las reconoce por separado, pero ambas cosas mencionadas
deben devolverme elementos a los cual calcularle su longitud, luego una función que compare la longitud de estas
y por último palabramaslarga me devuleve a la más larga--}
--es agarrar y hacer palabramaslarga (x:y:xs) = damealmaslargo (palabras (x:y:xs)) (siendo que ya palabras labura todo el proceso de espacios blancos)

palabramaslarga :: [Char] -> [Char] 
palabramaslarga (x:y:xs) = damealmaslargo (palabras (x:y:xs)) 
--para usar longitud deberia definirlo para Char y no t maybe, mas comodo
--(busque un paralelismo del uso de la función máximo para listar de Int y la de longitud)
damealmaslargo :: [[Char]] -> [Char]  --esta me va a devolver de una lista de palabras, el elemento más largo, debo comparar cada elemento=palabra entre sí
damealmaslargo [x] = x 
damealmaslargo (x:y:xs)|longitud x >= longitud y = damealmaslargo (x:xs)
                       |otherwise = damealmaslargo (y:xs)
--tratar de hacerlo sin abusar de la función PALABRAS

--ejercicio 4.4 aplanar!!! aplanar :: [[Char]] -> [Char], que a partir de una lista de palabras arma una lista de caracteres concatenandolas.
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs 

--ejercicio 4.5 aplanarconblancos, me concatena pero con espacios para poder formar palabras con espacios!!
{--aplanarConBlancos :: [[Char]] -> [Char], que a partir de una lista de palabras, arma una lista de caracteres
concaten´andolas e insertando un blanco entre cada palabra--}
aplanarconblancos :: [[Char]] -> [Char]
aplanarconblancos [] = []
aplanarconblancos [x] = x
aplanarconblancos (x:xs) = (head (x:xs) ++ [' ']) ++ aplanarconblancos xs 
--faltaban parentesis que pelotudo xd

--ejercicio 4.6 
{--aplanarConNBlancos :: [[Char]] -> Integer -> [Char], que a partir de una lista de palabras y un entero n,
arma una lista de caracteres concatenandolas e insertando n blancos entre cada palabra (n debe ser no negativo)--}

aplanarconNblancos :: [[Char]] -> Integer -> [Char]
























