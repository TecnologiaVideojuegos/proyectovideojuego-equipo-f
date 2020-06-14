

class Entrenador:
    """
    Clase entrenador usada para el propio jugador y los entrenadores enemigos. Los enemigos solo usarán las listas fakemon
    """


    def __init__(self, nombre):
        """
        Constructor de la clase Entrenador
        :param nombre: nombre del entrenador o jugador
        """
        # String
        self.nombre = nombre
        # Int
        self.dinero = 200
        # Diccionario String-->Int
        self.inventario = {'Pocion':1,'Cuerda Huida':1}
        # Lista de objetos Pokemon
        self.lista_equipo = []
        self.lista_muertos = []
        self.no_derrotado = True # Variable usada unicamente en entrenadores enemigos para comprobar si han sido derrotados


    def restar_dinero(self, cantidad):
        """
        Resta dinero del jugador al realizar una compra
        :param cantidad: cantidad de dinero a retirar
        """
        self.dinero -= cantidad
        if self.dinero <= 0: self.dinero = 0 # Evita tener dinero negativo


    def nuevo_pokemon(self, pokemon,):
        """
        Añade un nuevo fakemon a la lista
        :param pokemon: fakemon a añadir
        :return: booleano para indicar que la lista esta llena
        """
        self.lista_equipo.append(pokemon)
        if len(self.lista_equipo) >= 4:
            return True
            # En el caso de que nuestra lista de pokemons este llena tendra que aparecer un mensaje en pantalla que explique al jugador que debe
            # o cambiar uno de sus pokemons antiguo por el actual o desechar el actual y seguir con su equipo.
            #Hace falta introducir algo en key press y un centinela


    def nuevo_objeto(self, objeto):
        """
        Añade un nuevo objeto al inventario
        :param objeto: objeto a añadir
        """
        self.inventario[objeto] = self.inventario[objeto]+1
