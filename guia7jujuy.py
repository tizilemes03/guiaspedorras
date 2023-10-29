#Ejercicios Guia 7
def pertenece(vector:[int],e:int)-> bool: 
    res= False
    
    for i in range(len(vector)):
        res = res or (e == vector[i])
    
    return res
        
def pertenece2 (vector:[],e):
    
    for i in range(len(vector)):
        if (e==vector[i]):
            return True 
    
    return False 

def divideATodos(vector:[int],e:int)-> bool: 
    res:bool = True 
    for i in range (len(vector)): 
        res= res and (vector[i]%e==0)
    return res 

def sumaTotal(s:[int])-> int:
    res:int = 0 
    for i in range (0,len(s),1):
        res = res + s[i]  
        
    return res 

def ordenados(vector:[int])-> bool:  
    for i in range (0,len(vector)-1,1):
         if (vector[i]>= vector[i+1]):
             return False
         
    return True 
 
def long_7(vector:[str])-> bool: 
    for i in range (0,len(vector),1):
        if (len(vector[i]))>7:
            return True 
    
    return False 

def es_palindromo(palabra:str)-> bool:
    for i in range (0,len(palabra),1): 
        if (palabra[(len(palabra)-1)-i]) != (palabra[i]):
            return False
        
    return True 

#7 fortaleza de la contraseña
"""Analizar la fortaleza de una contrasena. El parametro de entrada de la funcion sera un string con la contraseña a
analizar, y la salida otro string con tres posibles valores: VERDE, AMARILLA y ROJA. Nota: en python la “ñ/ Ñ”
es considerado un caracter especial y no se comporta como cualquier otra letra.
La contrasena sera VERDE si:
a) la longitud es mayor a 8 caracteres
b) tiene al menos 1 letra minuscula.
c) tiene al menos 1 letra mayuscula.
d ) tiene al menos 1 digito numerico (0..9)
La contrasena sera ROJA si:
a) la longitud es menor a 5 caracteres.
En caso contrario sera AMARILLA."""
#voy a precisar de funciones auxiliares, sobre si es minuscula, mayuscula y  digito numerico

def fortaleza_password(contra:str)-> str: 
    if len(contra)>=8 and hay_min(contra) and hay_may(contra) and hay_num(contra):
        res:str ="VERDE"
    elif len(contra)<5:
        res:str = "ROJA"
    else:
        res:str ="AMARILLA"
        
    return res

def hay_min (contra:str)->bool:
    res:bool = False
    for i in range(len(contra)):
        if (contra[i]>= 'a' and contra[i]<='z'):
            res = True 
    return res


def hay_may(contra:str)->bool:
    res:bool = False
    for i in range(len(contra)):
        if (contra[i]>= 'A' and contra[i]<='Z'):
            res = True 
    return res

    
def hay_num (contra:str)->bool:
    res:bool = False
    for i in range(len(contra)):
        if (contra[i]>='0' and contra[i]<='9'):
            res = True 
    return res

#8
"""Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual.
Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de
dinero y “R” para retiro de dinero, y ademas el monto de cada operacion. Por ejemplo, si la lista de tuplas es [(‘‘I’’,
2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces el saldo actual es 1280"""

def cuenta_bancaria(vector:[str,int])->int: #como preciso la coordenada 0 y 1 del vector uso un for que la recorra
    resu:int = 0
    for i in range (len(vector)):
        if (vector[i])[0]== "I":  #recordar que me quede como un boludo porque es una lista de tuplas, donde la i se mueve por cada elemento de tupla, no por cada coordenada dentro de cada elemento!!!
            resu = resu + (vector[i])[1]
        elif (vector[i])[0] == "R":
            resu = resu - (vector[i])[1]
    return resu 

#9 Recorrer una palabra en formato string y devolver True si esta tiene al menos 3 vocales distintas y False en caso contrario.
def tres_vocales_dif(palabra:str)->bool:
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    resu:int = 0
    resultado:bool = False 
    for i in range(len(palabra)):
        for v in range(len(vocales)):
            if (vocales[v] == palabra[i]):
                resu= resu + 1
                vocales[v] = "" #esto quita la vocal para que no busque repetidas en la lista!!!
    if (resu>=3):
        resultado:bool = True 
    return resultado 

    
"""Segunda Parte"""
#1 funcion del tipo inout, en los números pares, coloca un 0.
def chau_pares(lista:[int])-> [int]:
    for p in range (len(lista)):
        if (lista[p]%2==0):
            lista[p] = 0

#esta pasa por referencia a la lista original, es decir le cambia los valores

def chau_pares_dado(lista:[int])-> [int]:
    res:[int] = lista.copy()
    for p in range (len(lista)):
        if (lista[p]%2==0):
            res[p] = 0
    return res
    
#esta pasa por copia local, es decir me devuelve una lista con lo que me pide, pero la original la guarda intacta.
def string_sin_vocales(texto:str)->str: 
    res=""
    vocales=["a","e","i","o","u","A","E","I","O","U"]
    for l in range (len(texto)):
            if not (pertenece2(vocales,texto[l])):
                res += texto[l]
    return res 

def pertenece2 (vector:[],e):
    
    for i in range(len(vector)):
        if (e==vector[i]):
            return True 
    
    return False 
        
#4 reemplaza vocales
"""problema reemplazaVocales (in s:seq<Char>) : seq<Char> {
requiere: { T rue }
asegura: {Para todo i ∈ Z, si 0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘ ’) ∨
(¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i] ) ) }
}"""
def reemplaza_vocales(palabra:str)->str:
    res=""
    vocales = ["a","e","i","o","u"]
    for i in range(len(palabra)):
        if pertenece2(vocales,(palabra[i])):
            res += ""
        else:
            res+= palabra[i]
    print (res)
    return res

def pertenece2(vector:[str],e):
    
    for i in range(len(vector)):
        if (e==vector[i]):
            return True 
    
    return False 

#5 daVueltaStr (interpretar bien)
def daVueltaStr(s:str)->str:
    res:str = ""
    for i in range(len(s)):
        res += s[(len(s)-i)-1]

    print (res)        
    return res 

#6 eliminarRepetidos
#def eliminarRepetidos(s:str)->str:

def eliminarRepetidos(s:str)->str:
    res= ""
    for i in range(len(s)):
        repite:bool = False
        for j in range(i+1,len(s)):
            if (s[j]==s[i]):
                repite= True
        if not (repite == True):
            res += s[i]
    return res
     
"""Ejercicio 3"""
#estado de aprobacion de materia
"""problema aprobado (in notas: seq<Z>) : Z {
requiere: {|notas| > 0}
requiere: {Para todo i ∈ Z si 0 ≤ i < |notas| → 0 ≤ notas[i] ≤ 10)}
asegura: {res = 1 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7}
asegura: {res = 2 ↔ todos los elementos de notas son mayores o iguales a 4 y el promedio esta entre 4 (inclusive) y 7}
asegura: {res = 3 ↔ alguno de los elementos de notas es menor a 4 o el promedio es menor a 4}
}
"""
def aprobado(notas:[int])->int:
    if (menores_a_4(notas)) == True or (promedio(notas)<4):
        res:int =3
    if ((menores_a_4(notas))== False):
        if 4<=(promedio(notas))<7:
            res:int = 2
        elif (promedio(notas))>=7:
            res:int = 1
    
    return res

def promedio(notas:[int])->int:
    res:int =0
    for i in range(len(notas)):
        res +=notas[i]
    res = (res/len(notas))
    return res 

def menores_a_4(notas:[int])->bool:
    res:bool = False
    for i in range(len(notas)):
            res = res or (notas[i]<=3)
    
    return res

#preguntar que onda todo el planteo sin auxiliares
"""    for i in range(len(notas)):
        if (notas[i]<4) or (promedio(notas)<4):
            res:int = 3
            break
        if (notas[i]>=4) and (4<=promedio(notas)<7):
            res:int = 2 
        elif (notas[i]>=4) and (4<= promedio(notas)<=7):
            res:int = 1  
    return res """ 

"""Ejercicio 4"""
#a) estudiantes de la facu ndea
def estudiantesFCEN()->[str]:
    res:[str] = []
    estudiante:str= (input('Ingrese un alumno. Ingrese listo para terminar '))    
    while(estudiante!="listo"):
        res.append(estudiante) 
        estudiante:str= (input('Ingrese un alumno. Ingrese listo para terminar '))
   
    print(res)
    return res 

#b) funcion con input que tiene como elementos tuplas (Char x Int)
def subeConMilei()->[tuple]:
    res:[tuple]=[]
    acción:str = (input('Hola Clipete, que deseas hacer en tu sube:'))
    while (acción != "X"):
        if acción == "C" or acción == "D":
            monto:int = 0
            monto:int =(input('CUANTO METES O SACAS:'))
            res.append((acción,monto))
            acción = (input('QUE QUIERE HACER AHORA:'))
    
    print(res)
    return res

#c) juego de 7.5
"""Vamos a escribir un programa para simular el juego conocido como 7 y medio. El mismo debera generar un numero
aleatorio entre 0 y 12 (excluyendo el 8 y 9) y debera luego preguntarle al usuario si desea seguir sacando otra “carta”
o plantarse. En este ultimo caso el programa debe terminar. Los numeros aleatorios obtenidos deberan sumarse segun
el numero obtenido salvo por las “figuras” (10, 11 y 12) que sumaran medio punto cada una. El programa debe ir
acumulando los valores y si se pasa de 7.5 debe informar que el usuario ha perdido. Al finalizar la funcion devuelve
el historial de “cartas” que hizo que el usuario gane o pierda. Para generar numeros pseudo-aleatorios entre 1 y 12
utilizaremos la funcion random.randint(1,12). Al mismo tiempo, la funcion random.choice() puede ser de gran
ayuda a la hora de repartir cartas."""
import random
def juego_7ymedio()->[float]:
    tu_maso:[float] = []
    maso_usado:[float]=[1,2,3,4,5,6,7,10,11,12]
    primeraCarta:float = random.choice(maso_usado)
    print("Tu primer carta es", str(primeraCarta))
   
    tu_maso.append(primeraCarta)
    cuanto_va(tu_maso)
    print ("usted va",str(primeraCarta))
    juego:str=(input("Esto es el 7 y medio, saca una carta o se planta?"))
    while (juego!= "me planto"):
        if juego == "sigo":
            otra_carta:int = random.choice(maso_usado)
            print ("Tu carta es",str(otra_carta))
            tu_maso.append(otra_carta)
            if cuanto_va(tu_maso)> 7.5:
                print("Lo siento, perdiste, superaste 7.5, mejor suerte para la próxima")
                break
            elif cuanto_va(tu_maso)<=7.5:
                juego:str=(input("Bueno queride, sacas una carta o se planta?"))
    
    if cuanto_va(tu_maso)<7.5:
        print("te quedaste corto pa, mejor la próxima")
        print("aca esta tu maso", str(tu_maso))
    elif cuanto_va(tu_maso)== 7.5:
        print ("ganaste pa")
        print ("aca esta tu maso victorioso" , str(tu_maso))


def cuanto_va(puntos:[float])->float:
    res:float =0
    for i in range(len(puntos)):
        if puntos[i] == 10 or puntos[i]==12 or puntos[i]==11:
            res = res + 0.5
        else:
            res = res + puntos[i]
    return res
 
"""Ejercicio 5"""
# a)si el entero "e" pertenece o no devuelve en cada elemento el booleano correspondiente
def perteneceACadaUno(s:[[int]],e:int)->[bool]:
    resu:[bool] = []
    for i in range(len(s)):
        if pertenece_int_lisInt(e,s[i]) == True:
            resu.append(True)
        elif pertenece_int_lisInt(e,s[i]) == False:
            resu.append(False)
    return resu

def pertenece_int_lisInt(e:int,x:[int])->bool:
    resu:bool = False 
    for i in range(len(x)):
        resu = resu or e==x[i] 
    return resu

#b es matriz
"""2. problema esMatriz (in s:seq<seq<Z>>) : Bool {
requiere: { T rue }
asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (Para todo i ∈ Z si 0 ≤ i < |s| → |s[i]| = |s[0]|)}
}
"""
def esMatriz(s:[[int]])->bool:
    resu:bool = True 
    for i in range(len(s)):
        if len(s[0])!= len(s[i]):
            resu = False 
    
    return resu 

#c filas ordenadas
"""3. problema filasOrdenadas (in m:seq<seq<Z>>, out res: seq<Bool>) {
requiere: { esMatriz(m)}
asegura: {Para todo i ∈ Z si 0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i])) }
}"""
def filasOrdenadas(m:[[int]])->[bool]:
    resu = []
    for i in range(len(m)):
        resu.append(ordenados(m[i]))
    return resu

#d
"""4. Implementar una funci´on que tome un entero d y otro p y eleve una matriz cuadrada de tama˜no d con valores generados
al azar a la potencia p. Es decir, multiplique a la matriz generada al azar por s´ı misma p veces. Realizar experimentos
con diferentes valores de d. ¿Qu´e pasa con valores muy grandes?
Nota 1: record´a que en la multiplicaci´on de una matriz cuadrada de dimensi´on d por si misma cada posici´on se calcula
como res[i][j] = Pd−1
k=0(m[i][k] × m[k][j])
Nota 2: para generar una matriz cuadrada de dimensi´on d con valores aleatorios hay muchas opciones de implementaci´on, analizar las siguientes usando la biblioteca numpy (ver recuadro):
Opci´on 1:
import numpy as np
m = np.random.random((d, d))2
Opci´on 2:
import numpy as np
m = np.random.randint(i,f, (d, d))3"""
#def matrizcuadradaElevada()





#def estudiantesFCEN(estudiante:"str"=(input('Ingrese un alumno. Ingrese listo para terminar '))):
#    while(estudiante!="listo"):
                    
                    
    

                

#recorrido reverso de una palabra, sobre un ciclo que lo recorre directo print(palabra[(len(palabra)-1)-i])
#con while
#def pertenece3 (vector:[])
    

#ejercicios de la clase
#def sumaTotal(s:[int])-> int:
#    res: int = 0
#    for i in range(0,len(s),1):
#        res += s[i]
#    return res 


#def pertenece(vector:[int],e:int)-> bool: 
# #for i in range(len(vector)):
#    print(vector[i])

"""BLOQUE DE CÓDIGO"""
resultado = pertenece2([], 3)
print(resultado)
divideono = divideATodos([66,33,30],3)
print(divideono)
resusuma = sumaTotal ([45,5,50])
print(resusuma)
resu= ordenados([3,4,5,6,])
print(resu)
resu6= es_palindromo("aja uju aja")
print(resu6)
print (fortaleza_password("Benjamin8"))
print(fortaleza_password("Pepinaldo"))
print (fortaleza_password("To11"))
print (cuenta_bancaria ([("I",3500),("R",251),("I",712)]))
print (chau_pares_dado([2,5,4,3,4,1,8]))
print (string_sin_vocales ("CIEXNTIXFICOXS COXN WAXDOX"))
(reemplaza_vocales("cientificos con wado"))
print (string_sin_vocales("BEXNJAXMXIN XEN LXA 1402"))
daVueltaStr("clipete")
print (eliminarRepetidos("banana"))
print (eliminarRepetidos("otorrinolaringonlogia"))
print (promedio([5,7,2,3]))
print (menores_a_4([5,7,3]))
print (aprobado([5,4,3,8]))
print (aprobado([4,4,4,5,6]))
print (aprobado([9,7,5,10]))
#(estudiantesFCEN())
#(subeConMilei())
print(cuanto_va([3,5,10,5,12]))
#juego_7ymedio()
print(perteneceACadaUno([[12,4,6],[1,4,7],[1,6],[0]],4))
print(esMatriz([[2,43],[1,6],[7,4]]))
print(esMatriz([[2,4],[1,7],[7,1,3]]))
print(ordenados([2,5,7,8]))
print(filasOrdenadas([[2,5,6,1],[1,2,3,4],[0,3,2],[5,7]]))
