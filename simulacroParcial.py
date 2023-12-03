#SIMULACRO DE PARCIAL
"""Ejercicio 1"""
def ultima_aparicion(s:[int],e:int)->int:
    res =0
    indices_apariciones = []
    for i in range(0,len(s),1):
        if e==s[i] and pertenece(e,s):
            indices_apariciones.append(i)
    return max(indices_apariciones)
#esta forma hace que me de una lista con las posiciones en las que aparece "e" en la lista "s", y luego me de la última posición (máxima al ser creciente) de la lista de posiciones.


def pertenece(e:int,s:[int])->bool:
    resu=False
    for i in range(len(s)):
        resu= resu or e==s[i] 
    return resu

"""Ejercicio 2"""
#elementos exclusivos
def elementos_exclusivos(s:[int],t:[int])->[int]: #diferencia simetrica
    resultado = []
    for i in range(len(s)):
        if not pertenece(s[i],t):
            resultado.append(s[i])
    
    for j in range(len(s)):
        if not pertenece(t[j],s):
            resultado.append(t[j])

    laPosta=chauRepes(resultado)

    return laPosta

def chauRepes(list:[int])->[int]:
    listaNew=[]
    for i in range(len(list)):
        if not (list[i] in listaNew):
            listaNew.append(list[i])
            
    
    return listaNew
     
"""Ejercicio 3"""
def contar_traducciones_iguales(ing:dict,ale:dict)->int:
    listIng=[]
    listAle=[]
    for i in ing:
        listIng.append((i,ing[i]))
    for a in ale:
        listAle.append((a,ale[a]))
    
    resultado = compara_listas(listIng,listAle)
    return resultado

def compara_listas(list:[str],list2:[list])->int:
    res=0
    for e in list:
        if e in list2:           #O USAR EL IN PELOTUDO, (actualizacion): fue usado equisde
            res += 1
    return res

#def perteneceSTR(string:str,lista:[str])->bool:
#    resu=False
#    for i in range(len(lista)):
#        resu= resu or string==lista[i] 
#    return resu                                #RESULTO INNECESARIO              

#def iteradorDiccionario():
#    d:dict={"a":"1","b":"2"}
#    for i in d:
#        print (i)

#iteradorDiccionario()

"""Ejercicio 4"""
def convertir_a_diccionario(s:[int])->dict:
    dNumeros:dict={}
    for numero in s:
        if numero in dNumeros:
            dNumeros[numero] += 1
        else:
            dNumeros[numero] = 1
    
    return dNumeros


"""Bloque de codigo"""
#print(ultima_aparicion([1,4,5,4,5,4,6,8,4],4))   
#print(elementos_exclusivos([2,4,5,7,9,1,7,7,7],[68,25,2,8,1,9,6,6,6]))    
#print(contar_traducciones_iguales({"Mano":"Hand","Cara":"Gesicht","Pie":"Fuss","Dedo":"Finger"},{"Pie":"Foot","Dedo":"Finger","Mano":"Hand"}))
#print(convertir_a_diccionario([2,3,4,2,5,3,6,8,2]))
#print(convertir_a_diccionario([-1,0,4,100,100,-1,-2,-1]))