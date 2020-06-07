import os
import arcade

# La clase room es aquella clase que crea los escenarios donde se desplaza el jugador
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
    rooms = []
    # Titulo del juego
    room = setup_nivel("naranja")
    rooms.append(room)
    # Controles
    room = setup_nivel("naranja")
    rooms.append(room)
    # Historia
    room = setup_nivel("naranja")
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
    room = setup_nivel("naranja")
    rooms.append(room)
    # Combate
    room = setup_nivel("combate")
    rooms.append(room)
    return rooms

def texturas_jugador():

    #Cargamos textura de sprite quieto
    stand_right_textures = []
    stand_right_textures.append(arcade.load_texture(
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Derecha" + os.path.sep + "Der0.png"))

    stand_left_textures = []
    stand_left_textures.append(
        arcade.load_texture("resources/sprites/player/Izquierda/Izq0.png"))

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
        "resources" + os.path.sep + "sprites" + os.path.sep + "player" + os.path.sep + "Arriba/Arr3.png"))
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

    return  stand_right_textures,stand_left_textures,walk_right_textures,walk_left_textures,walk_down_textures,walk_up_textures