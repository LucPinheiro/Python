####################################################################
# Sistema de gestión de préstamos de biblioteca usando excepciones #
####################################################################

# Clases de excepciones personalizadas que heredan  de Exception
class LectorNoRegistrado(Exception):

    # Método constructor de la clase
    # Se añaden 2 campos: nome_lector y mensaje
    def __init__(self, nombre_lector, mensaje="Lector no registrado en la biblioteca.\n"):
        self.nombre_lector = nombre_lector
        self.mensaje = mensaje
        # Se pasa el mensaje a la excepción base.
        super().__init__(self.mensaje)

    # Método que define cómo se mostrará la excepción al imprimirla
    def __str__(self):
        return f"Lector: {self.nombre_lector}. {self.mensaje}"

class LibroNoPrestado(Exception):

    # Método constructor de la clase
    # Se añaden 2 campos: titulo y mensaje
    def __init__(self, titulo, mensaje="Ese libro no está prestado a este lector.\n"):
        self.titulo = titulo
        self.mensaje = mensaje
        # Se pasa el mensaje a la excepción base.
        super().__init__(self.mensaje)

    # Método que define cómo se mostrará la excepción al imprimirla
    def __str__(self):
        return f"Libro: {self.titulo}. {self.mensaje}"


# Diccionario que almacena los préstamos de cada lector
prestamos = {
    'Juan García': ['La Celestina', 'El lazarillo de Tormes'],
    'Ana López': ['La vida es sueño'],
    'Pedro Martínez': []
}

# Se presenta un menu con el uso del bucle while
# llamando a las clases de excepciones personalizadas,
# controlano posibles errores
while True:
    try:

        # Diccionario auxiliar que convierte los nombres de los lectores a minúsculas
        # para evitar problemas con mayúsculas y minúsculas al comparar
        lectores_lower = {lector.lower(): lector for lector in prestamos.keys()}

        print("** GESTIÓN DE PRÉSTAMOS DE BIBLIOTECA **")
        print("0 - Salir del programa")
        print("1 - Nuevo préstamo")
        print("2 - Cancelar un préstamo")
        print("3 - Listar préstamos actuales")
        print("-------------------------------------")

        # El usuario introduce una opción del menú y se convierte a número entero
        op = int(input("Opción: "))

        if op == 0:
            print("Fin de programa")
            print("Hasta luego")
            break

        elif op == 1:
            print("1 - NUEVO PRÉSTAMO")
            lector = input("Introduza el nombre del lector: ")

            # Se comprueba si el lector existe en el diccionario y luego 
            # se lanza una excepción personalizada si no existe
            if lector.lower() not in lectores_lower.keys():
                raise LectorNoRegistrado(lector)
            else:
                lector_original = lectores_lower[lector.lower()]

                titulo = input("Introduza el título del libro: ")

                # Se comprueba si el título está vacío
                if titulo.strip() == "":
                    raise ValueError("El título del libro no puede estar vacío.")

                # Se añade el libro a la lista de préstamos del lector
                prestamos[lector_original].append(titulo)

                print("-------------------------------------")
                print(f"Libro añadido correctamente a {lector_original}.\n")


        elif op == 2:
            print("2 - CANCELAR UN PRÉSTAMO")

            for lector, libros in prestamos.items():
                print(f"Lector {lector}: libros {libros}")

            lector = input("Introduza el nombre del lector a cancelar: ")

            # Se comprueba si el lector existe en el diccionario y luego
            # se lanza una excepción personalizada si no existe
            if lector.lower() not in lectores_lower.keys():
                raise LectorNoRegistrado(lector)

            lector_original = lectores_lower[lector.lower()]

            titulo = input("Introduza el título del libro: ")

            # Se comprueba si el título está vacío
            if titulo.strip() == "":
                raise ValueError("El título del libro no puede estar vacío.\n")

            # Se comprueba si el libro no está prestado al lector
            elif titulo not in prestamos[lector_original]:
                raise LibroNoPrestado(titulo)

            else:
                # Se elimina el libro de la lista de préstamos del lector
                prestamos[lector_original].remove(titulo)

                print("---------------------------------------------")
                print("Préstamo cancelado correctamente.\n")
            
        elif op == 3:
            print("LISTAJE DE PRÉSTAMOS")

            # Se usa un for para recoger la lista de lectores y sus libros
            for lector, libros in prestamos.items():
                if len(libros) == 0:
                    print(f"Lector {lector}: sin préstamo")
                else:
                    print(f"Lector {lector}: libros {libros}")
            print()
      
        else:
            raise ValueError("Opción no válida (teclee un número de 0 al 3)")

    # Captura y muestra los errores producidos
    except (ValueError, LectorNoRegistrado, LibroNoPrestado) as error:
        print(error)

