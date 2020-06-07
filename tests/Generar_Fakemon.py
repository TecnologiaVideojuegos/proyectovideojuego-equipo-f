import random
import Objeto_Pokemon
import os


def bonificacion(fakemon):
    mejora = random.randint(1, 4)
    desmejora = random.randint(1, 4)
    if (mejora == 1):
        fakemon.ataque += 3
    elif (mejora == 2):
        fakemon.defensa += 3
    elif (mejora == 3):
        fakemon.HP_MAX += random.randint(10, 50)

    if (desmejora == 1):
        fakemon.ataque -= 3
    elif (desmejora == 2):
        fakemon.defensa -= 3
    elif (desmejora == 3):
        fakemon.HP_MAX -= 3
def subir_estadisticas(nivel,HP_MAX,ataque,defensa):
    if nivel <= 10:
        for i in range(1,nivel):
            HP_MAX *= 1.205
            ataque *= 1.23
            defensa *= 1.27
    elif 10<nivel<40:
        for i in range(1,10):
            #Subimos las estadisticas de los primeros 10 niveles
            HP_MAX *= 1.205
            ataque *= 1.23
            defensa *= 1.27
        for i in range(1,nivel-10):
            # Bucle para comprobar como se veran las stats de nivel 11-40
            ataque = ataque + 3  # a partir de nivel 10, las estadisticas suben valores fijos
            vida = vida + 5
            defensa = defensa + 2

"""
Hay que tener cuidado con las diferentes diccionarios fakemon
El diccionario_fakemon esta pensado para colocar el nombre del fakemon y el nombre del png que tiene asociado

Mientras tanto el resto de listas estan ideadas para colocar el nombre del fakemon que debe coincidir con el diccionario fakemon
y el tipo de este.
Para los tipos y sus debilidades/fortalezas consulte el documento datos ordenados tipos en docs  
"""
def nuevo_salvaje(room):
    # Clave(nombre), Contenido(Dirección imagen)
    diccionario_fakemon = {"": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "",
                           "": ""}
    # valores estadisticas bases (lvl 1)
    HP_MAX = random.randint(20,25)  # random 20-25 vida inicial
    ataque = random.randint(8, 10)  # random 8-10 ataque inicial
    defensa = random.randint(3, 4)  # random 3-4 defensa inicial
    # nivel1
    if (room == 4):
        lista_fakemon1 = {"":"", "":"","":""}
        nombre = random.choice(list(lista_fakemon1.keys()))
        tipo = lista_fakemon1[nombre]
        nivel = random.randint(1, 6)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel,0,HP_MAX,ataque,defensa, imagen)
        bonificacion(fakemon)
        return fakemon
    # nivel2
    elif (room == 5):
        lista_fakemon2 = {"":"", "":"","":""}
        nombre = random.choice(list(lista_fakemon2.keys()))
        tipo = lista_fakemon2[nombre]
        nivel = random.randint(6, 12)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel,0,HP_MAX,ataque,defensa, imagen)
        bonificacion(fakemon)
        return fakemon
    # nivel3
    elif (room == 6):
        lista_fakemon3 = {"":"", "":"","":""}
        nombre = random.choice(list(lista_fakemon3.keys()))
        tipo = lista_fakemon3[nombre]
        nivel = random.randint(12, 18)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel,0,HP_MAX,ataque,defensa, imagen)
        bonificacion(fakemon)
        return fakemon
    # nivel4
    elif (room == 7):
        lista_fakemon4 = {"":"", "":"","":""}
        nombre = random.choice(list(lista_fakemon4.keys()))
        tipo = lista_fakemon4[nombre]
        nivel = random.randint(18, 24)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel,0,HP_MAX,ataque,defensa, imagen)
        bonificacion(fakemon)
        return fakemon
    # nivel5
    elif (room == 8):
        lista_fakemon5 = {"":"", "":"","":""}
        nombre = random.choice(list(lista_fakemon5.keys()))
        tipo = lista_fakemon5[nombre]
        nivel = random.randint(24, 30)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel,0,HP_MAX,ataque,defensa, imagen)
        bonificacion(fakemon)
        return fakemon
    # nivel6
    elif (room == 9):
        lista_fakemon6 = {"":"", "":"","":""}
        nombre = random.choice(list(lista_fakemon6.keys()))
        tipo = lista_fakemon6[nombre]
        nivel = random.randint(30, 36)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel,0,HP_MAX,ataque,defensa, imagen)
        bonificacion(fakemon)
        return fakemon
    #nivel7
    elif (room == 10):
        lista_fakemon7 = {"":"", "":"","":""}
        nombre = random.choice(list(lista_fakemon7.keys()))
        tipo = lista_fakemon7[nombre]
        nivel = random.randint(36, 40)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]
        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel,0,HP_MAX,ataque,defensa, imagen)
        bonificacion(fakemon)
        return fakemon
