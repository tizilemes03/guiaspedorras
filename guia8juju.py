#la guia 8 en casa, importando hechos de la clase
"""Ejercicio 1"""
#1-3. Una funcion cantidad apariciones(in nombre archivo : str, in palabra : str) → int que 
#devuelve la cantidad de apariciones de una palabra en un archivo de texto
def cantidad_apariciones(nombre_archivo:str,palabra:str)->int:
    archivo= open(nombre_archivo,"r")
    contenido= archivo.readlines()

    apariciones:int=0
    
    for i in range(len(contenido)):
        linea=contenido[i].split() #forma mas práctica y no tan laburosa como habia pensado esto, split() me forma una lista con palabras de cada linea
    
        for j in range(len(linea)):
            print(linea[j])
            if palabra == linea [j]:
                apariciones += 1
    
    archivo.close()
    return apariciones

def perteneceAr(palabra:str,lista:[str])->bool:
    resu = False
    for i in range(len(lista)):
        resu = resu or palabra==lista[i]
     
    return resu

###EJERCICIOS 1.2, 1.3, Y 2 HECHOS EN CLASE ABAJO

"""Ejercicio 3"""

def archivo_con_reverso(nombre_archivo:str):
    archivo=open(nombre_archivo,"r")
    contenido= archivo.readlines()
    contenidoReverso = []

    for l in range(len(contenido)-1,-1,-1):
        print(contenido[l])
        contenidoReverso.append(contenido[l])

    
    newArchivo = open("clipeteGob","w")
    newArchivo.writelines(contenidoReverso)

    newArchivo.close()
    archivo.close()

###FORMA DE HACERLO CON REVERSED[::-1]

"""Ejercicio 4"""
#agregar frase al final de un archivo sin hacer copia del archivo

def agregarFrase(nombre_archivo:str,frase:str):
    archivo = open(nombre_archivo,"a") #primero usando el append a ver que onda!!
    archivo.write(" "+frase) #la mierda esta es alt 92!!!!
    archivo.close()

#ENTONCES EL PRIMERO AGREGA CON UN ESPACIO UNA FRASE A LA ULTIMA LINEA    

def agregarFrase2(nombre_archivo:str,frase:str):
    archivo = open(nombre_archivo,"a")
    
    archivo.writelines("\n"+frase)

    archivo.close()

#Y ESTE HACE SALTO DE LINEA!
#agregarFrase('pepinaldo2.txt',"hello guys") #este hace el salto sin usar el /n (si en la funcion pongo una frase por defecto y no la dejo como variable al usuario)
#agregarFrase2('pepino.txt',"pepinaldo") #y este creo que si le meto un espacio vacio ya me separa la frase (si en la funcion pongo una frase por defecto y no la dejo como variable al usuario!!!!!)

"""#archivo = open(nombre_archivo)
    pepinon = archivo.read()
    print (pepinon)""" #esto me devuelve en la terminal el contenido del archivo como cadena de caracteres

"""Ejercicio 5"""
def agregarFrasePrincipio(nombre_archivo:str,frase:str):
    archivo = open(nombre_archivo,"r")
    contenido = archivo.readlines()
    archivo.close()
    newContenido = []
    newContenido.append(frase+"\n") #DE ESTA FORMA SI PERRO
    for i in range(len(contenido)):
        newContenido.append(contenido[i])
    
    archivoA = open(nombre_archivo,"w")
    for linea in newContenido:
        archivoA.write(linea)

    #archivoW = open(nombre_archivo,"w")
    #archivoW.write(frase)
    #archivoW.close()

    #archivoA = open(nombre_archivo,"a")
    #archivoA.writelines(newContenido)
    #archivoA.close()

agregarFrasePrincipio('pepino.txt',"clipete")

"""Ejercicio 6""" #HACER


"""Ejercicio 7"""
"""Implementar una funcion que lea un archivo de texto separado por comas (comma-separated values, o .csv) que
contiene las notas de toda la carrera de un grupo de alumnos y calcule el promedio final de un alumno dado. La funcion
promedioEstudiante(in lu : str) → float. El archivo tiene el siguiente formato: 
nro de LU ( str ) , materia ( str ) , fecha ( str ) , nota ( float )
"""
#def promedioEstudiante(lu:str)->float:
#   archivoLu:open(lu,"r")
    

"""Ejercicio 8"""
"""PILAS"""
from queue import LifoQueue as Pila
import random as ran

def nros_al_azar(n:int,desde:int,hasta:int)->Pila:
    pilita=Pila()
    for i in range (0,n):
        numerosDePila = ran.randint(desde,hasta)
        #print(numerosDePila)
        pilita.put(numerosDePila) #es una funcion que le agrega a pilita un numero generado
        #cabezaDePilita= pilita.get() #esto lo quita lo agregado
        #print(cabezaDePilita) 
                            

#(nros_al_azar(5,2,75))


"""Ejercicio 9"""
def cantidad_elementos(pilita:Pila)->int:
    res = 0
    newPila = Pila()

    while not pilita.empty():
        pilin = pilita.get()
        newPila.put(pilin)
        res = res + 1
    
    while not newPila.empty():
        tilin = newPila.get()
        pilita.put(tilin)
    
    print(res)

pilita = Pila()
pilita.put(6)
pilita.put(2)
pilita.put(4)
#cantidad_elementos(pilita)

"""Ejercicio 10"""
def buscar_el_maximo(p:Pila)->int:
    newPila = Pila()
    newPepina = Pila()
    res = None
    lista_maximo = []

    while not p.empty():
        pig=p.get()
        lista_maximo.append(pig)
    
    res= max(lista_maximo)

    for i in range(len(lista_maximo)):
        newPila.put(lista_maximo[i])
    
    while not newPila.empty():
        smallz= newPila.get()
        newPepina.put(smallz) #aca recupere la pila del orto

    return res

pilaPiggy = Pila()
pilaPiggy.put(2007)
pilaPiggy.put(23)
pilaPiggy.put(213124)

#print(buscar_el_maximo(pilaPiggy))
    
"""Ejercicio 11"""
def esta_bien_balanceada(s:str)->bool:
    resu=True
    pilu=Pila()
    for i in range(len(s)):
        #print(s[i])
        pilu.put(s[i])

    listaDeOrden=[]
    while not pilu.empty():
        cerdo=pilu.get()
        listaDeOrden.append(cerdo)
    
    print(listaDeOrden)
    ultimo=(len(listaDeOrden)-1)
    #print(listaDeOrden[0])
    #print(listaDeOrden[ultimo])

    if (listaDeOrden[0]=='(') or (listaDeOrden[ultimo]== ')'):
        resu=False
    
    if contadorDeParentesis1(listaDeOrden) != contadorDeParentesis2(listaDeOrden):
        resu=False 
    
    print(s)
    print(resu)
    return resu    

#def ListaDeParentesis(s:[str]):
#    listaNew=[]
#    for i in range(len(s)):
#        if s[i]=='(' or ')':
#            listaNew.append(s[i])
#    
#    for n in range(listaNew):
#        for m in range(m+1,len(listaNew)):
#            if listaNew[m] == '(' and lista

def contadorDeParentesis1(s:[str]):
    cuenta = 0
    for i in range(len(s)):
        if s[i]=='(':
            cuenta = cuenta + 1
    return cuenta

def contadorDeParentesis2(s:[str]):
    cuenta = 0
    for i in range(len(s)):
        if s[i]==')':
            cuenta = cuenta + 1
    return cuenta

#esta_bien_balanceada("10*(8+(9-(9*3)))")
#esta_bien_balanceada("(5 + 4) * (5*(6+8))")
#esta_bien_balanceada("9)*(2+7)")
#print(contadorDeParentesis1("10*(8+(9-(9*3)))"))
#print(contadorDeParentesis2("10*(8+(9-(9*3)))"))
"""ME FALTA VER EL CASO EN EL QUE SERA POR EJEMPLO 9+)(*8"""
"""Ejercicio 12"""
#Hacer



"""COLAS"""
"""Ejercicio 13"""

from queue import Queue as cola
import random as cocote
def armado_de_cola(n,desde,hasta)->cola:
    sonic= cola()
    for i in range(0,n):
        numerosNuevos= cocote.randint(desde,hasta)
        print(numerosNuevos)
        sonic.put(numerosNuevos)
    
    listaComprobacion=[]
    while not sonic.empty():
        elem = sonic.get()
        listaComprobacion.append(elem)
    
    tails=cola()
    for i in range(len(listaComprobacion)):
        tails.put(listaComprobacion[i])
    
    lista2=[]
    while not tails.empty():
        elemt = tails.get()
        lista2.append(elemt)
    
    print(listaComprobacion)
    print(lista2)
    return cola

#armado_de_cola(4,6,8) #test, las listas son las mismas!!!!

"""Ejercicio 14"""
def cantidad_elementosCola(c:cola)->int:
    pepinon=cola()
    res=0
    while not c.empty():
        fuera=c.get()
        pepinon.put(fuera)
        res += 1
    
    while not pepinon.empty():
        out=pepinon.get()
        c.put(out)
    
    return res

#TESTEO
#c=cola()
#c.put(1)
#c.put(3)
#c.put(12345)
#print(cantidad_elementosCola(c))

"""Ejercicio 15"""

def buscar_el_maximo_cola(c:cola)->int:
    elementos= chauCola(c) #funcion que arma lista con elementos de cola para luego recorrerla
    for n in elementos: #si usara len estaria recorriendo los indices
        esMayor =True
        for m in elementos:
            if n<m:
                esMayor = False
        
        if esMayor == True:
            res = n

    print(res)    
    return(res)

def chauCola(c:cola)->list:
    listaUsar=[]
    while not c.empty():
        elem=c.get()
        listaUsar.append(elem)
    
    for i in listaUsar:
        c.put(i)
    
    return(listaUsar)

#mas simple de respetar la especificacion "in"

"""Ejercicio 16"""
#carton de bingo contiene 12 numeros al azar del [0,99]
"""1. implementar una funcion armar secuencia de bingo() → Cola[int] que genere una cola con los numeros del 0 al 99
ordenados al azar.
2. implementar una funcion jugar carton de bingo(in carton : list[int], in bolillero : cola[int]) → int que toma un
carton de Bingo y una cola de enteros (que corresponden a las bolillas numeradas) y determina cual es la cantidad de
jugadas de ese bolillero que se necesitan para ganar."""

"1."
def secuencia_de_bingo()->cola(int):
    sequence=cola()

    for i in range(0,100):
        numero_secuencia = cocote.randint(0,99)
        #print(numero_secuencia)
        sequence.put(numero_secuencia)
    
    return sequence

#secuencia_de_bingo()  

"2."
def jugar_carton_de_bingo(carton:[int],bolillero:cola(int))->int:
    fichas_bingo=12 #cantidad de numeros del carton
    numero_jugadas=0

    while fichas_bingo != 0:
        bola = bolillero.get()
        print(bola)
        numero_jugadas += 1
        #for i in carton:
        #    if bola in carton:
        #        fichas_bingo= fichas_bingo -1 #esto creo que me entra en un bucle que lo termina al re toque equisde
        if bola in carton:
            fichas_bingo= fichas_bingo -1
        

    print("Y hasta aca cerramos")
    print(numero_jugadas)
    return(numero_jugadas)
#ARREGLAR ESTE PUNTO DESPUÉS

def carton()->[int]:
    cartoncinho=[]
    for i in range(0,12):
        num=cocote.randint(0,99)
        cartoncinho.append(num)

    return cartoncinho

#pañuñu = carton()
#bolillerop = secuencia_de_bingo()
#jugar_carton_de_bingo(pañuñu,bolillerop)

"""Ejercicio 17"""
"""Vamos a modelar una guardia de un hospital usando una cola donde se van almacenando los pedidos de atencion
para los pacientes que van llegando. A cada paciente se le asigna una prioridad del 1 al 10 (donde la prioridad 1 es la mas urgente
y requiere atencion inmediata) junto con su nombre y la especialidad medica que le corresponde.
Implementar la funcion n pacientes urgentes(in c : Cola[(int, str, str)]) → int que devuelve la cantidad de pacientes de
la cola que tienen prioridad en el rango [1, 3]"""

#PRUEBO CON 10 PACIENTES PERO DEBERIA CON N, MEDIO UN DOLOR DE HUEVOS XD
def diez_pacientes_urgentes(c:cola)->int:
    URGENTES=[1,2,3]
    numero_urgentes=0
    listaPacientes=[]
    while not c.empty():
        pacientes=c.get()
        listaPacientes.append(pacientes)

    #AHORA A VER CUANTAS URGENCIAS HAY
    for i in range(len(listaPacientes)):
        if listaPacientes[i][0] in URGENTES:
            numero_urgentes +=1
    
    print (listaPacientes)
    print (numero_urgentes)
    return numero_urgentes


def armado_de_cola_pacientes()->cola:
    COLAPACIENTES= cola()
    
    tripla:(int,str,str)=(0,"","")
    nombres=["Juan","Benja","Jime","Agos","Kiara","Pepe","August","Luli","Loulou","Martu","Ju"]
    especialidades = ["Ofta","Dent","Hepa","Cardio","Ano","Uro","Traumato","Alerg"]
    
    listaDeTriplas = []
    
    for i in range(0,10):
        numerosNuevos= cocote.randint(1,10)
        tripla=(numerosNuevos,nombres[i],cocote.choice(especialidades))
        listaDeTriplas.append(tripla)
    
    for i in range(len(listaDeTriplas)):
        COLAPACIENTES.put(listaDeTriplas[i])
    
    return COLAPACIENTES

#testeo1 = armado_de_cola_pacientes()
#diez_pacientes_urgentes(testeo1)        

"""Ejercicio 18"""
"""La gerencia de un banco nos pide modelar la atencion de los clientes usando una cola donde se van registrando
los pedidos de atencion. Cada vez que ingresa una persona a la entidad, debe completar sus datos en una pantalla que esta a la
entrada: Nombre y Apellido, DNI, tipo de cuenta (si es preferencial o no) y si tiene prioridad por ser adulto +65, embarazada o
con movilidad reducida (prioridad si o no).
La atencion a los clientes se da por el siguiente orden: primero las personas que tienen prioridad, luego las que tienen cuenta
bancaria preferencial y por ultimo el resto. Dentro de cada subgrupo de clientes, se respeta el orden de llegada.
2. Implementar en Python la funcion a clientes(in c : Cola[(str, int, bool, bool)]) → Cola[(str, int, bool, bool)] que dada la cola de ingreso de clientes al banco devuelve la cola en la que van a ser atendidos.
""" #Y ESPECIFICAR EL PROBLEMA
"""DICCIONARIOS"""


"""Ejercicio 19"""
"""Leer un archivo de texto y agrupar la cantidad de palabras de acuerdo a su longitud. Implementar la funcion
agrupar por longitud(in nombre archivo : str) → dict que devuelve un diccionario {longitud en letras : cantidad de palabras}"""

def agrupar_por_longitud(nombre_archivo:str)->dict:
    archivo = open(nombre_archivo,"r")
    contenido = archivo.readlines()
    listaContenido = []
    dictionary : dict = {}
    for e in range(len(contenido)):
        palabras = contenido[e].split()
        #print(contenido[e].split())
        listaContenido.append(palabras)
    
    #print(listaContenido)
    #RECORRE LA LISTA DE LISTAS DE PALABRAS, CREANDO KEYS Y VALORES SEGUN LA CONDICION!
    for i in range (len(listaContenido)):
        for j in range(len(listaContenido[i])):
            clave = len((listaContenido)[i][j])
            if clave in dictionary:
                dictionary[clave] + 1
            else:
                dictionary[clave] = 1
    
    archivo.close()
    return dictionary

#print(agrupar_por_longitud('pepino.txt'))

"""Ejercicio 20"""

"""Ejercicio 21"""
def la_palabra_más_frecuente(nombre_archivo:str)->str:
    archivo = open(nombre_archivo,"r")
    contenido = archivo.readlines()
    d={}
    listaNew =[]
    listaDeMierda=[]
    cantidades=[]

    for linea in contenido:
        palabras= linea.split()
        if palabras != []:
            listaNew.append(palabras)
    
    for i in listaNew:
        for j in i:
            palabrita = j
            listaDeMierda.append(j)
    
    #print(listaDeMierda)
    for l in listaDeMierda:
        if l in d:
            d[l]+= 1
        else:
            d[l] = 1
    
    for j in d:
        cantidades.append(d[j])
    
    #print(cantidades)
    #print (max(cantidades))
    resultado = " "
    for maxfrecuente in d:
        if d[maxfrecuente] == max(cantidades):
            resultado = maxfrecuente
        
    print (resultado)
    archivo.close()
    return resultado
           
la_palabra_más_frecuente('pepino.txt')

"""Ejercicio 22"""
"""Nos piden desarrollar un navegador web muy simple que debe llevar un registro de los sitios web visitados por los
usuarios del sistema. El navegador debe permitir al usuario navegar hacia atras y hacia adelante en la historia de navegacion."""
historiales:dict={}


#!!!/%$($) Hechos el lunes 23 TRABAJO DE 4 HORAS EN CLASE!!!/%$($) -ARDUO Y SIMETRICO-
"""Ejercicio 1"""
def contar_lineas(nombre_archivo:str)-> int:
    archivo= open(nombre_archivo,"r")
    contenido = archivo.readlines()
    numlineas= 0
    
    for e in range(len(contenido)):
        numlineas += 1
    
    return numlineas
 

#2 existe palabra
def existe_palabra(palabra:str,nombre_archivo:str)-> bool:
    archivo= open(nombre_archivo,"r")
    contenido= archivo.readlines()
    resu = False
    for e in range(len(contenido)):
        if esta_aca_palabra(contenido[e],palabra) == True:
            resu = True 
            
    
    archivo.close()

    return resu

##preguntar como cortarlo sin break -MENTIRA SE PODIA SIN BREAK-
             
def esta_aca_palabra(frase:str,palabra:str)->bool:
    palabras = frase.split()
    resu = False
    for r in range(len(palabras)):
        if palabras[r] == palabra:
            resu = True
            
    return resu 
 
"""Ejercicio 2"""

def clonar_sin_comentarios(nombre_archivo:str):
    archivo = open(nombre_archivo,"r")
    contenido = archivo.readlines()
    newContent= []
    
    for e in range(len(contenido)):
        if not (es_o_no_comentario (contenido[e]) == True):
            newContent.append(contenido[e])
    
    nuevoArchivo = open("pepinaldo2.txt","w")
    nuevoArchivo.writelines(newContent)
    
    nuevoArchivo.close()
    archivo.close()
    
#auxiliar de ver si es o no comentario
def es_o_no_comentario(linea:str)->bool: 
    resu:bool = False
    for i in range(len(linea)):
        if (linea[i] == "#"):
            resu = True
            
            break
        
        elif (linea[i]!= " "):
            resu = False

            break
                     
    return resu 


"""Bloque de codigo"""
#bloque de codigo xd
#print(contar_lineas('pepino.txt'))
#print(es_o_no_comentario(" #pepe"))
#print(es_o_no_comentario("jose#milei"))    
#clonar_sin_comentarios('pepino.txt')
#print(existe_palabra("pepino",'pepino.txt'))
#print(existe_palabra("desaprobe",'pepino.txt'))
#print(cantidad_apariciones('pepino.txt',"pepino"))
#pepe=(nros_al_azar(8,4,29))
#archivo_con_reverso('pepino.txt')