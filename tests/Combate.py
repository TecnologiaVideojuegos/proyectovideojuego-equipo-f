def atacar(atacante, defensor):

    if atacante.tipo == "demonio":
        if defensor.tipo == "demonio":  # demonio vs demonio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "cometa":  # demonio vs cometa
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

        elif defensor.tipo == "volcanico":  # demonio vs volcanico
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

        elif defensor.tipo == "estelar":  # demonio vs estelar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

        elif defensor.tipo == "vacio":  # demonio vs vacio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "lunar":  # demonio vs lunar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

    if atacante.tipo  == "cometa":
        if defensor.tipo == "demonio":  # cometa vs demonio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

        elif defensor.tipo == "cometa":  # cometa vs cometa
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "volcanico":  # cometa vs volcanico
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

        elif defensor.tipo == "estelar":  # cometa vs estelar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "vacio":  # cometa vs vacio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

        elif defensor.tipo == "lunar":  # cometa vs lunar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

    if atacante.tipo  == "volcanico":
        if defensor.tipo == "demonio":  # volcanico vs demonio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

        elif defensor.tipo == "cometa":  # volcanico vs cometa
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

        elif defensor.tipo == "volcanico":  # volcanico vs volcanico
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "estelar":  # volcanico vs estelar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

        elif defensor.tipo == "vacio":  # volcanico vs vacio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

        elif defensor.tipo == "lunar":  # volcanico vs lunar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

    if atacante.tipo  == "estelar":

        if defensor.tipo == "demonio":  # estelar vs demonio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

        elif defensor.tipo == "cometa":  # estelar vs cometa
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "volcanico":  # estelar vs volcanico
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

        elif defensor.tipo == "estelar":  # estelar vs  estelar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "vacio":  # estelar vs vacio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

        elif defensor.tipo == "lunar":  # estelar vs  lunar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

    if atacante.tipo  == "vacio":
        if defensor.tipo == "demonio":  # vacio vs demonio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "cometa":  # vacio vs cometa
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

        elif defensor.tipo == "volcanico":  # vacio vs volcanico
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

        elif defensor.tipo == "estelar":  # vacio vs estelar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

        elif defensor.tipo == "vacio":  # vacio vs vacio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "lunar":  # vacio vs lunar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

    if atacante.tipo  == "lunar":
        if defensor.tipo == "demonio":  # lunar vs demonio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

        elif defensor.tipo == "cometa":  # lunar vs cometa
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

        elif defensor.tipo == "volcanico":  # lunar vs volcanico
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "estelar":  # lunar vs estelar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 0.5

        elif defensor.tipo == "vacio":  # lunar vs vacio
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa) * 1.5

        elif defensor.tipo == "lunar":  # lunar vs lunar
            if (defensor.defensa > atacante.ataque):
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)


def exp(exp_actual, lvl_aliado, lvl_enemigo):
        # Comprobador de diferencia de niveles entre aliado y enemigo
        dif_nivel = lvl_aliado - lvl_enemigo
        # si nivel aliado es mayor->dara menos exp
        # si nivel aliado es menor->dara mas exp
        # si los niveles son iguales->dara un numero base de exp
        if dif_nivel == 0:
            exp_actual = exp_actual + 8
        elif dif_nivel > 0:
            exp_actual = exp_actual + 5
        elif dif_nivel < 0:
            exp_actual = exp_actual + 13

        return exp_actual

        
def checkeo(jugador, aliado, enemigo):

    if aliado.HP > 0 and enemigo.HP > 0:

        #El combate continua
        return False, False

    elif aliado.HP < 0:

        jugador.lista_muertos.append(jugador.lista_equipo[0])  # Meter en la lista de muertos
        jugador.lista_equipo.pop(0)  # Retirar del equipo de aliado

        #Intentar cambiar pokemon
        if len(jugador.lista_equipo) != 0:

            return False, False

        else:

            #Pierde el combate, volver al inicio
            # Volver a la habitacion inicial
            return True, False


    elif enemigo.HP < 0:

        #Gana el combate, ganar experienci y volver a la sala
        jugador.lista_equipo[0].contador_exp = exp(jugador.lista_equipo[0].contador_exp,
                                                      jugador.lista_equipo[0].nivel, enemigo.nivel)
        if(jugador.lista_equipo[0].contador_exp>jugador.lista_equipo[0].exp_final):
            jugador.lista_equipo[0]. subir_nivel()


        return False, True



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
