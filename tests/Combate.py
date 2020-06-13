def atacar(atacante, defensor):

    if atacante.tipo == "demonio":
        if defensor.tipo == "demonio":  # demonio vs demonio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "cometa":  # demonio vs cometa
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "volcanico":  # demonio vs volcanico
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "estelar":  # demonio vs estelar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "vacio":  # demonio vs vacio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "lunar":  # demonio vs lunar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

    if atacante.tipo == "cometa":
        if defensor.tipo == "demonio":  # cometa vs demonio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "cometa":  # cometa vs cometa
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "volcanico":  # cometa vs volcanico
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "estelar":  # cometa vs estelar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "vacio":  # cometa vs vacio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "lunar":  # cometa vs lunar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

    if atacante.tipo == "volcanico":
        if defensor.tipo == "demonio":  # volcanico vs demonio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "cometa":  # volcanico vs cometa
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "volcanico":  # volcanico vs volcanico
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "estelar":  # volcanico vs estelar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "vacio":  # volcanico vs vacio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "lunar":  # volcanico vs lunar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

    if atacante.tipo == "estelar":

        if defensor.tipo == "demonio":  # estelar vs demonio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "cometa":  # estelar vs cometa
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "volcanico":  # estelar vs volcanico
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "estelar":  # estelar vs  estelar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "vacio":  # estelar vs vacio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "lunar":  # estelar vs  lunar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

    if atacante.tipo == "vacio":
        if defensor.tipo == "demonio":  # vacio vs demonio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "cometa":  # vacio vs cometa
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "volcanico":  # vacio vs volcanico
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "estelar":  # vacio vs estelar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "vacio":  # vacio vs vacio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "lunar":  # vacio vs lunar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

    if atacante.tipo == "lunar":
        if defensor.tipo == "demonio":  # lunar vs demonio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "cometa":  # lunar vs cometa
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "volcanico":  # lunar vs volcanico
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)

        elif defensor.tipo == "estelar":  # lunar vs estelar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "vacio":  # lunar vs vacio
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "lunar":  # lunar vs lunar
            if defensor.defensa >= atacante.ataque:
                defensor.HP -= 1
            else:
                defensor.HP -= (atacante.ataque - defensor.defensa)


def atacar_mensaje(atacante, defensor):
    if atacante.tipo == "demonio":
        if defensor.tipo == "demonio":  # demonio vs demonio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

        elif defensor.tipo == "cometa":  # demonio vs cometa
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

        elif defensor.tipo == "volcanico":  # demonio vs volcanico
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

        elif defensor.tipo == "estelar":  # demonio vs estelar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

        elif defensor.tipo == "vacio":  # demonio vs vacio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

        elif defensor.tipo == "lunar":  # demonio vs lunar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

    if atacante.tipo == "cometa":
        if defensor.tipo == "demonio":  # cometa vs demonio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

        elif defensor.tipo == "cometa":  # cometa vs cometa
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

        elif defensor.tipo == "volcanico":  # cometa vs volcanico
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

        elif defensor.tipo == "estelar":  # cometa vs estelar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

        elif defensor.tipo == "vacio":  # cometa vs vacio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

        elif defensor.tipo == "lunar":  # cometa vs lunar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

    if atacante.tipo == "volcanico":
        if defensor.tipo == "demonio":  # volcanico vs demonio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

        elif defensor.tipo == "cometa":  # volcanico vs cometa
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

        elif defensor.tipo == "volcanico":  # volcanico vs volcanico
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

        elif defensor.tipo == "estelar":  # volcanico vs estelar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

        elif defensor.tipo == "vacio":  # volcanico vs vacio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

        elif defensor.tipo == "lunar":  # volcanico vs lunar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

    if atacante.tipo == "estelar":

        if defensor.tipo == "demonio":  # estelar vs demonio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

        elif defensor.tipo == "cometa":  # estelar vs cometa
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

        elif defensor.tipo == "volcanico":  # estelar vs volcanico
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

        elif defensor.tipo == "estelar":  # estelar vs  estelar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

        elif defensor.tipo == "vacio":  # estelar vs vacio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

        elif defensor.tipo == "lunar":  # estelar vs  lunar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

    if atacante.tipo == "vacio":
        if defensor.tipo == "demonio":  # vacio vs demonio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

        elif defensor.tipo == "cometa":  # vacio vs cometa
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

        elif defensor.tipo == "volcanico":  # vacio vs volcanico
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

        elif defensor.tipo == "estelar":  # vacio vs estelar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

        elif defensor.tipo == "vacio":  # vacio vs vacio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

        elif defensor.tipo == "lunar":  # vacio vs lunar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

    if atacante.tipo == "lunar":
        if defensor.tipo == "demonio":  # lunar vs demonio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

        elif defensor.tipo == "cometa":  # lunar vs cometa
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

        elif defensor.tipo == "volcanico":  # lunar vs volcanico
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"

        elif defensor.tipo == "estelar":  # lunar vs estelar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "No es un ataque muy efectivo"

        elif defensor.tipo == "vacio":  # lunar vs vacio
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque muy efectivo"

        elif defensor.tipo == "lunar":  # lunar vs lunar
            if defensor.defensa >= atacante.ataque:
                return "Es un ataque muy efectivo"
            else:
                return "Es un ataque normal"


def num_atacar(atacante, defensor):
    if atacante.tipo == "demonio":
        if defensor.tipo == "demonio":  # demonio vs demonio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

        elif defensor.tipo == "cometa":  # demonio vs cometa
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "volcanico":  # demonio vs volcanico
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "estelar":  # demonio vs estelar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "vacio":  # demonio vs vacio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

        elif defensor.tipo == "lunar":  # demonio vs lunar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

    if atacante.tipo == "cometa":
        if defensor.tipo == "demonio":  # cometa vs demonio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "cometa":  # cometa vs cometa
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

        elif defensor.tipo == "volcanico":  # cometa vs volcanico
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "estelar":  # cometa vs estelar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

        elif defensor.tipo == "vacio":  # cometa vs vacio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "lunar":  # cometa vs lunar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

    if atacante.tipo == "volcanico":
        if defensor.tipo == "demonio":  # volcanico vs demonio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "cometa":  # volcanico vs cometa
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "volcanico":  # volcanico vs volcanico
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

        elif defensor.tipo == "estelar":  # volcanico vs estelar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "vacio":  # volcanico vs vacio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "lunar":  # volcanico vs lunar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

    if atacante.tipo == "estelar":

        if defensor.tipo == "demonio":  # estelar vs demonio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "cometa":  # estelar vs cometa
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

        elif defensor.tipo == "volcanico":  # estelar vs volcanico
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "estelar":  # estelar vs  estelar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

        elif defensor.tipo == "vacio":  # estelar vs vacio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "lunar":  # estelar vs  lunar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

    if atacante.tipo == "vacio":
        if defensor.tipo == "demonio":  # vacio vs demonio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

        elif defensor.tipo == "cometa":  # vacio vs cometa
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "volcanico":  # vacio vs volcanico
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "estelar":  # vacio vs estelar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "vacio":  # vacio vs vacio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

        elif defensor.tipo == "lunar":  # vacio vs lunar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

    if atacante.tipo == "lunar":
        if defensor.tipo == "demonio":  # lunar vs demonio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "cometa":  # lunar vs cometa
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "volcanico":  # lunar vs volcanico
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa

        elif defensor.tipo == "estelar":  # lunar vs estelar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 0.5)

        elif defensor.tipo == "vacio":  # lunar vs vacio
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return int((atacante.ataque - defensor.defensa) * 1.5)

        elif defensor.tipo == "lunar":  # lunar vs lunar
            if defensor.defensa >= atacante.ataque:
                return 1
            else:
                return atacante.ataque - defensor.defensa


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


def checkeo(jugador, enemigo):
    subir_nivel = False
    aliado = jugador.lista_equipo[0]

    # Los dos tienen vida
    if aliado.HP > 0 and enemigo.HP > 0:

        # El combate continua
        return False, False, aliado, subir_nivel

    # El aliado no tiene vida
    elif aliado.HP <= 0:

        # El fakemon muere
        jugador.lista_muertos.append(jugador.lista_equipo[0])  # Meter en la lista de muertos
        jugador.lista_equipo.pop(0)  # Retirar del equipo de aliado

        # Si hay mas fakemon
        if len(jugador.lista_equipo) != 0:

            # El combate continua
            return False, False, jugador.lista_equipo[
                0], subir_nivel  # El enemigo sigue siendo el mismo, pero el aliado cambia al primero de la lista

        # Si no quedan mas pokemon
        else:

            # Pierde el combate, volver al inicio
            return True, False, " ", subir_nivel  # El enemigo y el aliado desaparecen

    # El enemigo ha muerto
    elif enemigo.HP <= 0:

        # Gana el combate
        # Suma experiencia
        aliado.contador_exp = exp(aliado.contador_exp, aliado.nivel, enemigo.nivel)
        if aliado.contador_exp >= aliado.exp_final:
            aliado.subir_nivel()
            subir_nivel = True

        # Ganas el combate
        return False, True, aliado, subir_nivel  # El enemigo desaparece y el aliado continua siendo el mismo


def checkeo_e(jugador, entrenador):
    aliado = jugador.lista_equipo[0]
    enemigo = entrenador.lista_equipo[0]
    subir_nivel = False

    for pokemon in entrenador.lista_equipo: print(pokemon.nombre)

    # Los dos tiene vida
    if aliado.HP > 0 and enemigo.HP > 0:

        # El combate continua
        return False, False, aliado, enemigo, entrenador, subir_nivel

    # El aliado muere
    elif aliado.HP <= 0:

        jugador.lista_muertos.append(jugador.lista_equipo[0])  # Meter en la lista de muertos
        jugador.lista_equipo.pop(0)  # Retirar del equipo de aliado

        # Si quedan mas aliados
        if len(jugador.lista_equipo) != 0:

            # El combate continua
            return False, False, jugador.lista_equipo[0], enemigo, entrenador, subir_nivel  # El enemigo se mantiene y el aliado pasa a ser el primero en la lista

        # No quedan mas aliados
        else:

            # Pierde el combate, volver al inicio
            return True, False, aliado, enemigo, entrenador, subir_nivel  # El aliado y el entrenador se mantiene para curar a los fakemons

    # El fakemon enemigo esta muerto
    elif enemigo.HP <= 0:

        entrenador.lista_muertos.append(jugador.lista_equipo[0])  # Meter en la lista de muertos
        entrenador.lista_equipo.pop(0)  # Retirar del equipo de aliado

        # Suma experiencia
        aliado.contador_exp = exp(aliado.contador_exp, aliado.nivel, enemigo.nivel)
        if aliado.contador_exp >= aliado.exp_final:
            aliado.subir_nivel()
            subir_nivel = True

        # Si quedan mas enemigos
        if len(entrenador.lista_equipo) != 0:

            enemigo = entrenador.lista_equipo[0]

            # El combate continua
            return False, False, aliado, enemigo, entrenador, subir_nivel  # El aliado se mantiene y el enemigo pasa a ser el primero de la lista

        # Si no quedan mas enemigos
        else:

            # Gana el combate
            return False, True, aliado, enemigo, entrenador, subir_nivel  # El aliado se mantiene y el entrenador desaparecen
