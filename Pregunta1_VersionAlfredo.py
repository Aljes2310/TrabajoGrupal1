import os
import csv
os.system("cls")


class Libro:
    def __init__(self, id, titulo, genero, ISBN, editorial, autores):
        self.id=id
        self.titulo=titulo
        self.genero=genero
        self.ISBN=ISBN
        self.editorial=editorial
        self.autores=autores
    
    def __del__(self):
        return None

    def listar_libros(self):
        print(f"Titulo: {self.titulo}")
        print(f"Genero: {self.genero}")
        print(f"ISBN: {self.ISBN}")
        print(f"Editorial: {self.editorial}")
        print(f"Autor(es): {self.autores}")
        print("")



salida=False
while salida==False: 
    #MENU A INTERACTURAR EN EL PROMPT
    print("\nBienvenido al Menu Interactivo, eliga las siguientes opciones segun lo que desee realizar: ")
    print("")
    print("Opción 1: Leer archivo de disco duro (.txt o csv) que cargue 3 libros.")
    print("Opción 2: Listar libros.")
    print("Opción 3: Agregar libro.")
    print("Opción 4: Eliminar libro.")
    print("Opción 5: Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado.")
    print("Opción 6: Ordenar libros por título.")
    print("Opción 7: Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.")
    print("Opción 8: Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.")
    print("Opción 9: Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).")
    print("Opción 10: Guardar libros en archivo de disco duro (.txt o csv).")

    numero=int(input("\nColoca el numero de la opcion: "))

    if numero==1:
        lista_libros=input("\nInsertar nombre archivo de libros a leer (colocar tambien extension .txt o csv.): ")
        print("")

        with open(lista_libros) as f:    #leyendo el archivos con datos de libros
            reader = csv.reader(f)
            headers = next(reader)
            lines = list(reader) 

        data = dict(zip(headers, zip(*lines)))

        id=list(data["id"])
        titulo=list(data["titulo"])
        genero=list(data["genero"])
        ISBN=list(data["ISBN"])
        editorial=list(data["editorial"])
        autores=list(data["autores"])

        objetos=[]
        for i in range(0,len(id)):
            objetos.append(Libro(id[i], titulo[i], genero[i], ISBN[i], editorial[i], autores[i]))

        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True


    elif numero==2:
        listar=True
        while listar==True:
            libro_a_listar=input("Que libro te gustara listar?, Introduce su titulo: ")
            print("")

            objetos[titulo.index(libro_a_listar)].listar_libros()
        
            print("\n¿Deseas listar otro libro?")
            repetir_listado = input("\nIngresa 'si' para listar otro libro, o cualquier tecla para finalizar: ").lower()
            if repetir_listado != "si":
                listar=False

        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True

    elif numero==3:
        print("Introduce los datos del libro: ")
        titulo_agregado=input("\nIntroduce el Titulo: ")
        genero_agregado=input("Introduce el Genero: ")
        isbn_agregado=input("Introduce el ISBN: ")
        editorial_agregado=input("Introduce la Editorial: ")
        autor_agregado=input("Introduce los Autor(es), utilizar ´;´ para separar los nombres: ")

        id.append(max(id)+1)
        titulo.append(titulo_agregado)
        genero.append(genero_agregado)
        ISBN.append(isbn_agregado)
        editorial.append(editorial_agregado)
        autores.append(autor_agregado)

        objetos=[]
        for i in range(0,len(id)):
            objetos.append(Libro(id[i], titulo[i], genero[i], ISBN[i], editorial[i], autores[i]))

        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True
    
    elif numero==4:
        eliminado=input("Introduce el nombre del libro a eliminar: ")

        objetos[titulo.index(eliminado)].__del__()
        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True
    
    elif numero==5:
        opcion_cinco=True
        while opcion_cinco==True:
            opcion5=input("\nBuscar segun ISBN o Titulo, coloca ´ISBN´ o ´Titulo´ segun la opcion que prefieras: ").capitalize()
            if opcion5=="ISBN":
                isbn_a_buscar=input("Ingresa el ISBN: ")
                objetos[ISBN.index(isbn_a_buscar)].listar_libros()
                opcion_cinco=False
            elif opcion5=="Titulo":
                titulo_a_buscar=input("Ingresa el Titulo: ")
                objetos[titulo.index(titulo_a_buscar)].listar_libros() 
                opcion_cinco=False
            else:
                print("\nColoque una opcion valida")    

        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True


    elif numero==6:
        print("\nTitulos ordenados segun orden alfabetico: ")
        for i in sorted(titulo):
            print(f"- {i}")  

        respuesta=input("\nDesea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True

    elif numero==7:
        opcion_siete=True
        while opcion_siete==True:
            opcion7=input("\nBuscar segun Autor, Editorial, Genero , coloca ´Autor´, ´Genero´ o ´Editorial´ segun la opcion que prefieras: ").capitalize()
            if opcion7=="Autor":
                autores_a_buscar=input("Ingresa el Autor: ")
                objetos[autores.index(autores_a_buscar)].listar_libros()
                opcion_siete=False
            elif opcion7=="Genero":
                genero_a_buscar=input("Ingresa el Genero: ")
                objetos[genero.index(genero_a_buscar)].listar_libros() 
                opcion_siete=False
            elif opcion7=="Editorial":
                editorial_a_buscar=input("Ingresa la Editorial: ")
                objetos[editorial.index(editorial_a_buscar)].listar_libros() 
            else:
                print("\nColoque una opcion valida")    

        respuesta=input("Desea volver al Menu? . Colocar ´si´, para volver al menu de lo contrario presione cualquier tecla   : ").lower()
        if respuesta !="si":
            salida=True
    
    elif numero==8:
        numero_autores=int(input("Ingresar el numero de autores: "))

        lista_autores=[elemento_autor for elemento_autor in autores if ";" in elemento_autor and elemento_autor.count(";") == numero_autores-1] 
        for i in lista_autores:
            print(i)

                    
                
                

            

