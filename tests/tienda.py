#La definicion de estos objetos esta predefinido en el propio main , su objetivo es que en el pueblo en un espacio asignado aparezca unos cuadros de texto
#para la tienda. En estos cuadros al pulsarse las teclas se llamará a los datos del jugador y al objeto que le corresponda la tecla y hara la transacción pertinente
import Objeto_Entrenador
jugador = Objeto_Entrenador()

class Item():
    def __init__(self,nombre,descripcion,precio):
        #STRING
        self.nombre = nombre
        self.descripcion = descripcion\
        #INT
        self.precio = precio

class Tienda():

    def __init__(self):

        self.item_disponibles = []

    def nuevo_item(self, Item):
        #El item tiene que ser un objeto de la clase Item
        self.item_disponibles.append(Item)

    def comprar(self,dinero,item):
        #Es necesario llamar al objeto jugador para poder realizar este programa
        if(dinero>item.precio):
            #Mostrar un mensaje donde indique le nombre del objeto ha sido comprado
             jugador.inventario[item.nombre]+=1
             jugador.restar_dinero(item.precio)


        #Si no es asi muestra un mensaje donde no se tiene dinero suficiente
















