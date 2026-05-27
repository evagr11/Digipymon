import random
import time
from Jugador import Jugador
from Enemigo import Enemigo
from Inventario import Inventario
from Digipymon import Digipymon
from ListaNombres import ListaNombres

lista_nombres = ListaNombres()

# Función para imprimir texto letra a letra
def escribir(texto, velocidad=0.03):
    for letra in texto:
        print(letra, end='', flush=True)
        time.sleep(velocidad)
    print()

# Función para imprimir un separador decorativo
def separador():
    escribir("─" * 50, velocidad=0.01)

#Para generar un digipymon aleatorio, debes generar de forma aleatoria
#todos sus atributos antes de crear el objeto de tipo Digipymon.
#Consultar anexo
#a. La vida es entre 10 y 20
#b. El ataque entre 1 y 10
#c. El nivel entre 1 y 3
#d. El tipo entre "fuego, agua y planta"
#e. Un nombre aleatorio llamando al método "obtener_nombre_digipymon()" de la clase ListaNombres
def generar_digipymon_aleatorio():
    vida = random.randint(10, 20)
    ataque = random.randint(1, 10)
    nivel = random.randint(1, 3)
    tipo = random.choice(["fuego", "agua", "planta"])
    nombre = lista_nombres.obtener_nombre_digipymon()

    #Una vez tengas todos los valores, crea un objeto de la clase Digipymon
    #pasando por parámetro al constructor los valores y le haces un return
    #al objeto
    return Digipymon(nombre, vida, ataque, tipo, nivel)

#Imprime un menú que contenga:
#1. Buscar Digipymon
#2. Luchar contra un entrenador
#3. Ir a la tienda
#4. Usar objetos
#5. Consultar inventario
#6. Consultar digipymons
#7. Salir
#Pregunta al usuario por la opción que prefiere y haz un return de dicha opción.
def menu():
    separador()
    escribir("          MENÚ PRINCIPAL:")
    separador()
    print("1. Buscar Digipymon")
    print("2. Luchar contra un entrenador")
    print("3. Ir a la tienda")
    print("4. Usar objetos")
    print("5. Consultar inventario")
    print("6. Consultar digipymons")
    print("7. Salir")
    separador()

    opcion = input("Elige  una opción: ")
    return opcion

#Esta función recibe por parámetro el jugador y el inventario
def buscar_digipymon(jugador, inventario):
    separador()
    escribir("  *** BÚSQUEDA DE DIGIPYMON ***")
    separador()
    #Genera un digipymon aleatorio e imprímelo
    digipymon = generar_digipymon_aleatorio()
    escribir(f"¡Has encontrado un Digipymon! {digipymon}")

    #La probabilidad de captura del digipymon debe ser 100-(nivel del
    #digipymon * 10). Muestra al usuario la probabilidad de captura
    probabilidad_captura = 100 - (digipymon.nivel * 10)
    escribir(f"La probabilidad de captura es: {probabilidad_captura}%")

    #Puedes elegir si capturar al digipymon o no. Para capturar un
    #digipymon, debes comprobar que tienes digipyballs y que tienes
    #espacio (la máxima cantidad de digipymon que puedes tener es 6). Si
    #cumples los requisitos entonces se procede a la captura (teniendo en
    #cuenta el % de probabilidad). Tanto si aciertas como si fallas pierdes 1
    #digipyball.
    if inventario.objetos.get("digipyball", 0) <= 0:
        escribir("No tienes digipyballs para capturar al Digipymon.")
        return

    if jugador.cantidad_digipymon >= 6:
        escribir("No puedes capturar más Digipymons. Tu equipo está lleno.")
        return

    opcion = input("¿Quieres intentar capturar al Digipymon? (s/n): ").lower()
    if opcion == 's':
        escribir("Lanzando digipyball...", velocidad=0.05)
        time.sleep(0.5)
        inventario.usar_objeto("digipyball")
        if random.randint(1, 100) <= probabilidad_captura:
            jugador.añadir_digipymon(digipymon)
            escribir(f"¡Has capturado a {digipymon.nombre}!")
        else:
            escribir(f"¡Fallaste al capturar a {digipymon.nombre}!")
    #Si no quieres capturarlo, entonces indica que has huido.
    else:
        escribir("Has huido del Digipymon.")

#Nota:
#● Si la vida de tu digipymon cae a 0 en un combate, indícalo. Si entras en
#combate con tu digipymon con 0 de vida, pierdes el combate aunque
#tu digipymon tenga más ataque. Si la vida del digipymon cae por
#debajo de 0 en un combate entonces debes poner dicha vida a 0.
#● Al perder digicoins por las derrotas, tus digicoins nunca deben bajar de 0.

#Recibe por parámetro un jugador
def combate(jugador):
    separador()
    escribir("  *** COMBATE ***")
    separador()
    if jugador.cantidad_digipymon == 0:
        escribir("   No tienes Digipymons para combatir.")
        return
    #Genera un enemigo con un nombre aleatorio de la ListaNombres()
    enemigo_nombre = lista_nombres.obtener_nombre_entrenador()
    enemigo = Enemigo(enemigo_nombre)

    #Añade al enemigo tantos digipymons como tú tengas
    for digipymon in jugador.lista_digipymon:
        enemigo.añadir_digipymon(generar_digipymon_aleatorio())

    escribir(f"¡Te has encontrado con el entrenador {enemigo.nombre}!")
    time.sleep(0.3)

    #Permite al usuario decidir si quiere combatir o no. Si decide huir
    #entonces le quitas 1 digicoin.
    opcion = input("¿Quieres combatir contra el entrenador? (s/n): ").lower()
    if opcion != 's':
        jugador.digicoins = max(0, jugador.digicoins - 1)
        escribir(f"  Has huido... pierdes 1 digicoin. Tienes {jugador.digicoins} digicoins.")
        return

    victorias = 0
    derrotas = 0

    #El combate consiste en que tus digipymon y los del enemigo se
    #enfrentan. El primer digipymon de tu lista se enfrenta al primero
    #del enemigo y así sucesivamente.
    for i in range(min(jugador.cantidad_digipymon, enemigo.cantidad_digipymon)):
        jugador_digipymon = jugador.lista_digipymon[i]
        enemigo_digipymon = enemigo.lista_digipymon[i]

        # MEJORA 1: Calcular ataque efectivo con bonus de nivel para ambos
        # ataque_jugador = jugador_digipymon.ataque_efectivo()
        # ataque_enemigo = enemigo_digipymon.ataque_efectivo()

        separador()
        escribir(f"  COMBATE {i + 1} ")
        escribir(f"{jugador_digipymon.nombre} [{jugador_digipymon.tipo}]  VS  {enemigo_digipymon.nombre} [{enemigo_digipymon.tipo}]")
        separador()

        # Estadisticas base antes de aplicar mejoras
        escribir(f" ESTADÍSTICAS BASE:")
        escribir(f"   {jugador_digipymon.nombre}: Ataque base = {jugador_digipymon.ataque} | Nivel = {jugador_digipymon.nivel}")
        escribir(f"   {enemigo_digipymon.nombre}: Ataque base = {enemigo_digipymon.ataque} | Nivel = {enemigo_digipymon.nivel}")
        time.sleep(0.3)

        # MEJORA 1: Calcular ataque efectivo con bonus de nivel para ambos
        ataque_jugador_nivel = jugador_digipymon.ataque_efectivo()
        ataque_enemigo_nivel = enemigo_digipymon.ataque_efectivo()
        bonus_nivel_jugador = jugador_digipymon.nivel * 0.10
        bonus_nivel_enemigo = enemigo_digipymon.nivel * 0.10

        # MEJORA 1: Mostrar mensaje de bonus por nivel
        escribir(f" BONUS DE NIVEL (+{jugador_digipymon.nivel * 10}%):")
        escribir(f"   {jugador_digipymon.nombre}: {jugador_digipymon.ataque} + {bonus_nivel_jugador:.1f} = {ataque_jugador_nivel:.1f}")
        escribir(f"   {enemigo_digipymon.nombre}: {enemigo_digipymon.ataque} + {bonus_nivel_enemigo:.1f} = {ataque_enemigo_nivel:.1f}")
        time.sleep(0.3)

        # MEJORA 3: Calcular ataque con ventaja de tipo 
        ataque_jugador, tipo_jugador, bonus_tipo_jugador = jugador_digipymon.ataque_con_tipo(enemigo_digipymon)
        ataque_enemigo, tipo_enemigo, bonus_tipo_enemigo = enemigo_digipymon.ataque_con_tipo(jugador_digipymon)

        # MEJORA 3: Mostrar mensaje de ventaja/desventaja de tipo
        if tipo_jugador == "ventaja":
            escribir(f" ¡VENTAJA DE TIPO! {jugador_digipymon.tipo} es fuerte contra {enemigo_digipymon.tipo}")
            escribir(f"   {jugador_digipymon.nombre}: {ataque_jugador_nivel:.1f} + {bonus_tipo_jugador:.1f} (30% de ataque base) = {ataque_jugador:.1f}")
            escribir(f"   {enemigo_digipymon.nombre}: Sin ventaja = {ataque_enemigo:.1f}")
        elif tipo_enemigo == "ventaja":
            escribir(f" ¡VENTAJA DE TIPO PARA EL ENEMIGO! {enemigo_digipymon.tipo} es fuerte contra {jugador_digipymon.tipo}")
            escribir(f"   {jugador_digipymon.nombre}: Sin ventaja = {ataque_jugador:.1f}")
            escribir(f"   {enemigo_digipymon.nombre}: {ataque_enemigo_nivel:.1f} + {bonus_tipo_enemigo:.1f} (30% de ataque base) = {ataque_enemigo:.1f}")
        else:
            escribir(f"  Sin ventaja de tipo entre {jugador_digipymon.tipo} y {enemigo_digipymon.tipo}")
            escribir(f"   {jugador_digipymon.nombre}: {ataque_jugador:.1f}")
            escribir(f"   {enemigo_digipymon.nombre}: {ataque_enemigo:.1f}")

        time.sleep(0.3)

        # Resumen final de ataques antes de resultados del combate
        separador()
        escribir(f" RESUMEN FINAL:")
        escribir(f"   {jugador_digipymon.nombre}: ATAQUE TOTAL = {ataque_jugador:.1f}")
        escribir(f"   {enemigo_digipymon.nombre}: ATAQUE TOTAL = {ataque_enemigo:.1f}")
        separador()
        time.sleep(0.5)

        
        #Si la vida de tu digipymon cae a 0 en un combate, indícalo. Si entras en
        #combate con tu digipymon con 0 de vida, pierdes el combate aunque
        #tu digipymon tenga más ataque. Si la vida del digipymon cae por
        #debajo de 0 en un combate entonces debes poner dicha vida a 0.
        if jugador_digipymon.vida <= 0:
            derrotas += 1
            escribir(f"{jugador_digipymon.nombre} está debilitado y no puede combatir. ¡Has perdido este combate!")
        
        #Se compara los ataques de ambos digipymon, si el tuyo tiene
        #más ataque ganas el combate, pero tu digipymon pierde de vida
        #el ataque del digipymon enemigo.
        # MEJORA 1: Se usa ataque_efectivo() en lugar de ataque base
        elif ataque_jugador > ataque_enemigo:
            victorias += 1
            daño_recibido = int(ataque_enemigo)  # Se usa el ataque efectivo del enemigo como daño
            jugador_digipymon.vida = max(0, jugador_digipymon.vida - daño_recibido)
            escribir(f"¡Has ganado el combate! {jugador_digipymon.nombre} ha recibido {daño_recibido} de daño.")
            if jugador_digipymon.vida == 0:
                escribir(f"{jugador_digipymon.nombre} ha sido debilitado.")
        #Si tu digipymon tiene menos ataque, pierdes el combate y tu
        #digipymon pierde de vida la diferencia de ataque entre ambos
        #digipymons.
        elif ataque_jugador < ataque_enemigo:
            derrotas += 1
            daño_recibido = int(ataque_enemigo - ataque_jugador)
            jugador_digipymon.vida = max(0, jugador_digipymon.vida - daño_recibido)
            escribir(f"¡Has perdido el combate! {jugador_digipymon.nombre} ha recibido {daño_recibido} de daño.")
            if jugador_digipymon.vida == 0:
                escribir(f"{jugador_digipymon.nombre} ha sido debilitado.")
        else:
            escribir(f"¡Empate en este combate! Ninguno recibe daño.")

        escribir(f"\n  Resultado: {victorias} victorias / {derrotas} derrotas")
        time.sleep(0.2)

    #Ganas la batalla si tienes más victorias que derrotas en los combates.
    #Si ganas la batalla, entonces la cantidad de digicoins que ganas es la
    #misma cantidad que las victorias. Si pierdes la batalla, la cantidad de
    #digicoins perdida es la misma que las derrotas. En un empate ni ganas
    #ni pierdes digicoins.
    separador()
    if victorias > derrotas:
        jugador.digicoins += victorias
        escribir(f"\n¡Has ganado la batalla! Ganas {victorias} digicoins. Tienes {jugador.digicoins} digicoins.")
    elif derrotas > victorias:
        jugador.digicoins = max(0, jugador.digicoins - derrotas)
        escribir(f"\nHas perdido la batalla... pierdes {derrotas} digicoins. Tienes {jugador.digicoins} digicoins.")
    else:
        escribir("\nLa batalla ha terminado en empate. No ganas ni pierdes digicoins.")


#Recibe por parámetro el jugador y el inventario.
def digishop(jugador, inventario):
    separador()
    escribir("  *** DIGISHOP ***")
    separador()
    #Muestra el catálogo de la tienda, se propone lo siguiente aunque cada
    #uno es libre de modificarlo añadiendo o eliminando objetos:
        #a. Digipyballs: 5 digicoins
        #b. Pocion: 3 digicoins (restaura 10p de vida)
        #c. Anabolizantes: 4 digicoins (aumenta 5p de ataque)
    escribir("\nBienvenido a la Digishop. Estos son los objetos disponibles:")
    print("1. Digipyballs: 5 digicoins")
    print("2. Pocion: 3 digicoins (restaura 10p de vida)")
    print("3. Anabolizantes: 4 digicoins (aumenta 5p de ataque)")
    # MEJORA 2: Añadir nuevo ítem para subir nivel
    print("4. Subir Nivel: 6 digicoins (sube 1 nivel al Digipymon)")
    print("5. Salir de la tienda")

    #Crea todo lo necesario para comprar ítems, comprobando que tienes
    #digicoins para ello, añadiendo el inventario y restando digicoins
    #gastados.
    while True:
        opcion = input("¿Qué objeto quieres comprar? (1-5): ")
        if opcion == '1':
            if jugador.digicoins >= 5:
                inventario.añadir_objeto("digipyball", 1)
                jugador.digicoins -= 5
                escribir(f"Has comprado una digipyball. Tienes {jugador.digicoins} digicoins.")
            else:
                escribir("No tienes suficientes digicoins para comprar una digipyball.")
        elif opcion == '2':
            if jugador.digicoins >= 3:
                inventario.añadir_objeto("pocion", 1)
                jugador.digicoins -= 3
                escribir(f"Has comprado una pocion. Tienes {jugador.digicoins} digicoins.")
            else:
                escribir("No tienes suficientes digicoins para comprar una pocion.")
        elif opcion == '3':
            if jugador.digicoins >= 4:
                inventario.añadir_objeto("anabolizantes", 1)
                jugador.digicoins -= 4
                escribir(f"Has comprado anabolizantes. Tienes {jugador.digicoins} digicoins.")
            else:
                escribir("No tienes suficientes digicoins para comprar anabolizantes.")
        elif opcion == '4':
            # MEJORA 1: Ítem para subir nivel
            if jugador.digicoins >= 6:
                inventario.añadir_objeto("subir_nivel", 1)
                jugador.digicoins -= 6
                escribir(f"Has comprado un ítem de Subir Nivel. Tienes {jugador.digicoins} digicoins.")
            else:
                escribir("No tienes suficientes digicoins para comprar un ítem de Subir Nivel.")
        elif opcion == '5':
            escribir("Saliendo de la tienda...")
            break
        else:
            escribir("Opción no válida. Por favor, elige una opción entre 1 y 5.")

#Recibe por parámetro un jugador y un inventario
def usar_item(jugador, inventario):
    separador()
    escribir("  *** USAR OBJETO ***")
    separador()
    #Muestra tu inventario y pregunta al jugador qué ítem desea usar y a
    #qué Digipymon se lo vas a usar.
    #a. Las digipyballs no puedes usarlas, las pociones aumentan la vida,
    #los anabolizantes el ataque y si tienes más ítems entonces
    #programas la funcionalidad. Recuerda reducir el ítem en 1 al
    #usarlo.
    if not inventario.objetos:
        escribir("No tienes objetos en tu inventario.")
        return

    while True:
        # Crear lista de todos los objetos del inventario para el menú numérico
        objetos_lista = []
        escribir("\nObjetos disponibles:")
        for item, cantidad in inventario.objetos.items():
            objetos_lista.append(item)
            print(f"{len(objetos_lista)}. {item.capitalize()}: {cantidad}")
        
        # Opción de salir
        print(f"{len(objetos_lista) + 1}. Salir")

        opcion_item = input("\n¿Qué objeto quieres usar? (número): ")

        if opcion_item == str(len(objetos_lista) + 1):
            escribir("Saliendo del menú de objetos...")
            break

        if opcion_item < '1' or opcion_item > str(len(objetos_lista) + 1):
            escribir("Opción no válida. Por favor, elige una opción válida.")
            continue

        item_elegido = objetos_lista[int(opcion_item) - 1]

        # Verificar si el objeto elegido es digipyball
        if item_elegido == "digipyball":
            escribir("Las digipyballs no se pueden usar directamente, ¡son para capturar Digipymons!")
            continue

        if jugador.cantidad_digipymon == 0:
            escribir("No tienes Digipymons para usar el objeto.")
            return

        escribir("\nTus Digipymons:")
        for index, digipymon in enumerate(jugador.lista_digipymon):
            print(f"{index + 1}. {digipymon}")

        digipymon_elegido = input("¿A qué Digipymon quieres usar el objeto? (número): ")

        if digipymon_elegido < '1' or digipymon_elegido > str(jugador.cantidad_digipymon):
            escribir("Número de Digipymon no válido.")
            continue

        digipymon = jugador.lista_digipymon[int(digipymon_elegido) - 1]

        if item_elegido == "pocion":
            digipymon.vida += 10
            escribir(f"Has usado una pocion en {digipymon.nombre}. Su vida ahora es {digipymon.vida}.")
        elif item_elegido == "anabolizantes":
            digipymon.ataque += 5
            escribir(f"Has usado anabolizantes en {digipymon.nombre}. Su ataque ahora es {digipymon.ataque}.")
        elif item_elegido == "subir_nivel":
            # MEJORA 1: Funcionalidad para subir nivel
            digipymon.nivel += 1
            escribir(f"¡{digipymon.nombre} ha subido de nivel! Ahora es nivel {digipymon.nivel}.")
            # MEJORA 2: Verificar si evoluciona (nivel 5)
            if digipymon.nivel >= 5:
                separador()
                escribir(" ¡¡¡EVOLUCIÓN!!! ", velocidad=0.05)
                time.sleep(0.5)
                nombre_anterior = digipymon.evolucionar()
                escribir(f"¡{nombre_anterior} ha evolucionado a {digipymon.nombre}!")
                escribir(f"Vida aumentada en 15 puntos. Vida actual: {digipymon.vida}")
                escribir(f"Ataque base aumentado en 5 puntos. Ataque actual: {digipymon.ataque}")
                escribir(f"¡{digipymon.nombre} es ahora mucho más poderoso!")
                separador()
            else:
                ataque_bonus = digipymon.ataque_efectivo()
                escribir(f"Su ataque efectivo ahora es {ataque_bonus:.1f} (bonus del nivel aplicado).")
                
                # MEJORA 2: Mostrar progreso hacia evolución
                niveles_restantes = 5 - digipymon.nivel
                if niveles_restantes > 0:
                    escribir(f"Faltan {niveles_restantes} niveles para evolucionar.")

        inventario.usar_objeto(item_elegido)

#Muestra una introducción del videojuego y pregunta por el nombre del
#jugador. Crea entonces un objeto de la clase Jugador.
def main():
    separador()
    escribir("       *** BIENVENIDO A DIGIPYMON ***", velocidad=0.05)
    separador()
    escribir("¡Bienvenido a Digipymon!")
    escribir("En un mundo digital lleno de criaturas misteriosas, tu aventura está a punto de comenzar...")
    time.sleep(0.3)
    nombre_jugador = input("¿Cuál es tu nombre, entrenador? ")
    jugador = Jugador(nombre_jugador)
    inventario = Inventario()
 
    time.sleep(0.3)
    escribir(f"\nEn el camino hacia tu primera aventura, {nombre_jugador}, un Digipymon salvaje apareció ante ti...")
    time.sleep(0.5)
    digipymon_inicial = generar_digipymon_aleatorio()
    escribir(f"¡Era {digipymon_inicial.nombre}! Decidiste hacerlo tu compañero.")
    jugador.añadir_digipymon(digipymon_inicial)
    escribir(f"{digipymon_inicial.nombre} se ha unido a tu equipo.")
 
    time.sleep(0.3)
    escribir(f"\nUn viejo profesor de digipymons te detiene en el camino...")
    time.sleep(0.3)
    escribir("'Joven entrenador, toma estas digipyballs y esta poción. ¡Las necesitarás!'")
    inventario.añadir_objeto("digipyball", 3)
    inventario.añadir_objeto("pocion", 1)
    escribir("Has recibido 3 digipyballs y 1 poción.")
 
    while True:
        opcion = menu()
        if opcion == '1':
            buscar_digipymon(jugador, inventario)
        elif opcion == '2':
            combate(jugador)
        elif opcion == '3':
            digishop(jugador, inventario)
        elif opcion == '4':
            usar_item(jugador, inventario)
        elif opcion == '5':
            separador()
            escribir("\nInventario:")
            for item, cantidad in inventario.objetos.items():
                escribir(f"{item}: {cantidad}")
        elif opcion == '6':
            separador()
            jugador.consultar_digipymon()
        elif opcion == '7':
            separador()
            escribir("¡Gracias por jugar a Digipymon! ¡Hasta la próxima!", velocidad=0.05)
            separador()
            break
        else:
            escribir("Opción no válida. Por favor, elige una opción entre 1 y 7.")
 
if __name__ == "__main__":
    main()