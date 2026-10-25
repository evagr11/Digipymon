<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0%3A0A0E27%2C50%3A00D4AA%2C100%3A7B2FF7&height=200&section=header&text=Digipymon&fontSize=70&fontColor=fff&fontAlignY=38&desc=Juego+RPG+de+captura+y+combate+por+consola+en+Python&descAlignY=62&descSize=18" width="100%"/>
</div>

<div align="center">
  <a href="https://github.com/evagr11/Digipymon" target="_blank"><img src="https://img.shields.io/badge/Ver_Código-0A0E27?style=for-the-badge&logo=github&logoColor=white" alt="Ver Código"></a>
  <a href="#-cómo-utilizar-el-proyecto"><img src="https://img.shields.io/badge/Cómo_Jugar-00D4AA?style=for-the-badge&logo=python&logoColor=white" alt="Cómo Jugar"></a>
</div>

<div align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&size=18&duration=3500&pause=800&color=00D4AA&center=true&vCenter=true&width=600&lines=Captura+Digipymons+aleatorios%3BEnfr%C3%A9ntate+a+entrenadores+rivales%3BCompra+objetos+en+la+Digishop%3BSube+de+nivel+y+evoluciona%3B100%25+Python%2C+sin+librer%C3%ADas+externas" alt="Typing SVG" /></a>
</div>

# 🚀 Sobre el Proyecto

**Digipymon** es un **videojuego RPG por consola** hecho en Python e inspirado en Digimon. Empiezas con un compañero aleatorio y unas digipyballs; a partir de ahí buscas criaturas para capturarlas, te enfrentas a entrenadores rivales para ganar digicoins y los gastas en la tienda para curar, potenciar y hacer evolucionar a tu equipo.

Todo está hecho con **Python puro** (solo `random` y `time` de la librería estándar) y programación orientada a objetos. Los textos aparecen letra a letra, como en los RPG clásicos.

✨ **Características principales:**

*   🎲 **Captura con probabilidad:** Cada Digipymon salvaje se genera al azar (vida, ataque, nivel, tipo y nombre) y su probabilidad de captura baja con el nivel: `100 - nivel × 10`.
*   ⚔️ **Combates contra entrenadores:** El rival tiene tantos Digipymons como tú y se enfrentan uno contra uno por orden. Cada combate muestra el desglose del ataque paso a paso.
*   🔥 **Ventaja de tipos:** Fuego > Planta > Agua > Fuego. El que tiene ventaja suma un **30 %** de su ataque base.
*   ⬆️ **Niveles y evolución:** El nivel da un bonus de ataque y, al llegar a **nivel 5**, el Digipymon **evoluciona**: pasa a llamarse *Mega…* y gana +15 de vida y +5 de ataque.
*   🛒 **Digishop:** Digipyballs, pociones, anabolizantes y el objeto **Subir Nivel**, pagados con digicoins.
*   🎒 **Inventario:** Gestionado con un diccionario; los objetos desaparecen al llegar a 0.
*   📖 **Narrativa:** Introducción con un primer compañero y un viejo profesor que te da tus primeras digipyballs.

### 🖥️ Así se ve un combate

```text
──────────────────────────────────────────────────
  COMBATE 1
Tentomon [fuego]  VS  Betamon [planta]
──────────────────────────────────────────────────
 ESTADÍSTICAS BASE:
   Tentomon: Ataque base = 10 | Nivel = 3 | Vida = 13
   Betamon: Ataque base = 10 | Nivel = 1 | Vida = 17
 BONUS DE NIVEL
   Tentomon: 10 + 0.3 = 10.3
   Betamon: 10 + 0.1 = 10.1
 ¡VENTAJA DE TIPO! fuego es fuerte contra planta
   Tentomon: 10.3 + 3.0 (30% de ataque base) = 13.3
   Betamon: Sin ventaja = 10.1
──────────────────────────────────────────────────
 RESUMEN FINAL:
   Tentomon: ATAQUE TOTAL = 13.3
   Betamon: ATAQUE TOTAL = 10.1
──────────────────────────────────────────────────
¡Has ganado el combate! Tentomon ha recibido 10 de daño.

¡Has ganado la batalla! Ganas 1 digicoins. Tienes 11 digicoins.
```

# 🧠 Contexto del Proyecto

Este proyecto fue la **práctica final de la asignatura de Programación** del primer curso de **Desarrollo de Aplicaciones Multiplataforma (DAM)** en **New Digital Talent (Granada)**.

Partía de un enunciado que definía las clases, sus métodos y el funcionamiento básico del juego. Sobre esa base añadí la narrativa y tres mejoras propias: el **bonus por nivel**, la **evolución** y la **ventaja de tipos**, que en el código aparecen marcadas como `MEJORA 1`, `MEJORA 2` y `MEJORA 3`.

# 🛠️ Stack Tecnológico

<div align="center">
  <img src="https://img.shields.io/badge/Python_3-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/POO-00D4AA?style=for-the-badge&logo=python&logoColor=white" alt="POO">
  <img src="https://img.shields.io/badge/Terminal-0A0E27?style=for-the-badge&logo=windowsterminal&logoColor=white" alt="Terminal">
  <img src="https://img.shields.io/badge/Status-Terminado-7B2FF7?style=for-the-badge" alt="Status Terminado">
</div>

<br>

<div align="center">

| Área | Tecnología |
| :--- | :--------- |
| **Lenguaje** | `Python 3` |
| **Paradigma** | Programación orientada a objetos (5 clases) |
| **Librería estándar** | `random` (generación aleatoria), `time` (efecto de escritura) |
| **Estructuras de datos** | Listas (equipo) y diccionarios (inventario, tabla de tipos) |
| **Interfaz** | Consola |

</div>

# 🧩 Arquitectura

<div align="center">

| Archivo | Responsabilidad |
| :------ | :-------------- |
| `Main.py` | Bucle principal, menú, búsqueda, combate, tienda y uso de objetos |
| `Digipymon.py` | La criatura: atributos, ataque efectivo por nivel, ventaja de tipo y evolución |
| `Jugador.py` | El entrenador: su equipo (máximo 6) y sus digicoins (empieza con 10) |
| `Enemigo.py` | El entrenador rival y su equipo |
| `Inventario.py` | Diccionario de objetos con sus cantidades |
| `ListaNombres.py` | Nombres aleatorios para Digipymons y entrenadores |

</div>

# 🎮 Funcionalidades

### 🔍 Buscar Digipymon
- Genera un Digipymon con **vida** 10-20, **ataque** 1-10, **nivel** 1-3 y **tipo** fuego, agua o planta.
- Muestra la probabilidad de captura y te deja decidir si lanzar una digipyball o huir.
- Hace falta tener digipyballs y hueco en el equipo (máx. 6). Se gasta la digipyball aciertes o falles.

### ⚔️ Luchar contra un entrenador
- Si huyes, pierdes 1 digicoin.
- Cada combate compara el **ataque total** (base + bonus de nivel + ventaja de tipo).
- El ganador sigue en pie, pero recibe daño; si un Digipymon llega a 0 de vida pierde automáticamente sus siguientes combates.
- Ganas tantos digicoins como victorias y pierdes tantos como derrotas, sin bajar nunca de 0.

### 🛒 Digishop

<div align="center">

| Objeto | Precio | Efecto |
| :----- | :----: | :----- |
| Digipyball | 5 💰 | Permite intentar una captura |
| Poción | 3 💰 | +10 de vida |
| Anabolizantes | 4 💰 | +5 de ataque |
| Subir Nivel | 6 💰 | +1 nivel; a nivel 5, evoluciona |

</div>

### 🎒 Inventario y equipo
- **Usar objetos:** eliges objeto y Digipymon; al subir de nivel te dice cuántos niveles faltan para evolucionar.
- **Consultar inventario** y **consultar Digipymons** con todas sus estadísticas.

# 📂 Estructura del Proyecto

```bash
Digipymon/
├── Main.py           # Punto de entrada y bucle principal
├── Digipymon.py      # Clase Digipymon
├── Jugador.py        # Clase Jugador
├── Enemigo.py        # Clase Enemigo
├── Inventario.py     # Clase Inventario
├── ListaNombres.py   # Clase ListaNombres
├── .gitignore
└── README.md
```

# 🚀 Cómo Utilizar el Proyecto

Solo necesitas **Python 3** instalado; no hay dependencias que instalar.

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/evagr11/Digipymon.git
    ```
2.  **Navega a la carpeta del proyecto:**
    ```bash
    cd Digipymon
    ```
3.  **Ejecuta el juego:**
    ```bash
    # Windows
    python Main.py

    # macOS / Linux
    python3 Main.py
    ```

# 📚 Lo que aprendí con este proyecto

- Diseñar un programa con **varias clases** repartidas en módulos y hacer que colaboren.
- Usar **listas** y **diccionarios** para guardar el estado del juego.
- Generar contenido **aleatorio** con `random` y trabajar con probabilidades.
- Construir una **lógica de combate** paso a paso y mostrarla de forma clara al jugador.
- **Ampliar un enunciado** con mejoras propias sin romper lo que ya funcionaba.

# 🎯 Mejoras futuras

- 🗺️ **Zonas de exploración** con Digipymons y entrenadores de más nivel.
- 🍀 **Objeto "Suerte"** que aumente temporalmente la probabilidad de captura.
- 💾 **Guardar partida** en un fichero para continuar más tarde.
- 🛡️ **Validar mejor las entradas** del usuario (por ejemplo, si escribe letras donde se espera un número).
- 🖥️ **Interfaz gráfica** con `tkinter` u otra librería.

<br>

<div align="center">
  <p>Creado por <strong>Eva Gallardo</strong></p>
  <a href="https://github.com/evagr11" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <a href="https://www.linkedin.com/in/eva-gallardo-romero-830362349/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0%3A0A0E27%2C50%3A00D4AA%2C100%3A7B2FF7&height=120&section=footer" width="100%"/>
</div>
