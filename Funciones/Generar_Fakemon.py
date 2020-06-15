import random
import os

from Funciones import Objeto_Pokemon


def bonificacion(fakemon):
    """
    Otorga una mejor o desmejora a las estadísticas del fakemon aleatoriamente
    :param fakemon: fakemon a mejorar/desmejorar
    """
    # Se obtienen dos numeros aleatorios entre el 1 y el 4
    mejora = random.randint(1, 4)
    desmejora = random.randint(1, 4)

    # Si es 1 se otorga una mejora al ataque
    if mejora == 1:
        fakemon.ataque += 3

    # Si es 2 se otorga un mejora a la defensa
    elif mejora == 2:
        fakemon.defensa += 3

    # Si es 3 se otorga una mejora a la vida máxima
    elif mejora == 3:
        fakemon.HP_MAX += random.randint(10, 50)
        fakemon.HP = fakemon.HP_MAX

    # Si es 1 se reduce el ataque
    if desmejora == 1:
        fakemon.ataque -= 3

    # Si es 2 se reduce la defensa
    elif desmejora == 2:
        fakemon.defensa -= 3

    # Si es 3 se reduce la vida máxima
    elif desmejora == 3:
        fakemon.HP_MAX -= 3
        fakemon.HP = fakemon.HP_MAX


def subir_estadisticas(nivel, HP_MAX, ataque, defensa):
    """
    Sube las estadísticas del fakemon
    :param nivel: nivel actual del fakemon
    :param HP_MAX: vida máxima actual del fakemon
    :param ataque: ataque actual del fakemon
    :param defensa: defensa actual del fakemon
    """
    #Para niveles 10 o inferior
    if nivel <= 10:
        for i in range(1, nivel):
            HP_MAX *= 1.205
            ataque *= 1.23
            defensa *= 1.27
    #Para nivel entre 10 y 40
    elif 10 < nivel <= 40:
        # Subimos las estadisticas de los primeros 10 niveles
        for i in range(1, 10):
            HP_MAX *= 1.205
            ataque *= 1.23
            defensa *= 1.27
        for i in range(1, nivel - 10):
            ataque = ataque + 3  # a partir de nivel 10, las estadisticas suben valores fijos
            HP_MAX = HP_MAX + 5
            defensa = defensa + 2


def nuevo_salvaje(room):
    """
    Genera fakemons salvajes segun la habitación en la que se encuentra
    :param room: habitación actual
    :return: fakemon generado
    """
    
    # Clave(nombre), Contenido(Dirección imagen)
    diccionario_fakemon = {"Cablanta":"Cablanta", "Cablanta Shiny": "Cablanta Shiny", "Pyro": "Pyro"
        , "Oryp": "Oryp", "Sarzul": "Sarzul", "Sargrey": "Sargrey","Raziel": "Raziel", "Romeu": "Romeu", "Vacivus": "Vacivus",
                            "Fhenou": "Fhenou", "Curmtop": "Curmtop", "Dodkei": "Dodkei"}
    
    # valores estadisticas bases (lvl 1)
    HP_MAX = random.randint(20, 25)  # random 20-25 vida inicial
    ataque = random.randint(8, 10)  # random 8-10 ataque inicial
    defensa = random.randint(3, 4)  # random 3-4 defensa inicial
    
    # nivel1
    if room == 4:
        lista_fakemon1 = {"Cablanta": "estelar", "Sarzul": "estelar"} # Fakemons posibles
        nombre = random.choice(list(lista_fakemon1.keys())) #Se elige aleatoriamente uno
        
        #Se le otorgan estadísticas
        tipo = lista_fakemon1[nombre]
        nivel = random.randint(1, 6)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "enemy" + os.path.sep + diccionario_fakemon[nombre] + ".png"
        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel, 0, HP_MAX, ataque, defensa, imagen)
        bonificacion(fakemon)
        
        #Devuelve el fakemon generado
        return fakemon
    
    # nivel2
    elif room == 5:
        lista_fakemon2 = {"Raziel": "volcanico", "Pyro": "volcanico"} # Fakemons posibles
        nombre = random.choice(list(lista_fakemon2.keys())) #Se elige aleatoriamente uno
        
        # Se le otorgan estadísticas
        tipo = lista_fakemon2[nombre]
        nivel = random.randint(6, 12)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "enemy" + os.path.sep + \
                 diccionario_fakemon[nombre] + ".png"

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel, 0, HP_MAX, ataque, defensa, imagen)
        bonificacion(fakemon)

        # Devuelve el fakemon generado
        return fakemon
    
    # nivel3
    elif room == 6:
        lista_fakemon3 = {"Oryp": "demonio", "Dodkei": "demonio"} # Fakemons posibles
        nombre = random.choice(list(lista_fakemon3.keys())) #Se elige aleatoriamente uno

        # Se le otorgan estadísticas
        tipo = lista_fakemon3[nombre]
        nivel = random.randint(12, 18)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "enemy" + os.path.sep + \
                 diccionario_fakemon[nombre] + ".png"

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel, 0, HP_MAX, ataque, defensa, imagen)
        bonificacion(fakemon)

        # Devuelve el fakemon generado
        return fakemon
    
    # nivel4
    elif room == 7:
        lista_fakemon4 = {"Romeu": "vacio", "Vacivus": "vacio", "Fhenou": "cometa","Curmtop":"cometa"} # Fakemons posibles
        nombre = random.choice(list(lista_fakemon4.keys())) #Se elige aleatoriamente uno

        # Se le otorgan estadísticas
        tipo = lista_fakemon4[nombre]
        nivel = random.randint(18, 24)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "enemy" + os.path.sep + \
                 diccionario_fakemon[nombre] + ".png"

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel, 0, HP_MAX, ataque, defensa, imagen)
        bonificacion(fakemon)

        # Devuelve el fakemon generado
        return fakemon
    
    # nivel5
    elif room == 8:
        lista_fakemon5 = {"Fhenou": "cometa", "Curmtop": "cometa", "Cablanta Shiny": "lunar","Sargrey":"lunar"} # Fakemons posibles
        nombre = random.choice(list(lista_fakemon5.keys())) #Se elige aleatoriamente uno

        # Se le otorgan estadísticas
        tipo = lista_fakemon5[nombre]
        nivel = random.randint(24, 30)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "enemy" + os.path.sep + \
                 diccionario_fakemon[nombre] + ".png"

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel, 0, HP_MAX, ataque, defensa, imagen)
        bonificacion(fakemon)
        return fakemon
    # nivel6
    elif room == 9:
        lista_fakemon6 = {"Sargrey": "lunar", "Cablanta Shiny": "lunar", "Fhenou": "cometa", "Curmtop": "cometa", "Cablanta": "estelar", "Sarzul": "estelar"} # Fakemons posibles
        nombre = random.choice(list(lista_fakemon6.keys())) #Se elige aleatoriamente uno

        # Se le otorgan estadísticas
        tipo = lista_fakemon6[nombre]
        nivel = random.randint(30, 36)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "enemy" + os.path.sep + \
                 diccionario_fakemon[nombre] + ".png"

        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel, 0, HP_MAX, ataque, defensa, imagen)
        bonificacion(fakemon)

        # Devuelve el fakemon generado
        return fakemon
    
    # nivel7
    elif room == 10:
        lista_fakemon7 = {"Cablanta": "estelar", "Sarzul": "estelar", "Pyro": "volcanico"
            , "Raziel": "volcanico", "Oryp": "demonio", "Dodkei": "demonio", "Fhenou": "cometa", "Curmtop": "cometa",
                               "Romeu": "vacio", "Vacivus": "vacio", "Sargrey": "lunar", "Cablanta Shiny": "lunar"} # Fakemons posibles
        nombre = random.choice(list(lista_fakemon7.keys())) #Se elige aleatoriamente uno

        # Se le otorgan estadísticas
        tipo = lista_fakemon7[nombre]
        nivel = random.randint(36, 40)
        subir_estadisticas(nivel, HP_MAX, ataque, defensa)
        imagen = "resources" + os.path.sep + "sprites" + os.path.sep + "fakemon" + os.path.sep + "enemy" + os.path.sep + \
                 diccionario_fakemon[nombre] + ".png"
        fakemon = Objeto_Pokemon.Fakemon(nombre, tipo, nivel, 0, HP_MAX, ataque, defensa, imagen)
        bonificacion(fakemon)

        # Devuelve el fakemon generado
        return fakemon
