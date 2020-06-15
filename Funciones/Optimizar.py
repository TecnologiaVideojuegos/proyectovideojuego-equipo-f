import os
import arcade

# La clase room es aquella clase que crea los escenarios donde se desplaza el jugador
from Funciones import Objeto_Pokemon


class Room:
    """
    Esta clase crea y caga las distintas habitaciones del juego
    """

    def __init__(self):
        self.wall_list = None
        self.textura = None


def setup_nivel(nivel):
    """
    Crea una room
    """
    room = Room()

    # Lista de Sprites
    room.wall_list = arcade.SpriteList()
    room.textura = arcade.SpriteList()

    map = arcade.tilemap.read_tmx("resources" + os.path.sep + "maps" + os.path.sep + nivel + ".tmx")

    carga = arcade.process_layer(map, "Nivel", 1)
    wall = arcade.process_layer(map, "Muros Invisibles", 1)

    room.textura = carga
    room.wall_list = wall

    return room


def habitaciones():
    """
    Carga todas las habitaciones del juego
    :return: lista de habitaciones
    """
    rooms = []
    # Titulo del juego
    room = setup_nivel("inicio")
    rooms.append(room)
    # Controles
    room = setup_nivel("instrucciones")
    rooms.append(room)
    # Historia
    room = setup_nivel("historia")
    rooms.append(room)
    # Comienza el juego
    room = setup_nivel("nivel0")
    rooms.append(room)
    room = setup_nivel("nivel1")
    rooms.append(room)
    room = setup_nivel("nivel2")
    rooms.append(room)
    room = setup_nivel("nivel3")
    rooms.append(room)
    room = setup_nivel("nivel4")
    rooms.append(room)
    room = setup_nivel("nivel5")
    rooms.append(room)
    room = setup_nivel("nivel6")
    rooms.append(room)
    room = setup_nivel("nivel7")
    rooms.append(room)
    # Fin del juego
    room = setup_nivel("final")
    rooms.append(room)
    # Combate
    room = setup_nivel("combate")
    rooms.append(room)

    return rooms


def texturas_jugador():
    """
    Carga las distintas texturas del personaje principal
    :return: listas con los diferentes sprites
    """
    # Cargamos textura de sprite quieto
    stand_right_textures = [arcade.load_texture("resources" + os.path.sep + "sprites" + os.path.sep + "player" +
                                                os.path.sep + "Derecha" + os.path.sep + "Der0.png")]

    stand_left_textures = [arcade.load_texture("resources"+ os.path.sep +"sprites"+ os.path.sep +"player"+ os.path.sep +"Izquierda"+ os.path.sep +"Izq0.png")]

    # Cargamos las texturas para el movimiento derecho
    walk_right_textures = []
    walk_right_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Derecha" + os.path.sep + "Der1.png"))
    walk_right_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Derecha" + os.path.sep + "Der2.png"))
    walk_right_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Derecha" + os.path.sep + "Der3.png"))
    walk_right_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Derecha" + os.path.sep + "Der4.png"))
    walk_right_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Derecha" + os.path.sep + "Der5.png"))
    walk_right_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Derecha" + os.path.sep + "Der6.png"))
    walk_right_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Derecha" + os.path.sep + "Der7.png"))
    walk_right_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Derecha" + os.path.sep + "Der8.png"))

    # Cargamos las texturas para el movimiento  izquierdo
    walk_left_textures = []
    walk_left_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Izquierda" + os.path.sep + "Izq1.png"))
    walk_left_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Izquierda" + os.path.sep + "Izq2.png"))
    walk_left_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Izquierda" + os.path.sep + "Izq3.png"))
    walk_left_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Izquierda" + os.path.sep + "Izq4.png"))
    walk_left_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Izquierda" + os.path.sep + "Izq5.png"))
    walk_left_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Izquierda" + os.path.sep + "Izq6.png"))
    walk_left_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Izquierda" + os.path.sep + "Izq7.png"))
    walk_left_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Izquierda" + os.path.sep + "Izq8.png"))

    # Cargamos las texturas para el movimiento abajo
    walk_down_textures = []
    walk_down_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Abajo" + os.path.sep + "Abj0.png"))
    walk_down_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Abajo" + os.path.sep + "Abj1.png"))
    walk_down_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Abajo" + os.path.sep + "Abj2.png"))
    walk_down_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Abajo" + os.path.sep + "Abj3.png"))
    walk_down_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Abajo" + os.path.sep + "Abj4.png"))
    walk_down_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Abajo" + os.path.sep + "Abj5.png"))
    walk_down_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Abajo" + os.path.sep + "Abj6.png"))
    walk_down_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Abajo" + os.path.sep + "Abj7.png"))
    walk_down_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Abajo" + os.path.sep + "Abj8.png"))

    # Cargamos las texturas para el movimiento de arriba
    walk_up_textures = []
    walk_up_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Arriba" + os.path.sep + "Arr0.png"))
    walk_up_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Arriba" + os.path.sep + "Arr1.png"))
    walk_up_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Arriba" + os.path.sep + "Arr2.png"))
    walk_up_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Arriba"+ os.path.sep +"Arr3.png"))
    walk_up_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Arriba" + os.path.sep + "Arr4.png"))
    walk_up_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Arriba" + os.path.sep + "Arr5.png"))
    walk_up_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Arriba" + os.path.sep + "Arr6.png"))
    walk_up_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Arriba" + os.path.sep + "Arr7.png"))
    walk_up_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Arriba" + os.path.sep + "Arr8.png"))

    return stand_right_textures, stand_left_textures, walk_right_textures, walk_left_textures, walk_down_textures, walk_up_textures


def lista_entrenador(num):
    """
    Añade a cada entrenador sus fakemons asignados
    :return: devuelve la lista del equipo del entrenador
    """
    #(self, nombre, tipo, nivel, exp_final, HP_MAX, ataque, defensa, imagen)
    lista_equipo = []
    path = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "enemy"

    #Entrenador 1
    if num == 1:
        # Genera los fakemons
        fakemon = Objeto_Pokemon.Fakemon("Sarzul", "estelar",5,0,42,18,7, path + os.path.sep + "Sarzul.png")
        #Los añade al equipo
        lista_equipo.append(fakemon)

    elif num == 2:
        # Genera los fakemons
        fakemon = Objeto_Pokemon.Fakemon("Pyro", "volcanico", 10,0,118,64,25, path + os.path.sep + "Pyro.png")
        # Los añade al equipo
        lista_equipo.append(fakemon)

    elif num == 3:
        # Genera los fakemons
        fakemon1 = Objeto_Pokemon.Fakemon("Oryp", "demonio", 15,0,143,64,33, path + os.path.sep + "Oryp.png")
        fakemon2 = Objeto_Pokemon.Fakemon("Dodkei", "demonio", 18,0,147,78,48, path + os.path.sep + "Dodkei.png")
        # Los añade al equipo
        lista_equipo.append(fakemon1)
        lista_equipo.append(fakemon2)

    elif num == 4:
        # Genera los fakemons
        fakemon1 = Objeto_Pokemon.Fakemon("Romeu", "vacio",22,0,172,97,47, path + os.path.sep + "Romeu.png")
        fakemon2 = Objeto_Pokemon.Fakemon("Vacivus", "cometa", 24,0,198,90,51, path + os.path.sep + "Vacivus.png")
        # Los añade al equipo
        lista_equipo.append(fakemon1)
        lista_equipo.append(fakemon2)

    elif num == 5:
        # Genera los fakemons
        fakemon1 = Objeto_Pokemon.Fakemon("Fhenou", "cometa", 24,0,172,90,51, path + os.path.sep + "Fhenou.png")
        fakemon2 = Objeto_Pokemon.Fakemon("Curmtop", "cometa", 26,0,187,102,55, path + os.path.sep + "Curmtop.png")
        fakemon3 = Objeto_Pokemon.Fakemon("Raziel", "lunar", 30,0,212,121,63, path + os.path.sep + "Raziel.png")
        # Los añade al equipo
        lista_equipo.append(fakemon1)
        lista_equipo.append(fakemon2)
        lista_equipo.append(fakemon3)

    elif num == 6:
        # Genera los fakemons
        fakemon1 = Objeto_Pokemon.Fakemon("Cablanta Shiny", "lunar",34,0,233,133,80, path + os.path.sep + "Cablanta Shiny.png")
        fakemon2 = Objeto_Pokemon.Fakemon("Sargrey", "lunar",35,0,232,129,73, path + os.path.sep + "Sargrey.png")
        fakemon3 = Objeto_Pokemon.Fakemon("Cablanta", "estelar",36,0,232,126,76, path + os.path.sep + "Cablanta.png")
        # Los añade al equipo
        lista_equipo.append(fakemon1)
        lista_equipo.append(fakemon2)
        lista_equipo.append(fakemon3)

    elif num == 7:
        # Genera los fakemons
        fakemon1 = Objeto_Pokemon.Fakemon("Oryp", "demonio",37,0,258,129,77, path + os.path.sep + "Oryp.png")
        fakemon2 = Objeto_Pokemon.Fakemon("Raziel", "volcanico",38,0,242,132,79, path + os.path.sep + "Raziel.png")
        fakemon3 = Objeto_Pokemon.Fakemon("Romeu", "vacio",39,0,263,141,81, path + os.path.sep + "Romeu.png")
        fakemon4 = Objeto_Pokemon.Fakemon("Sarzul", "estelar",40,0,279,151,92, path + os.path.sep + "Sarzul.png")
        # Los añade al equipo
        lista_equipo.append(fakemon1)
        lista_equipo.append(fakemon2)
        lista_equipo.append(fakemon3)
        lista_equipo.append(fakemon4)


    return lista_equipo
    #TEMPORAL
    def subir_estadisticas(LVL, HP, A, D):
        if LVL <= 10:
            for i in range(1, LVL):
                HP *= 1.205
                A *= 1.23
                D *= 1.27
        # Para nivel entre 10 y 40
        elif 10 < LVL <= 40:
            # Subimos las estadisticas de los primeros 10 niveles
            for i in range(1, 10):
                HP *= 1.205
                A *= 1.23
                D *= 1.27
            for i in range(1, LVL - 10):
                A = A + 3  # a partir de nivel 10, las estadisticas suben valores fijos
                HP = HP + 5
                D = D + 2

        print(str(LVL) + "," + str(HP) + "," + str(A) + "," + str(D))
