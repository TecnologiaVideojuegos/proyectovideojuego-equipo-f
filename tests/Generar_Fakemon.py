import random
import Objeto_Pokemon;
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


def nuevo_salvaje(room):
    # Clave(nombre), Contenido(Dirección imagen)
    diccionario_fakemon = {"": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "", "": "",
                           "": ""}

    if (room == 1):
        lista_fakemon1 = ["", "", ""]
        nombre = random.choice(lista_fakemon1)
        tipo = ""
        nivel = random.randint(1, 10)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon(nombre, tipo, nivel, 78, 85, 29, imagen)
        bonificacion(fakemon)
        return fakemon

    elif (room == 2):
        lista_fakemon1 = ["", "", ""]
        nombre = random.choice(lista_fakemon1)
        tipo = ""
        nivel = random.randint(10, 20)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon(nombre, tipo, nivel, 78, 85, 29, imagen)
        bonificacion(fakemon)
        return fakemon

    elif (room == 3):
        lista_fakemon1 = ["", "", ""]
        nombre = random.choice(lista_fakemon1)
        tipo = ""
        nivel = random.randint(20, 30)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon(nombre, tipo, nivel, 78, 85, 29, imagen)
        bonificacion(fakemon)
        return fakemon

    elif (room == 4):
        lista_fakemon1 = ["", "", ""]
        nombre = random.choice(lista_fakemon1)
        tipo = ""
        nivel = random.randint(30, 40)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon(nombre, tipo, nivel, 78, 85, 29, imagen)
        bonificacion(fakemon)
        return fakemon

    elif (room == 5):
        lista_fakemon1 = ["", "", ""]
        nombre = random.choice(lista_fakemon1)
        tipo = ""
        nivel = random.randint(1, 10)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon(nombre, tipo, nivel, 78, 85, 29, imagen)
        bonificacion(fakemon)
        return fakemon

    elif (room == 6):
        lista_fakemon1 = ["", "", ""]
        nombre = random.choice(lista_fakemon1)
        tipo = ""
        nivel = random.randint(1, 10)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon(nombre, tipo, nivel, 78, 85, 29, imagen)
        bonificacion(fakemon)
        return fakemon

    elif (room == 7):
        lista_fakemon1 = ["", "", ""]
        nombre = random.choice(lista_fakemon1)
        tipo = ""
        nivel = random.randint(1, 10)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "\enemy" + diccionario_fakemon[nombre]

        fakemon = Objeto_Pokemon(nombre, tipo, nivel, 78, 85, 29, imagen)
        bonificacion(fakemon)
        return fakemon
