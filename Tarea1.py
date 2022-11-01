global lista
lista = list()
class Libro:
    def __init__(self,id,titulo,genero,isbn,editorial,autor):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autor = autor

    def ListarLibros(self):
        for a in lista:
            print (f"{a.id}, -- , {a.titulo}, -- , {a.genero}")

    def AgregarLibros(self):
        l = Libro()
        l.id = input("Ingrese el id del libro: ")
        l.titulo = input("Ingrese el titulo del libro: ")
        l.genero = input("Ingrese el genero del libro: ")
        lista.append(l)

    def menu():
        op = 0
        while op != 9:
            print("Menú Principal")
            print("***********")
            print("1. Leer archivo de disco duro")
            print("2. Listar libros: ")
            print("3. Agregar libros: ")
            print("4. Eliminar libros: ")
            print("5. Buscar libro por ISBN o por título: ")
            print("6. Ordenar libros por título.: ")
            print("7. Buscar libros por autor, editorial o género.: ")
            print("8. Buscar libros por número de autores: ")
            print("9. Para salir del programa: ")
            op = int(input("Ingrese una opción: "))

            if op == 1:
                print("")
            elif op == 2:
                ListarLibros()
            elif op == 3:
                AgregarLibros()
            elif op == 4:
                print("")
            elif op == 5:
                print("")
            elif op == 6:
                print("")
            elif op == 7:
                print("")
            elif op == 8:
                print("")
            elif op == 9:
                print("Gracias por usar el programa")
    menu()