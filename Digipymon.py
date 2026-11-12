class Digipymon:
    """Criatura del juego con nombre, vida, ataque, tipo y nivel.

    Los tipos son fuego, agua y planta, y cada uno tiene ventaja sobre otro
    (fuego > planta > agua > fuego).
    """
    #Constructor por parámetros que recibe un nombre, vida, ataque, tipo y nivel.
    def __init__(self, nombre, vida, ataque, tipo, nivel):
        """Crea un Digipymon.

        Args:
            nombre: nombre del Digipymon.
            vida: puntos de vida.
            ataque: puntos de ataque base.
            tipo: "fuego", "agua" o "planta".
            nivel: nivel, del 1 en adelante.
        """
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel

    #Método “__str__” que imprima todos los atributos
    def __str__(self):
        """Devuelve todos los atributos en una línea, para imprimirlo."""
        return (f"Digipymon: {self.nombre} | Vida: {self.vida} | Ataque: {self.ataque}"
                f"| Tipo: {self.tipo} | Nivel: {self.nivel}")
    
    # MEJORA 1: Método para calcular el ataque efectivo con bonus de nivel
    # El ataque aumenta un (nivel * 10)% del ataque actual
    def ataque_efectivo(self):
        """Devuelve el ataque con el bonus de nivel.

        Returns:
            El ataque base más nivel * 0.10.
        """
        bonus = self.nivel * 0.10
        return self.ataque + bonus
    
    # MEJORA 2: Método para evolucionar el Digipymon
    # Si llega a nivel 5, evoluciona: cambia nombre, sube vida y ataque
    def evolucionar(self):
        """Evoluciona el Digipymon: añade "Mega" al nombre, +15 de vida y +5 de ataque.

        Returns:
            El nombre que tenía antes de evolucionar.
        """
        nombre_original = self.nombre

        # Añado prefijo "Mega" al nombre
        self.nombre = "Mega" + self.nombre

        # Subir vida en 15 puntos
        self.vida += 15

        # Subir ataque base en 5 puntos
        self.ataque += 5

        return nombre_original
    
    # MEJORA 3: Método para calcular el ataque con ventaja de tipo
    # Fuego > Planta > Agua > Fuego
    # Si tiene ventaja: +30% de daño
    def ataque_con_tipo(self, enemigo_digipymon):
        """Calcula el ataque contra otro Digipymon teniendo en cuenta el tipo.

        Si tiene ventaja de tipo, suma un 30 % del ataque base al ataque efectivo.

        Args:
            enemigo_digipymon: Digipymon al que ataca.

        Returns:
            Una tupla (ataque, "ventaja" o "normal", bonus de tipo aplicado).
        """
        ataque_con_nivel = self.ataque_efectivo()
        bonus_tipo = self.ataque * 0.30  # +30% sobre ataque BASE

        # Tabla de ventajas de tipo
        ventajas = {
            "fuego": "planta",
            "planta": "agua",
            "agua": "fuego"
        }

        # Comprobar si tiene ventaja de tipo
        if ventajas.get(self.tipo) == enemigo_digipymon.tipo:
            # Ventaja: ataque con nivel + 30% sobre ataque base
            return ataque_con_nivel + bonus_tipo, "ventaja", bonus_tipo
        else:
            return ataque_con_nivel, "normal", 0