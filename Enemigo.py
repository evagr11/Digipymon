class Enemigo:
    #El constructor de esta clase recibe un nombre por parámetro. Además,
    #tiene un atributo llamado “lista_digipymon” inicializado a una lista vacía
    #y “cantidad_digipymon” inicializado a 0
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

    #Método “añadir_digipymon” recibe por parámetro un digipymon.
    #Añadir a la lista dicho digipymon y aumenta la cantidad de digipymon
    #en 1
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1