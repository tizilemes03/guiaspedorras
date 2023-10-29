#Ejercicio 1
def holaMundo():
    print("hola mundo") 

#la funcion termina cuando la columna de tabulacion se corta.

#PrimerDiaPython (respetar los 3 bloques de -import-def_funciones-codigo_libre-)

#operacion % es n modulo m
#importante para el codigo libre guardar a la funcion en una variable, para luego imprimirla en pantalla

def imprimirVerso():
    print ("When life is like this,im thankful \nwarm sun, good vibrations")
    
def raizDe2 ():
    import math as r
    num= r.sqrt (2) 
    return ( round(num , 4)) 

def factorial_de_dos ():
    import math as m
    a= m.factorial(2)
    return a 

def perimetro ():
    import math as m
    peri =m.pi 
    return 2*peri 

#Ejercicio 2 
def imprimir_saludo(nombre:str): 
    print ("Hola" ,(nombre))

def raiz_cuadrada_de (n:int):
    import math as m
    res= m.sqrt(n)
    return res

def fahrenheit_a_celsius (temp_far:float)->float: 
    return ((temp_far)+(-32)) * 5/9
def imprimir_dos_veces (estribillo:str):
    print ( estribillo , estribillo )
    
def es_multiplo_det(n:int,m:int)->bool:
    res:bool = (n%m==0) 
    return res 

def es_par(numero:int)->bool:
    res:bool = (numero%2==0) 
    return res       

def cantidad_de_pizzas (comensales:int,min_cant_de_porciones:int)-> int:
    import math as m
    res= round ((min_cant_de_porciones * comensales) / 8) + 1
    return res
#podria usar la funcion m.ceill (que viene de libreria math) que redondea para arriba

"""Ejercicio 3"""
#alguno es 0(numero1, numero2): dados dos numeros racionales, decide si alguno de los dos es igual a 0.
def alguno_es_0(numero1:float,numero2:float)-> bool: 
    res:bool = numero1==0 or numero2==0 
    return res 

#ambos son 0(numero1, numero2): dados dos numeros racionales, decide si ambos son iguales a 0.
def ambos_son_0(numero1:int,numero2:int) -> bool:
    res:bool = (numero1 ==0 and numero2==0)
    return res

def es_nombre_largo2(nombre:str) ->bool:
    res:bool = (len(nombre)<=8) and (len(nombre)>=3)
    return res

def es_bisiesto(año:int)->bool: 
    res:bool = (año%4==0 or año%400==0) and not(año%100==0)
    return res

"""Ejercicio 4""" #del 1 al 3
#el coso de los pinos, donde hasta los 3 metros, cada centimetro vale 3kg, y pasados los 3 metros, cada centimetro se cuenta por 2kg 
""""usados para fabrica de muebles, a la que le sirven arboles de entre 400 y 1000 kilos
un pino fuera de este rango no le sirve a la fabrica."""

def peso_pino(w:int)-> int:
    if w<=300:
        peso: int = w*3
    else:
        peso: int = (w-300)*2 + 900 
    return peso 

def es_peso_util(p:int)->bool:
    res:bool = (min(p,400)==400) and (max(p,1000)==1000)
    return res 
 
def sirve_pino(h:int)->bool: 
    res:bool = max(h,133)==h and min(h,350)==h
    return res 

"""Ejercicio 5"""
#1. devolver el doble si es par(numero) que devuelve el doble del numero en caso de ser par y el mismo numero encaso contrario.

def devuelve_doble_par(n:int)->int: 
    if n%2==0:
        res:int = n*2
    else:
        res: int = n 
    return res

#2 devolver valor si es par sino el que sigue(numero). que devuelve el mismo numero si es par y sino el siguiente. Analizar distintas formas de implementacion (usando un if-then-else, y 2 if), ¿todas funcionan?
def devolver_valor_si_es_par_sino_el_que_sigue(numero:int)-> int:
    if numero%2==0: 
        res:int = numero
    else: 
        res:int = numero+1
    return res 

#3 
"""3. devolver el doble si es multiplo3 el triple si es multiplo9(numero). En otro caso devolver el numero original. 
Analizar distintas formas de implementacion (usando un if-then-else, y 2 if, usando alguna opcion de operacion
logica), ¿todas funcionan?.""" 
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero:int)->int: 
    if numero%3==0 and not numero%9==0:
        res:int = numero*2 
    elif numero%9==0:
        res:int = numero*3 
    return res 

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9_2(numero:int)->int: 
    if numero%3==0:
        if numero%9==0:
            res:int = numero*3 
        else:
            res:int = numero*2 
    else:
        res:int = numero
    return res 


"""4) lindo_nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga 
“Tu nombre tiene muchas letras!” y sino, “Tu nombre tiene menos de 5 caracteres”."""
def lindo_nombre(nombre:str)->str:
    if len(nombre)>=5:
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")
    
#5 elRango que imprime por pantalla “Menor a 5” si el numero es menor a 5, “Entre 10 y 20” si el numero esta en ese rango y “Mayor a 20” si el numero es mayor a 20.
def elRango(numero:int)->str:
    generica:str = ""
    if numero<=20:
        if numero<5:
            generica:str = "Menor a 5"
        elif numero>9:
            generica:str = "Entre 10 y 20"
    elif numero>20:
        generica:str = "Mayor a 20"
    print(generica)

#6
"""En Argentina una persona del sexo femenino se jubila a los 60 anos, mientras que aquellas del sexo masculino se jubilan
a los 65 anos. Quienes son menores de 18 anos se deben ir de vacaciones junto al grupo que se jubila. Al resto de
las personas se les ordena ir a trabajar. Implemente una funcion que, dados los parametros de sexo (F o M) y edad,
imprima la frase que corresponda segun el caso: “Anda de vacaciones” o “Te toca trabajar”."""

def peronchismo(sexo:str,edad:int)-> str: 
    if edad<18 or edad>=65:
        destino:str = "Anda a Cochabamba"
    elif edad>59 and sexo=="F":
        destino:str = "Anda a Peru"
    else: 
        destino:str = "Anda a laburar a Claypole trola"
    print(destino)

"""Ejercicio 6"""
#imprimir los numeros del 1 al 10 con while
def uno_al_diez():
    i=1
    while(i<=10):
        print (i)
        i = i + 1 #i va iterando de cierta forma, hasta dejar de ser menor igual a 10!!!

#pares entre el 10 y el 40
def pares_hasta_40():
    i=10
    while(i<=40):
        if i%2==0:
            print(i)
            i= i + 1
        else:
            i= i + 1

#eco 10 veces 
def eco_10_veces():
    i=1
    while(i<=10):
        print("eco")
        i= i + 1
    print ("BASTA CERDO")

#cuenta del cohete
def cuenta_cohete(i:int):
    i = i
    while(i>0):
        print(i)
        i = i - 1
    print ("Despegue!!!!!")

#viaje en el tiempo
def viaje_tiempo(añop:int,añol:int):
    añop = añop
    while (añop>añol):
        print ("Viajo un año al pasado, estamos en el año: " + str(añop))
        añop = añop - 1 
    print ("Llegamos al año: " + str(añol))

#viaje hasta 384.AC saltando de 20 en 20 hacia atras

"""Ejercicio 7"""
#todos los anteriores usando for




#hechos de la clase 
def es_multiplo_de (n:int,m:int)->bool:
    res:bool = (n/m == int(n/m))
    return res 

def es_multiplo_De (n:int,m:int)->bool:
    res:bool = n%m ==0
    return res
def es_nombre_largo (nombre:str)-> bool: 
    res:bool = (len (nombre) >= 3) and (len (nombre) <=8) 
    return res 

def pares_entre_10_y_40_mal ():
    for i in range(10,41,2):
        print (i) #esto va de 2 en 2 sea par o no
        
def pares_entre_10_y_40 (inicio:int):
    for i in range (inicio,41,1):
        if i%2==0:
            print(i)
        

            
#quiero saber si es que arranco con par o impar, igualmente 
    
#el boton play me guarda automaticamente el procedimiento

    
# testeo bloq de codigo
holaMundo()
print (es_multiplo_De (10,5))
imprimirVerso() 
test1 = es_multiplo_de (3,5)
print("Resultado de es_multiplo_de(3,5) ",test1)
print( round(4.578245353 ,4) )
print (raizDe2 ())
print (factorial_de_dos())
print (perimetro())
imprimir_saludo('pepe') 
print (raiz_cuadrada_de (4))
print (fahrenheit_a_celsius (89))
imprimir_dos_veces ('juju')
print (es_multiplo_det (4,2))
print (es_multiplo_det (5,3))
print (es_par (3))
print (cantidad_de_pizzas (8,5))
(pares_entre_10_y_40 (3))
print (alguno_es_0(4.5,0))
print (alguno_es_0(4,2.8))
print (ambos_son_0(8.2,0))
print (ambos_son_0(0,0))
print (es_nombre_largo2("pepinaldo"))
print (es_nombre_largo2("benjamin"))
print (es_bisiesto(1988))
print (es_bisiesto(400))
print (min(8,9))
print (max(1,6))
print (peso_pino(20))
print (peso_pino(360))
print (es_peso_util(450))
print (es_peso_util(20))
print (es_peso_util(1060))
print (sirve_pino(134))
print (sirve_pino(25))
print (sirve_pino(360))
lindo_nombre("pepinaldo")
lindo_nombre("tizi")
elRango(2)
elRango(11)
elRango(30) 
peronchismo("M",47)
peronchismo("F",62)
peronchismo("M",17)
peronchismo("F",79)
print ("conteo del 1 al 10")
uno_al_diez()
print("conteo pares del 10 al 40")
pares_hasta_40()
eco_10_veces()
cuenta_cohete(5)
viaje_tiempo(23,15)