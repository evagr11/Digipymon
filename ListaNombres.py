import random
class ListaNombres:
    #Constructor por defecto. Tiene un atributo llamado
    #“lista_nombres_digipymons” el cual se inicializa con una lista con al
    #menos 20 nombres que decidas poner. También otro atributo llamado
    #“lista_nombres_entrenadores” inicializado a una lista con otros 20
    #nombres que te inventes.
    def __init__(self):
        self.lista_nombres_digipymons = [
            "Betamon", "Dorimon", "Gaomon", "Gomamon", "Gotsumon", 
            "Guilmon", "Greymon", "Tokomon", "Salomon", "Lopmon", 
            "Tanemon", "Tentomon", "Wormmon", "Terriermon", "Poyomon", 
            "Palmon", "Monmon", "Numemon", "Nyaromon", "Pupumon"
        ]
        self.lista_nombres_entrenadores = [
            "Tai Kamiya", "Sora Takenouchi", "Edwin Matsumara", "Izzy Izumi", 
            "Kari Kamiya", "Matt Ishida", "Mimi Tachecagua", "Joe Kido", 
            "T.K. Ishida", "Yolei Inoue", "Ken Ichijouji", "Davis Motomiya", 
            "Cody Hida", "Yamato Ishida", "Rika Nonaka", "Renamon", 
            "Jeri Katou", "Kazu Shioda", "Miyako Inoue", "Arata Santana"
        ]

    #Método “obtener_nombre_digipymon”. Obtienes un nombre aleatorio
    #de la lista de nombres de digipymons, devuelves con un return dicho
    #nombre. Consultar anexo
    def obtener_nombre_digipymon(self):
        return random.choice(self.lista_nombres_digipymons)
    
    #Método “obtener_nombre_entrenador”. Exactamente igual que el
    #método anterior pero con la lista de nombres de entrenadores.
    #Consultar anexo
    def obtener_nombre_entrenador(self):
        return random.choice(self.lista_nombres_entrenadores)