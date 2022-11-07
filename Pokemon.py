import requests


url = "https://pokeapi.co/api/v2/"
r =  requests.get(url)
dato = r.json()

generacion=dato["pokemon-shape"] #Esta es la url de la generacion de pokemones .
url_generacion = requests.get(generacion)
objeto_generacion_json=url_generacion.json()
#print(objeto_generacion_json)
#print(objeto_generacion_json)
#Primero objeo_generacion_json["results"]["name"] ---->Estos son los nombre de los tipos de los pokemones.
r=0
lista_pokemones =[]
for i in objeto_generacion_json["results"]:#En al primera iteracion solo tendre el url de uno con su respectivo generacion
    nombre_tipo=i["name"]
    #print(i["url"]) #El hecho que lo pueda buscar es por que este me duevuelve en cada linea un dicc donde puedo acceder a una clave mediante su nombre .
    obj_gene = i["url"]  #Esto es para obtener los datos de cada generacion
    urlm=requests.get(obj_gene)
    obj_json_gene=urlm.json()
    r +=1
    #print(f"Los pokemos de forma {nombre_tipo} de la {r} generación")
    
    for k in obj_json_gene["pokemon_species"]: #Por ende cuando termine toda la itearcion de la primera generacion volvera arriba con la segunda url e iteracion
        #print(k["name"],"\n")
        lista_pokemones.append([r,nombre_tipo,k["name"]]) #Con esto me guardara en una lista asi = [[generacion,nombretipoForma,pokemon][.....]]





#La lista de pokemones podria decirse que la tengo algo a medias ordenadas
#print(lista_pokemones)
#Ahora crear una funcion que me permita ordenar eso en tal manera que que en cada sublista tenga solo [id_generacion,Tipoforma,Pokemon]
lista_nueva_1_generacion=[]
lista_nueva_2_generacion =[]
lista_nueva_3_generacion=[]
lista_nueva_4_generacion=[]
lista_nueva_5_generacion=[]
lista_nueva_6_generacion=[]
lista_nueva_7_generacion=[]
lista_nueva_8_generacion=[]
lista_nueva_9_generacion=[]
lista_nueva_10_generacion=[]
lista_nueva_11_generacion=[]
lista_nueva_12_generacion=[]
lista_nueva_10_generacion=[]
lista_nueva_11_generacion=[]
lista_nueva_12_generacion=[]
lista_nueva_13_generacion=[]
lista_nueva_14_generacion=[]
for o in lista_pokemones :
    if 1 in o:
        lista_nueva_1_generacion.append(o)
    elif 2 in o :
        lista_nueva_2_generacion.append(o)
    elif 3 in o :
        lista_nueva_3_generacion.append(o)
    elif 4 in o :
        lista_nueva_4_generacion.append(o)
    elif 5 in o :
        lista_nueva_5_generacion.append(o)
    elif 6 in o :
        lista_nueva_6_generacion.append(o)
    elif 7 in o :
        lista_nueva_7_generacion.append(o)
    elif 8 in o :
        lista_nueva_8_generacion.append(o)
    elif 9 in o :
        lista_nueva_9_generacion.append(o)
    elif 10 in o :
        lista_nueva_10_generacion.append(o)
    elif 11 in o :
        lista_nueva_11_generacion.append(o)
    elif 12 in o :
        lista_nueva_12_generacion.append(o)
    elif 13 in o :
        lista_nueva_13_generacion.append(o)
    elif 14 in o :
        lista_nueva_14_generacion.append(o)
    else :
        pass
    
#Con estos ya tengo en cada lista personalizada mis pokemones con sus respectivos formastipo y generacion

#///////////////////////Esta es para ala opcion1
def ImprimirPoke_Opcion1(nrespuesta): #LA Funcion se encarga de imprimir la lista de pokemon correspondiente a ala generacion que pida el usuario.
    if nrespuesta.isdigit() :
        if nrespuesta == "1" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_1_generacion:
                print(f"------> {k[2]}")
        elif nrespuesta == "2":
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_2_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "3" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_3_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "4" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_4_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "5" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_5_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "6" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_6_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "7" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_7_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "8" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_8_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "9" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_9_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "10" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_10_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "11" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_11_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "12" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_12_generacion :
                print(f"------> {k[2]}")
        elif nrespuesta == "13" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_13_generacion :
                print(f"------> {k[2]}") 
        elif nrespuesta == "14" :
           print(f"Los pokemones de esta generacion {nrespuesta} :\n")
           for k in lista_nueva_14_generacion :
                print(f"------> {k[2]}") 
        else :
            pass
    else :
        print("La respuesta o valor ingresado no es el correcto.")   





#/////////////////Esta es para la opcion2
#La funcion debe imprimir los pokemones por su tipo .

def ImprimirPorTipo_Opcion2(ncadena):
    if ncadena.isdigit() == False :
        if ncadena.lower() == "ball" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_1_generacion:
                print(f"-------> {p[2]}")
        elif ncadena.lower() == "squiggle" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_2_generacion:
                print(f"-------> {p[2]}")
        elif ncadena.lower() == "fish" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_3_generacion:
                print(f"-------> {p[2]}")
        elif ncadena.lower() == "arms" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_4_generacion:
                print(f"-------> {p[2]}")
        elif ncadena.lower() == "blob" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_5_generacion:
                print(f"-------> {p[2]}")
        elif ncadena.lower() == "upright" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_6_generacion:
                print(f"-------> {p[2]}")
        elif ncadena.lower() == "legs" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_7_generacion:
                print(f"-------> {p[2]}")
        elif ncadena.lower() == "quadruped" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_8_generacion:
                print(f"-------> {p[2]}")
        elif ncadena.lower() == "wings" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_9_generacion:
                print(f"-------> {p[2]}")
        elif ncadena.lower() == "tentacles" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_10_generacion:
                print(f"-------> {p[2]}")

        elif ncadena.lower() == "heads" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_11_generacion:
                print(f"-------> {p[2]}")
        
        elif ncadena.lower() == "humanoid" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_12_generacion:
                print(f"-------> {p[2]}")
        
        elif ncadena.lower() == "bug-wings" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_13_generacion:
                print(f"-------> {p[2]}")
        
        elif ncadena.lower() == "armor" :
            print("Los pokemones de la forma {ncadena}")
            for p in lista_nueva_14_generacion:
                print(f"-------> {p[2]}")
        
        else :
            pass

    else :
        print("Has ingresado un valor erróneo.")










#ImprimirPorTipo_Opcion2("ball")












nn=input("Ingrese el valor de prueba 1 :")
ImprimirPoke_Opcion1(nn)
