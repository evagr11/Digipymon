class Jugador:
    """El jugador: su nombre, sus Digipymon (hasta 6) y sus digicoins."""

    #Esta clase tendrá un constructor por parámetros que admite un
    #nombre, además en dicho constructor tendremos un atributo llamado
    #“lista_digipymon” inicializado a una lista vacía, “cantidad_digipymon”
    #inicializado a 0 y “digicoins” inicializado a 10
    def __init__(self, nombre):
        """Crea un jugador sin Digipymon y con 10 digicoins.

        Args:
            nombre: nombre del jugador.
        """
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

    #Método “añadir_digipymon”, recibe un digipymon por parámetro. La
    #funcionalidad del método consiste en añadir el digipymon a la lista y
    #aumentar la cantidad de digipymon en 1
    def añadir_digipymon(self, digipymon):
        """Añade un Digipymon al equipo.

        Args:
            digipymon: Digipymon capturado.
        """
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1

    #Método “consultar_digipymon”. La funcionalidad del método consiste
    #en recorrer la lista de digipymons e imprimirla
    def consultar_digipymon(self):
        """Imprime los Digipymon del jugador, o avisa si no tiene ninguno."""
        if not self.lista_digipymon:
            print(f"No tienes ningún Digipymon {self.nombre}.")
        else:
            print(f"  Digipymons de {self.nombre}:")
            for digipymon in self.lista_digipymon:
                print(digipymon)

    #Método “consultar_digicoins”. Como su nombre indica, imprime los
    #digicoins que tienes
    def consultar_digicoins(self):
        """Imprime los digicoins del jugador."""
        print(f"{self.nombre} tiene {self.digicoins} digicoins.")