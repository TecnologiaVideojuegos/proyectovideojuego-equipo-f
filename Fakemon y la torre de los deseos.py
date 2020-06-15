# Librerias externas
import os
import arcade
import random
# Librerias internas

from Funciones.Generar_Fakemon import nuevo_salvaje
from Funciones import Combate, Optimizar, Objeto_Pokemon, Objeto_Entrenador, Generar_Fakemon
from Funciones.Optimizar import habitaciones, texturas_jugador

"""
Variables globales
"""
WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.6
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

VIEWPORT_MARGIN_TOP = 60
VIEWPORT_MARGIN_BOTTOM = 60
VIEWPORT_RIGHT_MARGIN = 270
VIEWPORT_LEFT_MARGIN = 270
MOVEMENT_SPEED = 3


# Juego
class MyGame(arcade.Window):
    def __init__(self):
        """
        Constructor de la clase MyGame
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
        self.movimiento = True
        self.mensaje_trainer = False
        self.no_pasar = False

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

        self.mensaje = ""
        self.mensaje_enemy = ""

        self.contador_combate = 120
        self.contador_mensaje = 180

        # Sonido
        self.sonido_fallo = arcade.load_sound(
            "resources" + os.path.sep + "sound" + os.path.sep + "Choque de no poder pasar.mp3")
        self.sonido_Salto = arcade.load_sound("resources" + os.path.sep + "sound" + os.path.sep + "Salto.mp3")

    def setup(self):
        """
        Setup del juego
        """
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


        # Posición de inicio del jugador

        self.player_sprite.center_x = 73
        self.player_sprite.center_y = 86.5

        self.player_list.append(self.player_sprite)


        # Sistema de habitaciones
        self.top_rooom = 4
        self.current_room = 0
        self.rooms = habitaciones()
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.rooms[self.current_room].wall_list)


        ###################Registro de fakemon################################
        # (nombre,tipo,nivel,exp_final,HP_MAX,ataque,defensa,imagen)
        path = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "ally"
        fakemon1 = Objeto_Pokemon.Fakemon("Pyro", "volcanico",1,10,25,12,5, path + os.path.sep + "Pyro.png")
        self.fakemon2 = Objeto_Pokemon.Fakemon("Cablanta", "estelar",14,220,149,73,40,
                                               path + os.path.sep + "Cablanta.png")
        self.fakemon3 = Objeto_Pokemon.Fakemon("Romeu", "vacio",25,450,204,106,62, path + os.path.sep + "Romeu.png")
        self.fakemon4 = Objeto_Pokemon.Fakemon("Sargrey", "lunar",36,880,259,139,84,
                                               path + os.path.sep + "Sargrey.png")


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
        self.trainer6 = Objeto_Entrenador.Entrenador("Sugismundo")
        self.trainer6.lista_equipo = Optimizar.lista_entrenador(6)
        self.trainer7 = Objeto_Entrenador.Entrenador("El protector de la torre")
        self.trainer7.lista_equipo = Optimizar.lista_entrenador(7)


        # Establecemos dos variables globales para el combate
        self.current_ally = self.jugador.lista_equipo[0]


    def genera_texto(self, text):
        """
        Sistema para generar  texto :Esta funcion recibe el texto dentro de los sprites y dibuja en un cuadro
        :param text: texto a imprimir por pantalla
        """

        arcade.draw_lrwh_rectangle_textured(self.view_left, self.player_sprite.center_y / 5.15, WIDTH, HEIGHT / 2,
                                            arcade.load_texture(
                                                "resources" + os.path.sep + "sprites" + os.path.sep + "messages" + os.path.sep + text))

    def on_draw(self):
        """
        Función on_draw del juego
        """
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

        if self.current_room == 3 and (271 <= self.player_sprite.center_x <= 283) and self.player_sprite.center_y == 393.5:
            self.genera_texto("cuadrositiocerrado.png")

        if self.current_room == 3 and (73 <= self.player_sprite.center_x <= 97) and self.player_sprite.center_y == 585.5:
            self.genera_texto("cuadrositiocerrado.png")


        # Cuadros de texto cuando vences a un entrenador
        #Entrenador 1
        if self.current_room == 4 and self.player_sprite.center_x == 393 and self.player_sprite.center_y == 246.5 and not self.trainer1.no_derrotado:
            self.genera_texto("victoria_trainer1.png")
        # Entrenador 2
        elif self.current_room == 5 and self.player_sprite.center_x == 479 and self.player_sprite.center_y == 137.5 and not self.trainer2.no_derrotado:
            self.genera_texto("victoria_trainer_fakemon2.png")
        # Entrenador 3
        elif self.current_room == 6 and self.player_sprite.center_x == 713 and self.player_sprite.center_y == 457.5 and not self.trainer3.no_derrotado:
            self.genera_texto("victoria_trainer3.png")
        # Entrenador 4
        elif self.current_room == 7 and self.player_sprite.center_x == 663 and self.player_sprite.center_y == 278.5 and not self.trainer4.no_derrotado:
            self.genera_texto("victoria_trainer_fakemon4.png")
        # Entrenador 5
        elif self.current_room == 8 and self.player_sprite.center_x == 527 and self.player_sprite.center_y == 233.5 and not self.trainer5.no_derrotado:
            self.genera_texto("victoria_trainer5.png")
        # Entrenador 6
        elif self.current_room == 9 and self.player_sprite.center_x == 631 and self.player_sprite.center_y == 241.5 and not self.trainer6.no_derrotado:
            self.genera_texto("victoria_trainer_fakemon6.png")
        # Entrenador 7
        elif self.current_room == 10 and self.player_sprite.center_x == 511 and self.player_sprite.center_y == 233 and not self.trainer7.no_derrotado:
            self.genera_texto("victoria_ultimo.png")


        # Cuadro de texto para cuando no derrotaste al entrenador de la planta
        if self.no_pasar:
            self.genera_texto("no_pasar.png")
            self.no_pasar = False


        # Sistema para generar mensajes de entrenadores
        if self.mensaje_trainer:
            # Entrenador 1
            if self.current_room == 4:
                self.genera_texto("trainer1.png")
            # Entrenador 2
            elif self.current_room == 5:
                self.genera_texto("trainer2.png")
            # Entrenador 3
            elif self.current_room == 6:
                self.genera_texto("trainer3.png")
            # Entrenador 4
            elif self.current_room == 7:
                self.genera_texto("trainer4.png")
            # Entrenador 5
            elif self.current_room == 8:
                self.genera_texto("trainer5.png")
            # Entrenador 6
            elif self.current_room == 9:
                self.genera_texto("trainer6.png")
            # Entrenador 7
            elif self.current_room == 10:
                self.genera_texto("trainer7.png")

            self.mensaje_trainer = False


        # Sistema de texto dinamico para combates fakemon
        if self.current_room == 12:
            #Muestra los datos del aliado
            arcade.draw_text(self.current_ally.nombre + "                    " + str(self.current_ally.nivel), 534, 253,
                             arcade.color.BLACK, 12)
            arcade.draw_text(
                str(self.current_ally.HP) + "/" + str(
                    self.current_ally.HP_MAX) + "                    " + self.current_ally.tipo + "               " + str(
                    self.current_ally.contador_exp) + "/" + str(self.current_ally.exp_final), 534,
                223, arcade.color.BLACK, 12)

            #Muestra los datos del enemigo
            arcade.draw_text(self.current_enemy.nombre + "                    " + str(self.current_enemy.nivel), 300,
                             530,
                             arcade.color.BLACK, 12)
            arcade.draw_text(
                str(self.current_enemy.HP) + "/" + str(
                    self.current_enemy.HP_MAX) + "                    " + self.current_enemy.tipo, 300,
                510, arcade.color.BLACK, 12)


            # Cargamos las imagenes de los fakemon
            arcade.draw_lrwh_rectangle_textured(730, 370, 250, 250, arcade.load_texture(self.current_enemy.imagen))
            arcade.draw_lrwh_rectangle_textured(120, 85, 300, 300, arcade.load_texture(self.current_ally.imagen))


            # Cargamos los distintos tipos de mensajes que pueden aparecer en el combate
            # Mensaje al atacar
            if self.ally_ataque:
                self.mensaje = "Tu " + self.current_ally.nombre + " ha infligido " + self.current_enemy.nombre + ":" + str(
                    int(Combate.num_atacar(self.current_ally, self.current_enemy))) + ".\n" + Combate.atacar_mensaje(
                    self.current_ally, self.current_enemy)
                self.ally_ataque = False

            # Mensaje al ser atacado
            if self.enemy_ataque:
                self.mensaje_enemy = self.current_enemy.nombre + " ha infligido " + self.current_ally.nombre + ":" + str(
                    int(Combate.num_atacar(self.current_enemy, self.current_ally)))
                self.enemy_ataque = False

            # Mensaje de curación
            if self.pocion:
                self.mensaje = self.current_ally.nombre + " se ha curado " + str(int(self.current_ally.HP_MAX * 0.5)
                                                                                 ) + " gastando una poción en el proceso(" \
                               + str(self.jugador.inventario['Pocion']) + ")"
                self.pocion = False

            # Mensaje al cambiar de fakemon aliado
            if self.cambio:
                self.mensaje = self.current_ally.nombre + " se retira, " + self.jugador.lista_equipo[
                    1].nombre + " entra en combate."
                self.cambio = False

            # Mensaje al fallar la huida
            if self.fallo_huida:
                self.mensaje = "Has fallado al intentar huir del combate"
                self.fallo_huida = False

            # Mensaje al intentar huir en un combate contra entrenadores
            if self.no_huida:
                self.mensaje = "No puedes huir cuando te enfrentas a entrenadores."
                self.mensaje_enemy = ""
                self.no_huida = False

            # Mensaje de victoria
            if self.has_ganado:
                self.mensaje = "Acabas de derrotar a " + self.current_enemy.nombre + " ganando 150 monedas \n y algo de experiencia para " + self.current_ally.nombre
                self.mensaje_enemy = ""
                # Si sube de nivel imprime otro mensaje
                if self.subir_nivel:
                    self.mensaje_enemy = self.current_ally.nombre + " acaba de subir a nivel " + str(
                        self.current_ally.nivel) + "\n volviendose más fuerte"

            # Mensaje de derrota
            if self.has_perdido:
                self.mensaje = "Tras quedarte sin fakemon con los que combatir \n escapas del combate y regresas al pueblo."
                self.mensaje_enemy = ""

            # Dibuja los mensajes
            arcade.draw_text(str(self.mensaje), 3, 480, arcade.color.BLACK, 11, 500)
            arcade.draw_text(str(self.mensaje_enemy), 1, 440, arcade.color.BLACK, 11, 500)


    def on_key_press(self, key, modifiers):
        """
        Sistemas de teclas del juego
        """

        # Sistema de movimiento
        if self.movimiento:
            if key == arcade.key.W:
                self.player_sprite.change_y = MOVEMENT_SPEED
            if key == arcade.key.A:
                self.player_sprite.change_x = -MOVEMENT_SPEED
            if key == arcade.key.S:
                self.player_sprite.change_y = -MOVEMENT_SPEED
            if key == arcade.key.D:
                self.player_sprite.change_x = MOVEMENT_SPEED
        elif not self.movimiento:
            self.player_sprite.change_x = 0
            self.player_sprite.change_y = 0


        # Sistema para pantalla completa
        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)

            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)


        # Sistema de teclas para el comabte
        if not self.has_ganado and not self.has_perdido:  #Impide continuar el combate una vez terminado
            if self.current_room == 12:     # Si esta en la sala de combate

                # Combate contra fakemon salvaje
                if self.is_salvaje:

                    # Tecla 1: Atacar
                    if key == arcade.key.KEY_1:
                        # Aliado inflinge daño
                        Combate.atacar(self.current_ally, self.current_enemy)
                        self.ally_ataque = True

                        # Se comprueban las vidas
                        self.has_perdido, self.has_ganado, self.current_ally, self.subir_nivel = Combate.checkeo(
                            self.jugador, self.current_enemy)

                        # Enemigo inflinge daño
                        Combate.atacar(self.current_enemy, self.current_ally)
                        self.enemy_ataque = True

                        # Se comprueban las vidas
                        self.has_perdido, self.has_ganado, self.current_ally, self.subir_nivel = Combate.checkeo(
                            self.jugador, self.current_enemy)

                    # Tecla 2: Poción
                    if key == arcade.key.KEY_2:

                        # Si quedan pociones y no tiene la vida completa
                        if self.jugador.inventario["Pocion"] > 0 and self.current_ally.HP < self.current_ally.HP_MAX:

                            # Se cura
                            self.current_ally.HP += int(self.current_ally.HP_MAX * 0.5)
                            self.pocion = True

                            # Si la vida supera el máximo se corrige
                            if self.current_ally.HP > self.current_ally.HP_MAX:
                                self.current_ally.HP = self.current_ally.HP_MAX

                            # Se quita una poción del inventario
                            self.jugador.inventario["Pocion"] -= 1

                            # Enemigo inflinge daño
                            Combate.atacar(self.current_enemy, self.current_ally)
                            self.enemy_ataque = True

                            # Se comprueban las vidas
                            self.has_perdido, self.has_ganado, self.current_ally, self.subir_nivel = Combate.checkeo(
                                self.jugador, self.current_enemy)

                    # Tecla 3: Cambiar de aliado
                    if key == arcade.key.KEY_3 and len(self.jugador.lista_equipo) > 1:
                        # Intercambia el fakemon del jugador actual por el siguiente en la lista
                        self.cambio = True
                        fakemon_antiguo = self.jugador.lista_equipo[0]
                        self.jugador.lista_equipo.pop(0)
                        self.jugador.lista_equipo.append(fakemon_antiguo)
                        self.current_ally = self.jugador.lista_equipo[0]

                    # Tecla 4: Huir
                    if key == arcade.key.KEY_4:

                        # Si tiene cuerdas
                        if self.jugador.inventario["Cuerda Huida"] > 0:

                            x = random.randrange(9)  # Numeros del 0 al 9

                            # La cuerda huida tiene un 30% de probabilidades de acertar, por lo tanto si x es 0, 1 o 2 surtira efecto
                            if -1 < x < 3:
                                arcade.play_sound(self.sonido_Salto)
                                self.cuerda_huida = True

                            # Si falla
                            else:
                                arcade.play_sound(self.sonido_fallo)
                                self.fallo_huida = True

                                # Enemigo inflinge daño
                                Combate.atacar(self.current_enemy, self.current_ally)
                                self.enemy_ataque = True

                                # Se comprueban vidas
                                self.has_perdido, self.has_ganado, self.current_ally, self.subir_nivel = Combate.checkeo(
                                    self.jugador, self.current_enemy)

                        # Si no tiene cuerdas
                        elif self.jugador.inventario["Cuerda Huida"] == 0:
                            arcade.play_sound(self.sonido_fallo)


                # Combate contra entrenador fakemon
                else:

                    # Tecla 1: Atacar
                    if key == arcade.key.KEY_1:

                        # Aliado inflinde daño
                        Combate.atacar(self.current_ally, self.current_trainer.lista_equipo[0])
                        self.ally_ataque = True

                        # Se comprueban vidas
                        self.has_perdido, self.has_ganado, self.current_ally, self.current_enemy, self.current_trainer, self.subir_nivel = Combate.checkeo_e(
                            self.jugador, self.current_trainer)

                        # Turno enemigo
                        if len(self.current_trainer.lista_equipo) != 0:

                            # Enemigo inflinge daño
                            Combate.atacar(self.current_trainer.lista_equipo[0], self.current_ally)
                            self.enemy_ataque = True

                            # Se comprueban vidas
                            self.has_perdido, self.has_ganado, self.current_ally, self.current_enemy, self.current_trainer, self.subir_nivel = Combate.checkeo_e(
                                self.jugador, self.current_trainer)

                    # Tecla 2: Poción
                    if key == arcade.key.KEY_2:

                        # Si quedan pociones y no tiene la vida completa
                        if self.jugador.inventario["Pocion"] > 0 and self.current_ally.HP < self.current_ally.HP_MAX:

                            # Se cura
                            self.current_ally.HP = int(self.current_ally.HP_MAX * 0.5)
                            self.pocion = True

                            # Si la vida supera el máximo se corrige
                            if self.current_ally.HP > self.current_ally.HP_MAX:
                                self.current_ally.HP = self.current_ally.HP_MAX

                            # Se quita una poción del inventario
                            self.jugador.inventario["Pocion"] -= 1

                            # Turno enemigo
                            if len(self.current_trainer.lista_equipo) != 0:

                                # Enemigo inflinge daño
                                Combate.atacar(self.current_trainer.lista_equipo[0], self.current_ally)
                                self.enemy_ataque = True

                                # Se comprueban las vidas
                                self.has_perdido, self.has_ganado, self.current_ally, self.current_enemy, self.current_trainer, self.subir_nivel = Combate.checkeo_e(
                                    self.jugador, self.current_trainer)

                    # Tecla 3: Cambiar fakemon aliado
                    if key == arcade.key.KEY_3 and len(self.jugador.lista_equipo) > 1:

                        # Intercambia el fakemon del jugador actual por el siguiente en la lista
                        self.cambio = True
                        fakemon_antiguo = self.jugador.lista_equipo[0]
                        self.jugador.lista_equipo.pop(0)
                        self.jugador.lista_equipo.append(fakemon_antiguo)
                        self.current_ally = self.jugador.lista_equipo[0]

                    # Tecla 4: Huir
                    if key == arcade.key.KEY_4:
                        #No se puede huir contra entrenadores
                        self.no_huida = True


        # Sistema de tiendas
        if self.current_room == 3 and self.player_sprite.center_x == 745 and self.player_sprite.center_y == 649.5:

            # Comprar poción
            if key == arcade.key.KEY_1 and self.jugador.dinero >= 50:
                self.jugador.restar_dinero(50)
                self.jugador.inventario["Pocion"] += 1

            # Cuerda Huida
            if key == arcade.key.KEY_2 and self.jugador.dinero >= 100:
                self.jugador.restar_dinero(100)
                self.jugador.inventario['Cuerda Huida'] += 1


        # Sistema de cuerda huida entre plantas
        if key == arcade.key.Q and self.current_room != 3 and \
                self.jugador.inventario["Cuerda Huida"] != 0 and self.current_room != 12:
            self.cuerda_huida = True



    def on_key_release(self, key, modifiers):
        """
        Función on_key_release del juego, frena al jugador si no presiona las teclas
        """
        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0

        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0


    def on_update(self, delta_time):
        """
        Función on_update del juego
        """

        # Actualiza los sprites
        self.player_list.update()
        self.player_list.update_animation()
        self.physics_engine.update()

        # Comprobamos la posicion del jugador al ganar el combate contra salvajes:
        if self.current_room != 12:
            self.x_victoria = self.player_sprite.center_x
            self.y_victoria = self.player_sprite.center_y

        # Se activa si has ganado
        if self.has_ganado:
            # Se impide el movimiento del jugador
            self.movimiento = False

            # Cuando el contador pare
            if self.contador_mensaje == 0:

                self.current_room = self.top_rooom # Se lleva al jugador a la habitación anterior
                self.jugador.dinero += 150 # Se suma el dinero tras el combate

                # Sistema para devolver la posición de victoria contra entrenadores
                if self.current_trainer == self.trainer1:
                    self.trainer1.no_derrotado = False
                    self.x_victoria = 393
                    self.y_victoria = 246.5

                elif self.current_trainer == self.trainer2:
                    self.trainer2.no_derrotado = False
                    #Añade un fakemon nuevo al equipo
                    self.jugador.lista_equipo.append(self.fakemon2)
                    self.x_victoria = 479
                    self.y_victoria = 137.5

                elif self.current_trainer == self.trainer3:
                    self.trainer3.no_derrotado = False
                    self.x_victoria = 713
                    self.y_victoria = 457.5

                elif self.current_trainer == self.trainer4:
                    self.trainer4.no_derrotado = False
                    # Añade un fakemon nuevo al equipo
                    self.jugador.lista_equipo.append(self.fakemon3)
                    self.x_victoria = 663
                    self.y_victoria = 278.5

                elif self.current_trainer == self.trainer5:
                    self.trainer5.no_derrotado = False
                    self.x_victoria = 631
                    self.y_victoria = 241.5

                elif self.current_trainer == self.trainer6:
                    self.trainer6.no_derrotado = False
                    # Añade un fakemon nuevo al equipo
                    self.jugador.lista_equipo.append(self.fakemon4)
                    self.x_victoria = 631
                    self.y_victoria = 241.5

                elif self.current_trainer == self.trainer7:
                    self.trainer7.no_derrotado = False
                    self.x_victoria = 511
                    self.y_victoria = 233

                # Si se peleaba contra salvajes se vuelve a la ultima posición del personaje
                if self.is_salvaje:
                    self.player_sprite.center_x = self.x_victoria
                    self.player_sprite.center_y = self.y_victoria
                    self.is_salvaje = False

                # Posiciona al jugador en las x e y indicadas anteriormente
                self.player_sprite.center_x = self.x_victoria
                self.player_sprite.center_y = self.y_victoria

                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)

                # Se vacían los mensajes para que no aparezcan en el siguiente combate
                self.current_enemy = ""
                self.current_trainer = ""

                #Se devuelven las variables a su valor original
                self.has_ganado = False
                self.movimiento = True
                self.subir_nivel = False
                self.contador_mensaje = 180

            # El contador continua
            else:
                self.contador_mensaje -= 1


        # Si activa si has perdido
        if self.has_perdido:

            # Se impide el movimiento
            self.movimiento = False

            # Si el contador para
            if self.contador_mensaje == 0:

                # Si has perdido contra un entrenador, curar a los enemigos
                if not self.is_salvaje:
                    for fakemon_muerto in self.current_trainer.lista_muertos:
                        fakemon_muerto.HP = fakemon_muerto.HP_MAX
                        self.current_trainer.lista_equipo.append(fakemon_muerto)

                    for fakemon_herido in self.current_trainer.lista_equipo:
                        fakemon_herido.HP = fakemon_herido.HP_MAX

                # Cura a tus fakemons
                for fakemon_muerto in self.jugador.lista_muertos:
                    fakemon_muerto.HP = fakemon_muerto.HP_MAX
                    self.jugador.lista_equipo.append(fakemon_muerto)

                # Se coloca al jugador en el inicio
                self.current_room = 3
                self.player_sprite.center_x = 840
                self.player_sprite.center_y = 120
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                # Se reinician los mensajes
                self.mensaje = ""
                self.mensaje_enemy = ""

                # Se devuelven las variables a su valor original
                self.movimiento = True
                self.current_enemy = ""
                self.current_trainer = ""
                self.is_salvaje = False
                self.has_perdido = False
                self.contador_mensaje = 180

            # Si el contador sigue
            else:
                self.contador_mensaje -= 1


        # Sistema para comprobar el mayor de los pisos y cambiar al piso donde se encontraba el jugador cuando sale de la torre
        if self.current_room > self.top_rooom and self.current_room != 12:
            self.top_rooom = self.current_room


        # Carga el piso desde el titulo del juego hasta la planta 3
        if self.current_room == 0 and self.player_sprite.center_x == 439 and 86.5 <= self.player_sprite.center_y <= 105.5:
            self.current_room = 1
            self.player_sprite.center_x = 430
            self.player_sprite.center_y = 620
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
        if self.current_room == 1 and 280 <= self.player_sprite.center_x <= 440 and 130 <= self.player_sprite.center_y <= 230:
            self.current_room = 2
            self.player_sprite.center_x = 200
            self.player_sprite.center_y = 200
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
        if self.current_room == 2 and 983 <= self.player_sprite.center_x and 169 <= self.player_sprite.center_y <= 201:
            self.current_room = 3
            self.player_sprite.center_x = 84
            self.player_sprite.center_y = 565
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)


        # Carga el piso donde se encontraba el jugador por ultima vez       pueblo--> top_room
        if self.current_room == 3 and (
                841 <= self.player_sprite.center_x <= 855) and self.player_sprite.center_y == 137.5:
            self.current_room = self.top_rooom
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)

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
                self.player_sprite.center_x = 707
                self.player_sprite.center_y = 448.5


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
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.player_sprite.center_x = 137
            self.player_sprite.center_y = 438.5

        # Sistema para generar fakemon salvajes dependiendo del piso donde se encuentre
        if 3 < self.current_room < 11:
            # Cuando el jugador se mueve se activa un condador
            if self.player_sprite.change_x == MOVEMENT_SPEED or self.player_sprite.change_y == MOVEMENT_SPEED or \
                    self.player_sprite.change_x == -MOVEMENT_SPEED or self.player_sprite.change_y == -MOVEMENT_SPEED:
                
                # Se genera un numero aleatorio
                if self.contador_combate == 0:
                    empieza_combate = random.randint(0, 500)
                    self.contador_combate = 120

                    # Si ese numero es mayor o igual a 450 se inicia un combate
                    if empieza_combate >= 450:
                        # Se limpian los mensajes
                        self.mensaje_enemy = ""
                        self.mensaje = ""
                        # Se usa la funcion nuevo_salvaje para generar un fakemon aleatorio
                        self.current_enemy = nuevo_salvaje(self.current_room)
                        # Se modifican las variables necesarias para el combate
                        self.is_salvaje = True
                        self.current_room = 12
                        self.player_sprite.center_x = 500
                        self.player_sprite.center_y = 80
                        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                         self.rooms[self.current_room].wall_list)
                
                else:
                    self.contador_combate -= 60
        
        
        #Sistema para evitar subir niveles si no ha derrotado al entrenador
        if 790 <= self.player_sprite.center_x <= 920 and 350 <= self.player_sprite.center_y <= 521 and 3 < self.current_room < 11:
            if self.current_room == 4 and self.trainer1.no_derrotado:
                trainer = self.trainer1
            elif self.current_room == 5 and self.trainer2.no_derrotado:
                trainer = self.trainer2
            elif self.current_room == 6 and self.trainer3.no_derrotado:
                trainer = self.trainer3
            elif self.current_room == 7 and self.trainer4.no_derrotado:
                trainer = self.trainer4
            elif self.current_room == 8 and self.trainer5.no_derrotado:
                trainer = self.trainer5
            elif self.current_room == 9 and self.trainer6.no_derrotado:
                trainer = self.trainer6
            elif self.current_room == 10 and self.trainer7.no_derrotado:
                trainer = self.trainer7
            else: trainer = ""
            if trainer != "" and trainer.no_derrotado:
                self.movimiento = False
                self.no_pasar = True
                if self.contador_mensaje == 0:
                    self.movimiento = True
                    self.no_pasar = False
                    self.player_sprite.center_x -= 30
                    self.player_sprite.center_y -= 30
                    self.contador_mensaje = 180

                else: self.contador_mensaje -=1

        # Sistema de vision para los entrenadores y genferar sus combate
        """
        Se crea un área de visión para los entrenadores, cuando el jugador entra en esta área se detiene y se muestra el
        mensaje de combate del entrenador. Si el entrenador ha sido derrotado el jugador puede moverse con libertad y 
        pasar a la siguiente zona. Si se acerca al entrenador y ya ha sido derrotado saldra el mensaje de victoria de 
        ese entrenador
        """
        if self.current_room == 4 and 361 <= self.player_sprite.center_x <= 730 and 189.5 <= self.player_sprite.center_y <= 329.5 and self.trainer1.no_derrotado:
            self.is_salvaje = False
            self.movimiento = False
            self.mensaje_trainer = True
            
            if self.contador_mensaje == 0:
                self.current_trainer = self.trainer1
                self.current_enemy = self.current_trainer.lista_equipo[0]
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.movimiento = True
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 5 and 375 <= self.player_sprite.center_x <= 600 and 118 <= self.player_sprite.center_y <= 378.5 and self.trainer2.no_derrotado:
            self.is_salvaje = False
            self.movimiento = False
            self.mensaje_trainer = True
            
            if self.contador_mensaje == 0:
                self.current_trainer = self.trainer2
                self.current_enemy = self.current_trainer.lista_equipo[0]
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.movimiento = True
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 6 and 656 <= self.player_sprite.center_x <= 791 and 310.5 <= self.player_sprite.center_y <= 521.5 and self.trainer3.no_derrotado:
            self.is_salvaje = False
            # Coords:795/513
            self.movimiento = False
            self.mensaje_trainer = True
            if self.contador_mensaje == 0:
                self.current_trainer = self.trainer3
                self.current_enemy = self.current_trainer.lista_equipo[0]
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.movimiento = True
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 7 and (
                457 <= self.player_sprite.center_x <= 727 or 649 <= self.player_sprite.center_x <= 727) and (
                250 <= self.player_sprite.center_y <= 313 or 55 <= self.player_sprite.center_y <= 313) and self.trainer4.no_derrotado:
            self.is_salvaje = False
            self.movimiento = False
            self.mensaje_trainer = True
            
            if self.contador_mensaje == 0:
                self.current_trainer = self.trainer4
                self.current_enemy = self.current_trainer.lista_equipo[0]
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.movimiento = True
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 8 and 383 <= self.player_sprite.center_x <= 567 and 173.5 <= self.player_sprite.center_y <= 293.5 and self.trainer5.no_derrotado:
            self.is_salvaje = False
            self.movimiento = False
            self.mensaje_trainer = True
            
            if self.contador_mensaje == 0:
                self.current_trainer = self.trainer5
                self.current_enemy = self.current_trainer.lista_equipo[0]
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.movimiento = True
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 9 and 457 <= self.player_sprite.center_x <= 599 and 150.5 <= self.player_sprite.center_y <= 300 and self.trainer6.no_derrotado:
            self.is_salvaje = False
            self.movimiento = False
            self.mensaje_trainer = True

            if self.contador_mensaje == 0:
                self.current_trainer = self.trainer6
                self.current_enemy = self.current_trainer.lista_equipo[0]
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.movimiento = True
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        elif self.current_room == 10 and 361 <= self.player_sprite.center_x <= 681 and 104.5 <= self.player_sprite.center_y <= 302 and self.trainer7.no_derrotado:
            self.is_salvaje = False
            self.movimiento = False
            self.mensaje_trainer = True

            if self.contador_mensaje == 0:
                self.current_trainer = self.trainer7
                self.current_enemy = self.current_trainer.lista_equipo[0]
                self.current_room = 12
                self.player_sprite.center_x = 500
                self.player_sprite.center_y = 80
                self.movimiento = True
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.rooms[self.current_room].wall_list)
                self.contador_mensaje = 180

            else:
                self.contador_mensaje -= 1


        # Sistema para regresar al pueblo con cuerda huida
        if self.cuerda_huida:
            self.jugador.inventario["Cuerda Huida"] -= 1
            self.cuerda_huida = False
            self.current_room = 3
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
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
        
        # Scroll izquierda
        left_bndry = self.view_left + VIEWPORT_LEFT_MARGIN
        if self.player_sprite.left < left_bndry:
            self.view_left -= left_bndry - self.player_sprite.left
            changed = True

        # Scroll derecha
        right_bndry = self.view_left + WIDTH - VIEWPORT_RIGHT_MARGIN
        if self.player_sprite.right > right_bndry:
            self.view_left += self.player_sprite.right - right_bndry
            changed = True

        # Scroll arriba
        top_bndry = self.view_bottom + HEIGHT - VIEWPORT_MARGIN_TOP
        if self.player_sprite.top > top_bndry:
            self.view_bottom += self.player_sprite.top - top_bndry
            changed = True

        # Scroll abajo
        bottom_bndry = self.view_bottom + VIEWPORT_MARGIN_BOTTOM
        if self.player_sprite.bottom < bottom_bndry:
            self.view_bottom -= bottom_bndry - self.player_sprite.bottom
            changed = True

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
