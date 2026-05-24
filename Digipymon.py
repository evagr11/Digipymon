class Digipymon:
    #Constructor por parámetros que recibe un nombre, vida, ataque, tipo y nivel.
    def __init__(self, nombre, vida, ataque, tipo, nivel):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel

    #Método “__str__” que imprima todos los atributos
    def __str__(self):
        return (f"Digipymon: {self.nombre} | Vida: {self.vida} | Ataque: {self.ataque}"
                f"| Tipo: {self.tipo} | Nivel: {self.nivel}")