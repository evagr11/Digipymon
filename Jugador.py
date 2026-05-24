class Jugador:

    #Esta clase tendrá un constructor por parámetros que admite un
    #nombre, además en dicho constructor tendremos un atributo llamado
    #“lista_digipymon” inicializado a una lista vacía, “cantidad_digipymon”
    #inicializado a 0 y “digicoins” inicializado a 10
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    #Método “añadir_digipymon”, recibe un digipymon por parámetro. La
    #funcionalidad del método consiste en añadir el digipymon a la lista y
    #aumentar la cantidad de digipymon en 1
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1

    #Método “consultar_digipymon”. La funcionalidad del método consiste
    #en recorrer la lista de digipymons e imprimirla
    def consultar_digipymon(self):
        if not self.lista_digipymon:
            print(f"No tienes ningún Digipymon {self.nombre}.")
        else:
            print(f"  Digipymons de {self.nombre}:")
            for digipymon in self.lista_digipymon:
                print(digipymon)

    #Método “consultar_digicoins”. Como su nombre indica, imprime los
    #digicoins que tienes
    def consultar_digicoins(self):
        print(f"{self.nombre} tiene {self.digicoins} digicoins.")