# Librerias externas
import os
import arcade
import random
# Librerias internas
import Objeto_Entrenador
import Objeto_Pokemon
from tests import Combate, Optimizar
from tests.Generar_Fakemon import nuevo_salvaje
from tests.Optimizar import habitaciones, texturas_jugador

WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.6
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

VIEWPORT_MARGIN_TOP = 60
VIEWPORT_MARGIN_BOTTOM = 60
VIEWPORT_RIGHT_MARGIN = 270
VIEWPORT_LEFT_MARGIN = 270
# MOVEMENT_SPEED = 2 es la velocidad normal
MOVEMENT_SPEED = 5


# Juego
class MyGame(arcade.Window):
    def __init__(self):
        """
        Constructor
        """
        super().__init__(WIDTH, HEIGHT, "Juego", fullscreen=True)

        self.set_mouse_visible(False)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        width, height = self.get_size()

        self.set_viewport(0, width, 0, height)

        self.current_room = 0
        self.rooms = None

        self.textura = None
        self.wall_list = None
        self.player_sprite = None
        self.player_list = None

        self.view_left = 0
        self.view_bottom = 0
        self.physics_engine = None

        # Variables globales para los principales procesos del juego
        self.tienda = False
        self.cuerda_huida = False
        self.fakemon_nuevo = False
        self.movimiento = True
        self.mensaje = ""
        self.mensaje_enemy = ""
        # Variables globales para el combate
        self.is_salvaje = False
        self.has_perdido = False
        self.has_ganado = False

        self.ally_ataque = False
        self.enemy_ataque = False
        self.pocion = False
        self.cambio = False

        self.fallo_huida = False
        self.no_huida = False
        self.subir_nivel = False
        self.current_trainer = ""
        self.current_enemy = ""
        self.current_ally = ""
        self.fakemon_nuevo_nombre = ""

        self.contador_combate = 120
        self.contador_mensaje = 180

        #Sonido
        self.sonido_fallo = arcade.load_sound("resources" + os.path.sep + "sound" + os.path.sep + "Choque de no poder pasar.mp3")
        self.sonido_Salto = arcade.load_sound("resources" + os.path.sep + "sounf" + os.path.sep + "Salto.mp3")

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_list = arcade.SpriteList()
        self.player_sprite = arcade.AnimatedWalkingSprite()
        # Establecemos las animaciones de los sprites
        self.player_sprite.stand_right_textures, \
        self.player_sprite.stand_left_textures, \
        self.player_sprite.walk_right_textures, \
        self.player_sprite.walk_left_textures, \
        self.player_sprite.walk_down_textures, \
        self.player_sprite.walk_up_textures = texturas_jugador()

        # Variables de mensajes
        self.mensaje = ""
        self.mensaje_enemy = ""
        # Posición de inicio del jugador
        self.player_sprite.center_x = 62
        self.player_sprite.center_y = 100

        self.player_list.append(self.player_sprite)

        # Sistema de habitaciones
        self.top_rooom = 4
        self.current_room = 0
        self.rooms = habitaciones()
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

        ###################Registro de fakemon################################
        # (nombre,tipo,nivel,exp_final,HP_MAX,ataque,defensa,imagen)
        path = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "ally"
        fakemon1 = Objeto_Pokemon.Fakemon("Pyro", "volcanico", 30, 20, 200, 100, 100, path + os.path.sep + "Pyro.png")
        self.fakemon2 = Objeto_Pokemon.Fakemon("Cablanta", "estelar", 30, 20, 200, 10, 10,
                                          path + os.path.sep + "Cablanta.png")
        self.fakemon3 = Objeto_Pokemon.Fakemon("", "vacio", 30, 20, 200, 10, 10, path + os.path.sep + "")
        self.fakemon4 = Objeto_Pokemon.Fakemon("Sargrey", "lunar", 30, 20, 200, 10, 10, path + os.path.sep + "Sargrey.png")

        ###################Registro de entrenadores################################
        self.jugador = Objeto_Entrenador.Entrenador("Doble elefante telépata de guerra")
        self.jugador.lista_equipo.append(fakemon1)
        self.trainer1 = Objeto_Entrenador.Entrenador("Segismundo")
        self.trainer1.lista_equipo = Optimizar.lista_entrenador(1)
        self.trainer2 = Objeto_Entrenador.Entrenador("Sigismundo")
        self.trainer2.lista_equipo = Optimizar.lista_entrenador(2)
        self.trainer3 = Objeto_Entrenador.Entrenador("Roberto")
        self.trainer3.lista_equipo = Optimizar.lista_entrenador(3)
        self.trainer4 = Objeto_Entrenador.Entrenador("Sagismundo")
        self.trainer4.lista_equipo = Optimizar.lista_entrenador(4)
        self.trainer5 = Objeto_Entrenador.Entrenador("Sogismundo")
        self.trainer5.lista_equipo = Optimizar.lista_entrenador(5)
        self.trainer6 = Objeto_Entrenador.Entrenador("Sugusmundo")
        self.trainer6.lista_equipo = Optimizar.lista_entrenador(6)
        self.trainer7 = Objeto_Entrenador.Entrenador("El protector de la torre")
        self.trainer7.lista_equipo = Optimizar.lista_entrenador(7)

        # Establecemos dos variables globales para el combate
        self.current_enemy = ""
        self.current_ally = self.jugador.lista_equipo[0]

    # Sistema para generar  texto :Esta funcion recibe el texto dentro de los sprites y dibuja en un cuadro
    def genera_texto(self, text):

        arcade.draw_lrwh_rectangle_textured(self.view_left, self.player_sprite.center_y / 5.15, WIDTH, HEIGHT / 2,
                                            arcade.load_texture(
                                                "resources" + os.path.sep + "sprites" + os.path.sep + "messages" + os.path.sep + text))

    def on_draw(self):
        # Establecemos el nivel
        arcade.start_render()
        self.rooms[self.current_room].textura.draw()
        self.rooms[self.current_room].wall_list.draw()
        self.player_list.draw()

        # Cuadros de texto correspondientes al pueblo
        if self.current_room == 3 and self.player_sprite.center_x == 471 and self.player_sprite.center_y == 681.5:
            self.genera_texto("cuadrocentro.png")

        if self.current_room == 3 and self.player_sprite.center_x == 745 and self.player_sprite.center_y == 649.5:
            # Dibuja el cuadro de texto
            self.genera_texto("cuadrotienda.png")
            # Dibuja la cantidad de Pociones que posee el jugador
            arcade.draw_text("Cantidad:" + str(self.jugador.inventario["Pocion"]), 350,
                             150, arcade.color.BLACK)
            # Dibuja la cantidad de Cuerdas huida que posee el jugador
            arcade.draw_text("Cantidad:" + str(self.jugador.inventario["Cuerda Huida"]), 800,
                             150, arcade.color.BLACK)
            # Dibuja la cantidad de dinero que tiene un jugador
            arcade.draw_text("Dinero:" + str(self.jugador.dinero), 600,
                             150, arcade.color.BLACK)

        if self.current_room == 3 and (self.player_sprite.center_x >= 271 and self.player_sprite.center_x <= 283) and self.player_sprite.center_y == 393.5:
            self.genera_texto("cuadrositiocerrado.png")

        if self.current_room == 3 and (self.player_sprite.center_x >= 73 and self.player_sprite.center_x <= 97) and self.player_sprite.center_y == 585.5:
            self.genera_texto("cuadrositiocerrado.png")

        if self.fakemon_nuevo: pass

        # Mapa de coordenadas utilizado para saber la dirección
        arcade.draw_text("Coordenada x:" + str(self.player_sprite.center_x), self.player_sprite.center_x + 10,
                         self.player_sprite.center_y, arcade.color.WHITE)
        arcade.draw_text("Coordenada y:" + str(self.player_sprite.center_y), self.player_sprite.center_x + 10,
                         self.player_sprite.center_y - 10, arcade.color.WHITE)

        # Sistema de texto dinamico para combates fakemon
        if self.current_room == 12:
            arcade.draw_text(self.current_ally.nombre + "                    " + str(self.current_ally.nivel), 534, 253,
                             arcade.color.BLACK, 12)
            arcade.draw_text(
                str(self.current_ally.HP) + "/" + str(
                    self.current_ally.HP_MAX) + "                    " + self.current_ally.tipo + "                    " + str(
                    self.current_ally.contador_exp) + "/" + str(self.current_ally.exp_final), 534,
                223, arcade.color.BLACK, 12)

            arcade.draw_text(self.current_enemy.nombre + "                    " + str(self.current_enemy.nivel), 300,
                             530,
                             arcade.color.BLACK, 12)
            arcade.draw_text(
                str(self.current_enemy.HP) + "/" + str(
                    self.current_enemy.HP_MAX) + "                    " + self.current_enemy.tipo, 300,
                510, arcade.color.BLACK, 12)

            arcade.draw_text(
                str(self.current_enemy.HP) + "/" + str(
                    self.current_enemy.HP_MAX) + "                    " + self.current_enemy.tipo, 300,
                510, arcade.color.BLACK, 12)

            # Cargamos las imagenes de los fakemon
            arcade.draw_lrwh_rectangle_textured(730, 370, 250, 250, arcade.load_texture(self.current_enemy.imagen))
            arcade.draw_lrwh_rectangle_textured(120, 85, 300, 300, arcade.load_texture(self.current_ally.imagen))

            # Cargamos los distintos tipos de mensajes que pueden aparecer en el combate
            if self.ally_ataque:
                self.mensaje = "Tu " + self.current_ally.nombre + " ha infligido " + self.current_enemy.nombre + ":" + str(
                    int(Combate.num_atacar(self.current_ally, self.current_enemy))) + ".\n" + Combate.atacar_mensaje(
                    self.current_ally, self.current_enemy)
                self.ally_ataque = False

            if self.enemy_ataque:
                self.mensaje_enemy = self.current_enemy.nombre + " ha infligido " + self.current_ally.nombre + ":" + str(
                    int(Combate.num_atacar(self.current_enemy, self.current_ally)))
                self.enemy_ataque = False

            if self.pocion:
                self.mensaje = self.current_ally.nombre + " se ha curado " + str(self.curacion_total) + " gastando una poción en el proceso(" \
                               + str(self.jugador.inventario['Pocion']) + ")"
                self.curacion_total = 0
                self.pocion = False

            if self.cambio:
                self.mensaje = self.current_ally.nombre + " se retira, " + self.jugador.lista_equipo[
                    1].nombre + " entra en combate."
                self.cambio = False

            if self.fallo_huida:
                self.mensaje = "Has fallado al intentar huir del combate"
                self.fallo_huida = False

            if self.no_huida:
                self.mensaje = "No puedes huir cuando te enfrentas a entrenadores."
                self.mensaje_enemy = ""
                self.no_huida = False

            if self.has_ganado:
                self.mensaje = "Acabas de derrotar a " + self.current_enemy.nombre + " ganando 150 monedas \n y algo de experiencia para " + self.current_ally.nombre
                self.mensaje_enemy = ""

                if self.subir_nivel:
                    self.mensaje_enemy = self.current_ally.nombre + " acaba de subir a nivel" + str(self.current_ally.nivel) + "\n volviendose más fuerte"

            if self.has_perdido:
                self.mensaje = "Tras quedarte sin fakemon con los que combatir \n escapas del combate y regresas al pueblo."
                self.mensaje_enemy = ""


            print(self.mensaje)
            print(self.mensaje_enemy)
            arcade.draw_text(str(self.mensaje), 3, 480, arcade.color.BLACK, 11, 500)
            arcade.draw_text(str(self.mensaje_enemy), 2, 440, arcade.color.BLACK, 11, 500)

    def on_key_press(self, key, modifiers):
        # Sistema de movimiento
        if key == arcade.key.W and self.movimiento:
            self.player_sprite.change_y = MOVEMENT_SPEED
        if key == arcade.key.A and self.movimiento:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        if key == arcade.key.S and self.movimiento:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        if key == arcade.key.D and self.movimiento:
            self.player_sprite.change_x = MOVEMENT_SPEED
        # Sistema para pantalla completa
        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)

            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

        if not self.has_ganado and not self.has_perdido:
            if self.current_room == 12:

                # Combate vs salvaje
                if self.is_salvaje:

                    if key == arcade.key.KEY_1:
                        Combate.atacar(self.current_ally, self.current_enemy)
                        self.ally_ataque = True

                        self.has_perdido, self.has_ganado, self.current_ally, self.subir_nivel = Combate.checkeo(self.jugador, self.current_enemy)
                        # Turno enemigo
                        Combate.atacar(self.current_enemy, self.current_ally)
                        self.enemy_ataque = True

                        self.has_perdido, self.has_ganado, self.current_ally, self.subir_nivel = Combate.checkeo(self.jugador, self.current_enemy)

                    if key == arcade.key.KEY_2:

                        if self.jugador.inventario["Pocion"] > 0 and self.current_ally.HP < self.current_ally.HP_MAX:

                            self.curacion_total = float(self.current_ally.HP_MAX * 0.5)
                            self.current_ally.HP += self.curacion_total
                            self.pocion = True

                            if self.current_ally.HP > self.current_ally.HP_MAX:
                                self.current_ally.HP = self.current_ally.HP_MAX

                            self.jugador.inventario["Pocion"] -= 1

                            # Turno enemigo
                            Combate.atacar(self.current_enemy, self.current_ally)
                            self.enemy_ataque = True

                            self.has_perdido, self.has_ganado, self.current_ally, self.subir_nivel = Combate.checkeo(self.jugador, self.current_enemy)

                        else:
                            print ("NO quedan pociones o la vida es maxima")

                    if key == arcade.key.KEY_3 and len(self.jugador.lista_equipo) > 1:
                        # Intercambia el fakemon del jugador actual por el siguiente en la lista
                        self.cambio = True
                        fakemon_antiguo = self.jugador.lista_equipo[0]
                        self.jugador.lista_equipo.pop(0)
                        self.jugador.lista_equipo.append(fakemon_antiguo)
                        self.current_ally = self.jugador.lista_equipo[0]

                    if key == arcade.key.KEY_4:

                        # Si tiene cuerdas
                        if self.jugador.inventario["Cuerda Huida"] > 0:

                            x = random.randrange(9)  # Numeros del 0 al 9

                            # La cuerda huida tiene un 30% de probabilidades de acertar, por lo tanto si x es 0, 1 o 2 surtira efecto
                            if -1 < x < 3:
                                arcade.play_sound(self.sonido_Salto)
                                self.cuerda_huida = True
                            else:
                                arcade.play_sound(self.sonido_fallo)
                                self.fallo_huida = True
                                # Turno enemigo
                                Combate.atacar(self.current_enemy, self.current_ally)
                                self.enemy_ataque = True

                                self.has_perdido, self.has_ganado, self.current_ally, self.subir_nivel = Combate.checkeo(self.jugador, self.current_enemy)

                        elif self.jugador.inventario["Cuerda Huida"] == 0: arcade.play_sound(self.sonido_fallo)


                # Combate vs entrenador
                else:

                    if key == arcade.key.KEY_1:
                        Combate.atacar(self.current_ally, self.current_trainer.lista_equipo[0])
                        self.ally_ataque = True

                        print("HP enemigo:" + str(self.current_trainer.lista_equipo[0].HP))
                        print("HP aliado:" + str(self.current_ally.HP))

                        self.has_perdido, self.has_ganado, self.current_ally, self.current_trainer = Combate.checkeo_e(
                            self.jugador, self.current_trainer)

                        print("Enemigo: " + self.current_enemy.nombre)
                        print("Aliado: " + self.current_ally.nombre)

                        print("Peder: " + str(self.has_perdido))
                        print("Ganar: " + str(self.has_ganado))

                        # Turno enemigo
                        Combate.atacar(self.current_trainer.lista_equipo[0], self.current_ally)
                        self.enemy_ataque = True

                        print("HP enemigo:" + str(self.current_trainer.lista_equipo[0].HP))
                        print("HP aliado:" + str(self.current_ally.HP))

                        self.has_perdido, self.has_ganado, self.current_ally, self.current_trainer = Combate.checkeo_e(
                            self.jugador, self.current_trainer)

                        print("Enemigo: " + self.current_enemy.nombre)
                        print("Aliado: " + self.current_ally.nombre)

                        print("Peder: " + str(self.has_perdido))
                        print("Ganar: " + str(self.has_ganado))

                    if key == arcade.key.KEY_2:
                        if self.jugador.inventario["Pocion"] > 0 and self.current_ally.HP < self.current_ally.HP_MAX:
                            self.current_ally.HP = int(self.current_ally.HP * 1.5)
                            self.pocion = True
                            if self.current_ally.HP > self.current_ally.HP_MAX:
                                self.current_ally.HP = self.current_ally.HP_MAX

                            self.jugador.inventario["Pocion"] -= 1
                            print("N pociones" + str(self.jugador.inventario["Pocion"]))

                            # Turno enemigo
                            Combate.atacar(self.current_trainer.lista_equipo[0], self.current_ally)
                            self.enemy_ataque = True

                            print("HP enemigo:" + str(self.current_trainer.lista_equipo[0].HP))
                            print("HP aliado:" + str(self.current_ally.HP))

                            self.has_perdido, self.has_ganado, self.current_ally, self.current_trainer = Combate.checkeo_e(
                                self.jugador, self.current_trainer)

                            print("Enemigo: " + self.current_enemy.nombre)
                            print("Aliado: " + self.current_ally.nombre)

                            print("Peder: " + str(self.has_perdido))
                            print("Ganar: " + str(self.has_ganado))

                    if key == arcade.key.KEY_3 and len(self.jugador.lista_equipo) > 1:
                        # Intercambia el fakemon del jugador actual por el siguiente en la lista
                        self.cambio = True
                        fakemon_antiguo = self.jugador.lista_equipo[0]
                        self.jugador.lista_equipo.pop(0)
                        self.jugador.lista_equipo.append(fakemon_antiguo)
                        self.current_ally = self.jugador.lista_equipo[0]

                    if key == arcade.key.KEY_4:
                        self.no_huida = True
                        print("No puedes huir en combates contra entrenadores")

        # Sistema de tiendas
        if self.current_room == 3 and self.player_sprite.center_x == 745 and self.player_sprite.center_y == 649.5:
            if key == arcade.key.KEY_1 and self.jugador.dinero >= 50:
                print("Comprado Pocion")
                self.jugador.restar_dinero(50)
                self.jugador.inventario["Pocion"] += 1
                print(str(self.jugador.inventario["Pocion"]))
            if key == arcade.key.KEY_2 and self.jugador.dinero >= 100:
                print("Comprado Cuerda Huida")
                self.jugador.restar_dinero(100)
                self.jugador.inventario['Cuerda Huida'] += 1
                print(str(self.jugador.inventario['Cuerda Huida']))

        # Sistema de cuerda huida entre plantas
        if key == arcade.key.Q and self.current_room != 3 and self.jugador.inventario["Cuerda Huida"] != 0 and self.current_room != 12:
            self.cuerda_huida = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0

        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):


        # Call update on all sprites (The sprites don't do much in this example though.)
        self.player_list.update()
        self.player_list.update_animation()
        self.physics_engine.update()

        # Comprobamos la posicion del jugador al ganar el combate contra salvajes:
        if self.current_room != 12:
            self.x_victoria = self.player_sprite.center_x
            self.y_victoria = self.player_sprite.center_y

        # Volver si has ganado
        if self.has_ganado:
            self.movimiento = False

            print(str(self.contador_mensaje))
            if self.contador_mensaje == 0:
                self.current_room = self.top_rooom
                self.jugador.dinero += 150
                if self.is_salvaje:
                    self.player_sprite.center_x = self.x_victoria
                    self.player_sprite.center_y = self.y_victoria
                    self.is_salvaje = False

                # ERROR FALTA POR DEFINIR TRAINER Y POSICIONES DE VICTORIA
                # Sistema para devolver la posición de victoria contra entrenadores
                elif self.current_trainer == self.trainer1:
                    self.trainer1.no_derrotado = False
                    self.x_victoria = "Aun por definir"
                    self.y_victoria = "Aun por definir"

                elif self.current_trainer == self.trainer2:
                    self.trainer2.no_derrotado = False
                    # Añadir 1º fakemon
                    self.jugador.lista_equipo.append(self.fakemon2)
                    self.x_victoria = "Aun por definir"
                    self.y_victoria = "Aun por definir"

                elif self.current_trainer == self.trainer3:
                    self.trainer3.no_derrotado = False
                    self.x_victoria = "Aun por definir"
                    self.y_victoria = "Aun por definir"

                elif self.current_trainer == self.trainer4:
                    self.trainer4.no_derrotado = False
                    # Añadir 2º fakemon
                    self.jugador.lista_equipo.append(self.fakemon3)
                    self.x_victoria = "Aun por definir"
                    self.y_victoria = "Aun por definir"

                elif self.current_trainer == self.trainer5:
                    self.trainer5.no_derrotado = False
                    self.x_victoria = "Aun por definir"
                    self.y_victoria = "Aun por definir"

                elif self.current_trainer == self.trainer6:
                    self.trainer6.no_derrotado = False
                    # Añadir 3º fakemon
                    self.jugador.lista_equipo.append(self.fakemon4)
                    self.x_victoria = "Aun por definir"
                    self.y_victoria = "Aun por definir"

                elif self.current_trainer == self.trainer7:
                    self.trainer7.no_derrotado = False
                    self.x_victoria = "Aun por definir"
                    self.y_victoria = "Aun por definir"

                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.current_enemy = ""
                self.current_trainer = ""
                self.has_ganado = False
                self.movimiento = True
                self.subir_nivel = False
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1

        # Volver al inicio si has perdido
        if self.has_perdido:
            self.movimiento = False

            if self.contador_mensaje == 0:

                # Si has perdido contra un entrenador, curar a los enemigos
                if not self.is_salvaje:
                    for fakemon_muerto in self.current_trainer.lista_muertos:
                        fakemon_muerto.HP = fakemon_muerto.HP_MAX
                        self.current_trainer.lista_equipo.append(fakemon_muerto)

                for fakemon_muerto in self.jugador.lista_muertos:
                    fakemon_muerto.HP = fakemon_muerto.HP_MAX
                    self.jugador.lista_equipo.append(fakemon_muerto)

                self.current_room = 3
                self.player_sprite.center_x = 840
                self.player_sprite.center_y = 120
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)

                self.movimiento = True
                self.current_enemy = ""
                self.current_trainer = ""
                self.is_salvaje = False
                self.has_perdido = False
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1

        # Sistema para comprobar el mayor de los pisos y cambiar al piso donde se encontraba el jugador cuando sale de la torre
        if self.current_room > self.top_rooom and self.current_room != 12:
            self.top_rooom = self.current_room

        # Carga el piso desde el titulo del juego hasta la planta 3
        if self.current_room == 0 or self.current_room == 1 and 1140 <= self.player_sprite.center_x <= 1143 and 54.5 <= self.player_sprite.center_y <= 74:
            self.current_room += 1
            self.player_sprite.center_x = 62
            self.player_sprite.center_y = 100
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

        if self.current_room == 2 and 983 <= self.player_sprite.center_x and 169 <= self.player_sprite.center_y <= 201:
            self.current_room = 3
            self.player_sprite.center_x = 84
            self.player_sprite.center_y = 565
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

        # Carga el piso donde se encontraba el jugador por ultima vez       pueblo--> top_room
        if self.current_room == 3 and (841 <= self.player_sprite.center_x <= 855) and self.player_sprite.center_y == 137.5:
            self.current_room = self.top_rooom
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)

            if self.top_rooom == 4:
                self.player_sprite.center_x = 137
                self.player_sprite.center_y = 438.5

            elif self.top_rooom == 5:
                self.player_sprite.center_x = 137
                self.player_sprite.center_y = 438.5

            elif self.top_rooom == 6:
                self.player_sprite.center_x = 137
                self.player_sprite.center_y = 438.5

            elif self.top_rooom == 7:
                self.player_sprite.center_x = 137
                self.player_sprite.center_y = 438.5

            elif self.top_rooom == 8:
                self.player_sprite.center_x = 137
                self.player_sprite.center_y = 438.5

            elif self.top_rooom == 9:
                self.player_sprite.center_x = 137
                self.player_sprite.center_y = 438.5

            elif self.top_rooom == 10:
                self.player_sprite.center_x = 137
                self.player_sprite.center_y = 438.5

            elif self.top_rooom == 11:
                self.player_sprite.center_x = 137
                self.player_sprite.center_y = 438.5

        # Carga el piso del pueblo al salir de la torre
        if self.player_sprite.center_x == 183 and self.player_sprite.center_y == 438.5:
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 840
            self.player_sprite.center_y = 120
        # Sube de habitación al terminar el nivel
        if (873 <= self.player_sprite.center_x <= 887) and self.player_sprite.center_y == 457.5:
            self.current_room += 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 137
            self.player_sprite.center_y = 438.5

        # Sistema para generar fakemon salvajes dependiendo del piso donde se encuentre
        if 3 < self.current_room < 11:
            if self.player_sprite.change_x == MOVEMENT_SPEED or self.player_sprite.change_y == MOVEMENT_SPEED or self.player_sprite.change_x == -MOVEMENT_SPEED or self.player_sprite.change_y == -MOVEMENT_SPEED:

                if self.contador_combate == 0:
                    empieza_combate = random.randint(0, 500)
                    print(empieza_combate)
                    self.contador_combate = 120

                    
                    if empieza_combate >= 450:
                        self.mensaje_enemy = ""
                        self.mensaje = ""
                        self.current_enemy = nuevo_salvaje(self.current_room)
                        self.is_salvaje = True
                        self.current_room = 12
                        self.player_sprite.center_x = 500
                        self.player_sprite.center_y = 80
                        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                         self.rooms[self.current_room].wall_list)
                    
                else:
                    self.contador_combate -= 60


        # Sistema de vision para los entrenadores y generar sus combate
        if self.current_room == 4 and 361 <= self.player_sprite.center_x <= 503 and 189.5 <= self.player_sprite.center_y <= 329.5 and self.trainer1.no_derrotado:
            self.is_salvaje = False
            self.current_trainer = self.trainer1
            print ("encontrado")
            #Coords: 402/329.5


            # ERROR Menasje??
            if (self.contador_mensaje == 0):
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
                # ERROR Mensaje??
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 5 and 375 <= self.player_sprite.center_x <= 600 and 118 <= self.player_sprite.center_y <= 378.5 and self.trainer2.no_derrotado:
            self.is_salvaje = False
            self.current_trainer = self.trainer2
            print("encontrado")
            #Coords: ?

            # ERROR Menasje??
            if self.contador_mensaje == 0:
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
                # ERROR Mensaje??
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 6 and 656 <= self.player_sprite.center_x <= 791 and 310.5 <= self.player_sprite.center_y <= 521.5 and self.trainer3.no_derrotado:
            self.is_salvaje = False
            self.current_trainer = self.trainer3
            print("encontrado")
            #Coords:696/521.5

            # ERROR Menasje??
            if self.contador_mensaje == 0:
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
                # ERROR Mensaje??
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 7 and 500 <= self.player_sprite.center_x <= 500 and 500 <= self.player_sprite.center_y <= 500 and self.trainer4.no_derrotado:
            self.is_salvaje = False
            self.current_trainer = self.trainer4
            #Coords = ?

            # ERROR Menasje??
            if self.contador_mensaje == 0:
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
                # ERROR Mensaje??
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1

        elif self.current_room == 8 and 383 <= self.player_sprite.center_x <= 567 and 173.5 <= self.player_sprite.center_y <= 293.5 and self.trainer5.no_derrotado:
            print("detectado")
            self.is_salvaje = False
            self.current_trainer = self.trainer5
            #Coords = 523/233.5

            # ERROR Menasje??
            if self.contador_mensaje == 0:
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                # ERROR Mensaje??
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 9 and 457 <= self.player_sprite.center_x <= 599 and 150.5 <= self.player_sprite.center_y <= 254.5 and self.trainer6.no_derrotado:
            self.is_salvaje = False
            self.current_trainer = self.trainer6
            print("encontrado")
            #Coords: 523/150.5

            # ERROR Menasje??
            if self.contador_mensaje == 0:
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
                # ERROR Mensaje??
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 10 and 557 <= self.player_sprite.center_x <= 735 and 104.5 <= self.player_sprite.center_y <= 254.5 and self.trainer7.no_derrotado:
            self.is_salvaje = False
            self.current_trainer = self.trainer7
            print("encontrado")
            #Coords: 667/104.5
            
            # ERROR Menasje??
            if self.contador_mensaje == 0:
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
                # ERROR Mensaje??
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        # Sistema para regresar al pueblo con cuerda huida
        if self.cuerda_huida:
            self.jugador.inventario["Cuerda Huida"] -= 1
            self.cuerda_huida = False
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 70
            self.player_sprite.center_y = 537.5

        # Sistema para restaurar HP de todos los fakemon
        if self.current_room == 3 and self.player_sprite.center_x == 471 and self.player_sprite.center_y == 681.5:

            for fakemon_muerto in self.jugador.lista_muertos:
                self.jugador.lista_equipo.append(fakemon_muerto)

            for fakemon in self.jugador.lista_equipo:
                fakemon.HP = fakemon.HP_MAX



            # Sistema de camara para jugador
        changed = False
        # Scroll left
        left_bndry = self.view_left + VIEWPORT_LEFT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        # Scroll right
        right_bndry = self.view_left + WIDTH - VIEWPORT_RIGHT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        # Scroll up
        top_bndry = self.view_bottom + HEIGHT - VIEWPORT_MARGIN_TOP
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        # Scroll down
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN_BOTTOM
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

        # If we need to scroll, go ahead and do it.
        if changed:
            self.view_left = int(self.view_left)
            self.view_bottom = int(self.view_bottom)
            arcade.set_viewport(self.view_left,
                                WIDTH + self.view_left,
                                self.view_bottom,
                                HEIGHT + self.view_bottom)


def main():
    window = MyGame()
    window.setup()
    arcade.run()


main()
