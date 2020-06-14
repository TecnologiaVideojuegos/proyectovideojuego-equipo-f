import Objeto_Entrenador

jugador = Objeto_Entrenador()

"""
La definicion de estos objetos esta predefinido en el propio main , su objetivo es que en el pueblo en un espacio asignado aparezca unos cuadros de texto
para la tienda. En estos cuadros al pulsarse las teclas se llamará a los datos del jugador y al objeto que le corresponda la tecla y hara la transacción pertinente
"""


class Item:
    """
    Clase objeto
    """
    def __init__(self,nombre,descripcion,precio):
        """
        Constructor
        :param nombre: nombre del objeto
        :param descripcion: descripción del objeto
        :param precio: precio del objeto
        """
        #STRING
        self.nombre = nombre
        self.descripcion = descripcion\
        #INT
        self.precio = precio


class Tienda:
    """
    Clase tienda
    """

    def __init__(self):
        """
        Cosntructor
        """

        self.item_disponibles = []


    def nuevo_item(self, Item):
        """
        Añade un nuevo objeto
        :param Item: objeto a añadir
        """
        #El item tiene que ser un objeto de la clase Item
        self.item_disponibles.append(Item)


    def comprar(self, dinero, item):
        """
        Compra un objeto de la tienda
        :param dinero: dinero disponible
        :param item: objeto que se quiere comprar
        :return: 
        """
        
        #Es necesario llamar al objeto jugador para poder realizar este programa
        if dinero>item.precio:
            #Mostrar un mensaje donde indique le nombre del objeto ha sido comprado
             jugador.inventario[item.nombre]+=1
             jugador.restar_dinero(item.precio)

