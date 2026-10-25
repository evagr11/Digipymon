<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0A0E27,50:00D4AA,100:7B2FF7&height=200&section=header&text=Digipymon&fontSize=70&fontColor=FFF&animation=fadeIn&fontAlignY=30&desc=Juego%20RPG%20de%20captura%20y%20combate%20en%20Python&descAlignY=55&descSize=18" width="100%"/>
</div>

<div align="center">
  <a href="https://github.com/evagr11/Digipymon" target="_blank">
    <img src="https://img.shields.io/badge/Ver_Código-0A0E27?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  <a href="#" target="_blank">
    <img src="https://img.shields.io/badge/Python_3-00D4AA?style=for-the-badge&logo=python&logoColor=white"/>
  </a>
</div>

<br>

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=00D4AA&center=true&vCenter=true&width=600&lines=Captura+Digipymons+aleatorios;Enfrentate+a+entrenadores+rivales;Compra+ítems+en+la+Digishop;Sistema+de+combate+por+turnos;100%25+Python+Vanilla"/>
</div>


# 🎮 Sobre el Proyecto

**Digipymon** es un **videojuego RPG por consola** desarrollado en Python como práctica final del módulo de **Programación** del primer curso de **DAM** (Desarrollo de Aplicaciones Multiplataforma) en **NDT NewDigitalTalent · Granada**.

El objetivo era construir un **juego completo de captura y combate** inspirado en la franquicia Digimon, utilizando únicamente **Python puro** sin frameworks externos.

✨ Características principales:

- Sistema de **captura** de criaturas con probabilidad variable
- **Combate por turnos** contra entrenadores rivales
- **Tienda** para comprar objetos (Digipyballs, Pociones, Anabolizantes)
- **Inventario** persistente en memoria con diccionarios
- Sistema de **digicoins** como moneda del juego
- Generación **aleatoria** de Digipymons con atributos variados
- Máximo de **6 Digipymons** por equipo


# 🧠 Contexto del Proyecto

Este proyecto surge como parte de la **práctica final de Programación** del segundo curso de **DAM**.

El objetivo era desarrollar un **videojuego completo en Python** que incluyera:

- Programación orientada a objetos (POO)
- Manejo de estructuras de datos (listas, diccionarios)
- Generación de números aleatorios
- Lógica de combate por turnos
- Gestión de inventario y economía in-game

El proyecto se desarrolló siguiendo un **enunciado detallado** que especificaba las clases, métodos y funcionalidades requeridas, permitiendo libertad creativa en la narrativa y mejoras adicionales.


# 🖼️ Diseño del Juego

El diseño del juego se planificó siguiendo la estructura propuesta en el enunciado:

- 📋 **Especificaciones técnicas** definidas en el documento de la práctica
- 🎨 **Narrativa** personalizada con historia introductoria
- 💻 **Implementación** en Python puro

> El objetivo fue mantener la funcionalidad completa mientras se añadía una capa de inmersión narrativa.


# 🛠️ Tecnologías

<p align="center">
  <img src="https://img.shields.io/badge/Python-0A0E27?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/POO-00D4AA?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Random-7B2FF7?style=for-the-badge&logo=dice&logoColor=white"/>
  <img src="https://img.shields.io/badge/Terminal-0A0E27?style=for-the-badge&logo=windowsterminal&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-00D4AA?style=for-the-badge&logo=github&logoColor=white"/>
</p>


# 🧩 Arquitectura del Proyecto

```bash
digipymon/
│
├── Main.py              # Punto de entrada y bucle principal del juego
├── Digipymon.py         # Clase Digipymon (criaturas capturables)
├── Jugador.py           # Clase Jugador (entrenador principal)
├── Enemigo.py           # Clase Enemigo (rivales de combate)
├── Inventario.py        # Clase Inventario (gestión de objetos)
├── ListaNombres.py      # Clase ListaNombres (generador de nombres aleatorios)
│
└── Enunciado Digipymon.pdf  # Documento funcional del proyecto
```

# 🎮 Funcionalidades

### 🔍 Buscar Digipymon
- Genera un Digipymon aleatorio con atributos variados
- Muestra la **probabilidad de captura** (100 - nivel × 10)
- Requiere **Digipyballs** y espacio en el equipo (máx. 6)
- Sistema de éxito/fracaso basado en porcentaje aleatorio

### ⚔️ Luchar contra entrenador
- Genera un enemigo con nombre aleatorio
- El enemigo tiene la **misma cantidad** de Digipymons que tú
- Combate **1 vs 1** secuencial por posición en el equipo
- Comparación de **ataque** para determinar ganador
- Sistema de **daño** y **debilitamiento** (vida a 0)
- Recompensas/penalizaciones en **digicoins**

### 🛒 Digishop (Tienda)
- Catálogo de objetos comprables:
  - **Digipyballs**: 5 digicoins
  - **Poción**: 3 digicoins (restaura 10p de vida)
  - **Anabolizantes**: 4 digicoins (aumenta 5p de ataque)
- Verificación de **digicoins** suficientes
- Añadido automático al **inventario**

### 🎒 Usar objetos
- Visualización del inventario actual
- Selección de **ítem** y **Digipymon objetivo**
- Efectos diferenciados por tipo de objeto
- Eliminación automática al agotarse (cantidad 0)

### 📦 Consultar inventario
- Listado de todos los objetos con sus cantidades

### 👾 Consultar Digipymons
- Visualización del equipo completo
- Estado de vida, ataque, tipo y nivel de cada criatura


# 🚀 Cómo jugar

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/digipymon.git

# Navegar al directorio
cd digipymon

# Ejecutar el juego
python Main.py
```

# 📚 Lo que aprendí con este proyecto

- **Programación Orientada a Objetos** en Python
- Gestión de **estado** en aplicaciones interactivas
- Uso de la librería **random** para generación procedural
- Manipulación de **listas** y **diccionarios** como estructuras de datos
- Lógica de **combate por turnos** y sistemas de economía
- Organización de código en **múltiples archivos** y **módulos**


# 🎯 Posibles mejoras

- 🔥 **Sistema de tipos**: Fuego > Planta > Agua (bonificaciones del 30%)
- ⬆️ **Sistema de niveles**: Aumento de ataque según nivel en combate
- 🌟 **Evoluciones**: Al subir de nivel, el Digipymon evoluciona cambiando nombre y stats
- 🗺️ **Zonas de exploración**: Áreas con Digipymons de mayor nivel y enemigos más fuertes
- 🍀 **Ítem "Suerte"**: Aumenta temporalmente la probabilidad de captura
- 🖥️ **Interfaz gráfica** con tkinter u otra biblioteca GUI


<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0A0E27,50:00D4AA,100:7B2FF7&height=100&section=footer"/>
  
   Proyecto académico desarrollado en NDT 
  
</div>
