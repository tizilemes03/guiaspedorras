pertenece :: (Eq t) => t -> [t] -> Bool
pertenece x [] = False
pertenece x (y:ys) = x==y || pertenece x ys 
-- uso el ó logico para que trabaje sobre "y" que sería el head, y luego con el resto de la lista
hayrepetidos :: (Eq t) => [t] -> Bool
hayrepetidos [] = False 
hayrepetidos [x] = False 
hayrepetidos (x:xs) = pertenece x (xs) || hayrepetidos (xs)
-- aca es lo mismo, uso el o logico para que siga viendo el pertenece recursivamente, pero si es solo una vez, es falso.
quitartodos :: (Eq t) => t -> [t] -> [t]
quitartodos x [] = []
quitartodos x [a]| x==a = []
quitartodos x (y:xs)|x==y = quitartodos x xs
                    |otherwise= (y:quitartodos x xs)
                   
eliminarrepetidos :: (Eq t) => [t] -> [t]
eliminarrepetidos [] = []
eliminarrepetidos (x:xs)= (x:eliminarrepetidos (quitartodos x xs))

aplanartuplas :: [(t,t)] -> [t]
aplanartuplas [] = []
aplanartuplas [(a,b)] = [a] ++ [b] 
aplanartuplas ((a,b):xs) = (a:b:aplanartuplas xs)

--longitud para string por ej para hacer paralelismos!!
longitud :: [Char] -> Int
longitud []=0 
longitud (xs)=1 + longitud (tail xs) 

