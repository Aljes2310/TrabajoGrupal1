import os
os.system("cls")
import requests


salida=False
while salida==False: 
    #MENU A INTERACTURAR EN EL PROMPT
    print("\nBienvenido al Menu Interactivo, eliga las siguientes opciones segun lo que desee realizar: ")
    print("")
    print("Opción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) y se listan todos los pokemon respectivos.")
    print("Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.")
    print("Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.")
    print("Opción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.")
    print("Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.")

    #OPCION 1 
    numero=int(input("\nColoca el numero de la opcion: "))
    if numero==1:
        print("")
        generacion=input("Ingresa el numero de generacion de pokemones que te gustaria ver: ")

        url1="https://pokeapi.co/api/v2/generation/" + str(generacion)
        r=requests.get(url1)
        data=r.json()
        print("")
        print(f"Los Pokemones correspondientes a la generacion {str(generacion)} son : ")
        print("")
        for i in range(0,len(data['pokemon_species'])):
            print("\t-",data['pokemon_species'][i]["name"].title())

        print("")    
        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True


    #OPCION 2
    if numero==2:
        url2="https://pokeapi.co/api/v2/pokemon-shape/"
        r=requests.get(url2)
        data=r.json()

        lista_formas=[]
        for i in range(0,len(data["results"])):
            lista_formas.append(data["results"][i]["name"].capitalize())

        print(f"\nLas formas de los pokemones a seleccionar son: ")
        print("")
        dic_forma={}
        for index, i in enumerate(lista_formas, start=1):
            print(f"\t-{i}")
            dic_forma[i]=index


        eleccion_forma=input("\n Elige una de las formas para ver los pokemones que pertenecen a esa forma ! : ").capitalize()

        url2_shape= url2 + str(dic_forma[eleccion_forma])

        r_forma=requests.get(url2_shape)
        data_formas=r_forma.json()

        print("")
        print(f"Los pokemones de la forma {eleccion_forma} son: ")
        print("")
        for i in range(0,len(data_formas['pokemon_species'])):
            print("\t-",data_formas['pokemon_species'][i]["name"].capitalize())

        print("")    
        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True

    if numero==3:
        
        url3="https://pokeapi.co/api/v2/ability/"
        r=requests.get(url3)
        data=r.json()
        print(data)


        lista_formas=[]
        for i in range(0,len(data["results"])):
            lista_formas.append(data["results"][i]["name"].capitalize())

        print(f"\nLas Habilidades a seleccionar son: ")
        print("")
        dic_forma={}
        for index, i in enumerate(lista_formas, start=1):
            print(f"\t- {i}")
            dic_forma[i]=index


        eleccion_habilidad=input("\n Elige una de las habilidades para ver los pokemones que tiene esta habilidad! : ").capitalize()

        url3_shape= url3 + str(dic_forma[eleccion_habilidad])

        r_forma3=requests.get(url3_shape)
        data_habilidad=r_forma3.json()

        print("")    
        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True

        print("")
        print(f"Los pokemones de habilidad {eleccion_habilidad} son: ")
        print("")
        for i in range(0,len(data_habilidad['pokemon'])):
            print("\t-",data_habilidad['pokemon'][i]["pokemon"]["name"].capitalize()) 


        print("")    
        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True


    if numero==4:
                    
        url4="https://pokeapi.co/api/v2/pokemon-habitat/"
        r=requests.get(url4)
        data=r.json()

        lista_formas=[]
        for i in range(0,len(data["results"])):
            lista_formas.append(data["results"][i]["name"].capitalize())

        print(f"\nLos Habitat a seleccionar son: ")
        print("")
        dic_forma={}
        for index, i in enumerate(lista_formas, start=1):
            print(f"\t- {i}")
            dic_forma[i]=index


        eleccion_habitat=input("\nElige una de los Habitat para ver los pokemones que pertenecen a este habitat! : ").capitalize()

        url4_shape= url4 + str(dic_forma[eleccion_habitat])

        r_forma4=requests.get(url4_shape)
        data_habitat=r_forma4.json()

        print("")
        print(f"Los pokemones del habitat {eleccion_habitat} son: ")
        print("")
        for i in range(0,len(data_habitat['pokemon_species'])):
            print("\t-",data_habitat['pokemon_species'][i]["name"].capitalize()) 


        print("")    
        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True

    if numero==5:
            
        url5="https://pokeapi.co/api/v2/type/"
        r=requests.get(url5)
        data=r.json()


        lista_formas=[]
        for i in range(0,len(data["results"])):
            lista_formas.append(data["results"][i]["name"].capitalize())

        print(f"\nLos Tipos de Pokemon son: ")
        print("")
        dic_forma={}
        for index, i in enumerate(lista_formas, start=1):
            print(f"\t- {i}")
            dic_forma[i]=index

        eleccion_tipo=input("\nElige una de los tipos para ver los pokemones que pertenecen a esta clase! : ").capitalize()

        url5_shape= url5 + str(dic_forma[eleccion_tipo])

        r_forma4=requests.get(url5_shape)
        data_tipo=r_forma4.json()

        print("")
        print(f"Los pokemones del tipo {eleccion_tipo} son: ")
        print("")

        for i in range(0,len(data_tipo['pokemon'])):
            print("\t-",data_tipo['pokemon'][i]["pokemon"]["name"].capitalize()) 

        print("")    
        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True


