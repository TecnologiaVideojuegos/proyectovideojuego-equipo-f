
# # # ACTUALIZACION IF HAS_GANADO # # #

        if self.has_ganado:

            self.jugador.dinero += 150
            self.room_victoria = 1
            self.x_victoria = 200
            self.y_victoria = 200
            self.current_room = self.room_victoria
            self.player_sprite.center_x = self.x_victoria
            self.player_sprite.center_y = self.y_victoria
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.current_enemy = ""
            self.current_trainer = ""
            self.has_ganado = False
            
# # # ACTUALIZACION IF HAS_PERDIDO # # #

        if self.has_perdido:

            #Si has perdido contra un entrenador, curar a los enemigos
            if not self.is_salvaje:
                for fakemon_muerto in self.current_trainer.lista_muertos:
                    fakemon_muerto.HP = fakemon_muerto.HP_MAX
                    self.current_trainer.lista_equipo.append(fakemon_muerto)
                self.is_salvaje = True

            for fakemon_muerto in self.jugador.lista_muertos:
                print(fakemon_muerto.nombre)
                fakemon_muerto.HP =  fakemon_muerto.HP_MAX
                self.jugador.lista_equipo.append(fakemon_muerto)
            self.current_room = 0
            self.player_sprite.center_x = 840
            self.player_sprite.center_y = 120
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                             self.rooms[self.current_room].wall_list)
            self.current_enemy = ""
            self.current_trainer = ""
            self.has_perdido = False
            
            
# # # FUNCION COMPLETA PARA EL COMBATE # # #

        if (self.current_room == 2 ):

            #Combate contra enemigo salvaje
            if self.is_salvaje :
                if key == arcade.key.KEY_1:
                    Combate.atacar(self.current_ally, self.current_enemy)
                    print("HP enemigo:" + str(self.current_enemy.HP))
                    print("HP aliado:" + str(self.current_ally.HP))
                    self.has_perdido, self.has_ganado = Combate.checkeo(self.jugador, self.current_ally,
                                                                        self.current_enemy)
                    print(str(self.has_ganado))
                    print(str(self.has_perdido))

                    # Turno enemigo
                    Combate.atacar(self.current_enemy, self.current_ally)
                    print("HP enemigo:" + str(self.current_enemy.HP))
                    print("HP aliado:" + str(self.current_ally.HP))
                    self.has_perdido, self.has_ganado = Combate.checkeo(self.jugador, self.current_ally,
                                                                        self.current_enemy)
                    print(str(self.has_ganado))
                    print(str(self.has_perdido))

                if key == arcade.key.KEY_2:
                    if (self.jugador.inventario["Pocion"] > 0 and self.current_ally.HP < self.current_ally.HP_MAX):
                        self.current_ally.HP = int(self.current_ally.HP * 1.5)
                        if (self.current_ally.HP > self.current_ally.HP_MAX):
                            self.current_ally.HP = self.current_ally.HP_MAX

                        self.jugador.inventario["Pocion"] -= 1
                        print("N pociones" + str(self.jugador.inventario["Pocion"]))

                        # Turno enemigo
                        Combate.atacar(self.current_enemy, self.current_ally)
                        print("HP enemigo:" + str(self.current_enemy.HP))
                        print("HP aliado:" + str(self.current_ally.HP))
                        self.has_perdido, self.has_ganado = Combate.checkeo(self.jugador, self.current_ally,
                                                                            self.current_enemy)
                        print(str(self.has_ganado))
                        print(str(self.has_perdido))

                if key == arcade.key.KEY_3:
                    # Intercambia el fakemon del jugador actual por el siguiente en la lista
                    fakemon_antiguo = self.jugador.lista_equipo[0]
                    self.jugador.lista_equipo.pop(0)
                    self.jugador.lista_equipo.append(fakemon_antiguo)

                if key == arcade.key.KEY_4:

                    # Si tiene cuerdas
                    if (self.jugador.inventario["Cuerda Huida"] > 0):

                        x = random.randrange(9)  # Numeros del 0 al 9

                        # La cuerda huida tiene un 30% de probabilidades de acertar, por lo tanto si x es 0, 1 o 2 surtira efecto
                        if -1 < x < 3:
                            self.cuerda_huida = True
                        else:
                            # Turno enemigo
                            Combate.atacar(self.current_enemy, self.current_ally)
                            print("HP enemigo:" + str(self.current_enemy.HP))
                            print("HP aliado:" + str(self.current_ally.HP))
                            self.has_perdido, self.has_ganado = Combate.checkeo(self.jugador, self.current_ally,
                                                                                self.current_enemy)
                            print(str(self.has_ganado))
                            print(str(self.has_perdido))



            #Combate contra entrenador
            else:

                print ("pokemons enemigos: ", str(self.current_trainer.lista_equipo[0].nombre))
                print("pokemons aliados: ", str(self.jugador.lista_equipo[0].nombre))

                if key == arcade.key.KEY_1:
                    Combate.atacar(self.current_ally, self.current_trainer.lista_equipo[0])
                    print("HP enemigo:" + str(self.current_trainer.lista_equipo[0].HP))
                    print("HP aliado:" + str(self.current_ally.HP))
                    self.has_perdido, self.has_ganado = Combate.checkeo_e(self.jugador, self.current_ally,
                                                                        self.current_trainer)
                    print(str(self.has_ganado))
                    print(str(self.has_perdido))
                    # Turno enemigo
                    Combate.atacar(self.current_trainer.lista_equipo[0], self.current_ally)
                    print("HP enemigo:" + str(self.current_trainer.lista_equipo[0].HP))
                    print("HP aliado:" + str(self.current_ally.HP))
                    self.has_perdido, self.has_ganado = Combate.checkeo_e(self.jugador, self.current_ally,
                                                                        self.current_trainer)
                    print(str(self.has_ganado))
                    print(str(self.has_perdido))

                if key == arcade.key.KEY_2:
                    if (self.jugador.inventario["Pocion"] > 0 and self.current_ally.HP < self.current_ally.HP_MAX):
                        self.current_ally.HP = int(self.current_ally.HP * 1.5)
                        if (self.current_ally.HP > self.current_ally.HP_MAX):
                            self.current_ally.HP = self.current_ally.HP_MAX

                        self.jugador.inventario["Pocion"] -= 1
                        print("N pociones" + str(self.jugador.inventario["Pocion"]))

                        # Turno enemigo
                        Combate.atacar(self.current_trainer.lista_equipo[0], self.current_ally)
                        print("HP enemigo:" + str(self.current_trainer.lista_equipo[0].HP))
                        print("HP aliado:" + str(self.current_ally.HP))
                        self.has_perdido, self.has_ganado = Combate.checkeo_e(self.jugador, self.current_ally,
                                                                            self.current_trainer)
                        print(str(self.has_ganado))
                        print(str(self.has_perdido))

                if key == arcade.key.KEY_3:
                    # Intercambia el fakemon del jugador actual por el siguiente en la lista
                    fakemon_antiguo = self.jugador.lista_equipo[0]
                    self.jugador.lista_equipo.pop(0)
                    self.jugador.lista_equipo.append(fakemon_antiguo)

                if key == arcade.key.KEY_4:

                    # Si tiene cuerdas
                    if (self.jugador.inventario["Cuerda Huida"] > 0):

                        x = random.randrange(9)  # Numeros del 0 al 9

                        # La cuerda huida tiene un 30% de probabilidades de acertar, por lo tanto si x es 0, 1 o 2 surtira efecto
                        if -1 < x < 3:
                            self.cuerda_huida = True
                        else:
                            # Turno enemigo
                            Combate.atacar(self.current_trainer.lista_equipo[0], self.current_ally)
                            print("HP enemigo:" + str(self.current_trainer.lista_equipo[0].HP))
                            print("HP aliado:" + str(self.current_ally.HP))
                            self.has_perdido, self.has_ganado = Combate.checkeo_e(self.jugador, self.current_ally,
                                                                                self.current_trainer)
                            print(str(self.has_ganado))
                            print(str(self.has_perdido))
                            
# # # FUNCION CHECKEO_E EN EL ARCHIVO COMBATE.PY# # #

def checkeo_e(jugador, aliado, enemigo):

    if aliado.HP > 0 and enemigo.lista_equipo[0].HP > 0:

        # El combate continua
        return False, False

    elif aliado.HP < 0:

        jugador.lista_muertos.append(jugador.lista_equipo[0])  # Meter en la lista de muertos
        jugador.lista_equipo.pop(0)  # Retirar del equipo de aliado

        # Intentar cambiar pokemon
        if len(jugador.lista_equipo) != 0:

            return False, False

        else:

            # Pierde el combate, volver al inicio
            # Volver a la habitacion inicial
            return True, False

    elif enemigo.lista_equipo[0].HP < 0:  # El fakemon enemigo esta muerto

        enemigo.lista_muertos.append(jugador.lista_equipo[0])  # Meter en la lista de muertos
        enemigo.lista_equipo.pop(0)  # Retirar del equipo de aliado

        # Comprobamos si quedan mas enemigos
        if len(enemigo.lista_equipo) != 0:

            return False, False

        # Si no quedan mas
        else:

            # Gana el combate
            return False, True
