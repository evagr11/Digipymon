class Enemigo:
    """Entrenador rival con su lista de Digipymon."""
    #El constructor de esta clase recibe un nombre por parámetro. Además,
    #tiene un atributo llamado “lista_digipymon” inicializado a una lista vacía
    #y “cantidad_digipymon” inicializado a 0
    def __init__(self, nombre):
        """Crea un entrenador sin Digipymon.

        Args:
            nombre: nombre del entrenador.
        """
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

    #Método “añadir_digipymon” recibe por parámetro un digipymon.
    #Añadir a la lista dicho digipymon y aumenta la cantidad de digipymon
    #en 1
    def añadir_digipymon(self, digipymon):
        """Añade un Digipymon al equipo del entrenador.

        Args:
            digipymon: Digipymon que se añade.
        """
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1