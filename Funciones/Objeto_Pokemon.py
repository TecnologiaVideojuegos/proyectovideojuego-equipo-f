
class Fakemon:
    """
    Clase fakemon usada para enemigos y aliados
    """
    def __init__(self, nombre, tipo, nivel, exp_final, HP_MAX, ataque, defensa, imagen):
        """
        Constructor de la clase Fakemon donde se asignan todos sus atributos
        :param nombre: nombre del fakemon
        :param tipo: tipo del fakemon
        :param nivel: nivel del fakemom
        :param exp_final: experiencia necesaria para subir de nivel
        :param HP_MAX: vida maxima del fakemon
        :param ataque: ataque del fakemon
        :param defensa: defensa del fakemon
        :param imagen: sprite asociado
        """
        #Constructor
        # String
        self.nombre = nombre
        self.tipo = tipo
        #Puntos de experiencia INT
        self.nivel = nivel
        self.contador_exp = 0
        self.exp_final = exp_final
        #Puntos de vida INT
        self.HP_MAX = HP_MAX
        self.HP = HP_MAX
        #Estadisticas daño y defensa INT
        self.ataque = ataque
        self.defensa = defensa
        #String con el enlace al tipo de imagen del fakemon
        self.imagen = imagen


    def subir_nivel(self):
        """
        Sube las estadísticas del fakemon junto a su nivel
        :return: 
        """
        self.nivel += 1
        self.contador_exp = 0
        #Planteamiento principal de subida de estadisticas(1-10)
        if self.nivel<=10:
            self.HP_MAX = int(self.HP_MAX*1.205)
            self.ataque = int(self.ataque*1.23)
            self.defensa = int(self.defensa*1.27)
            self.HP = self.HP_MAX
            self.exp_final += 10
        #A partir de lvl 10 la suma de estadisticas es distintas(10-40)
        elif 10<self.nivel<=40:
            self.ataque += 3
            self.HP_MAX += 5
            self.defensa +=2
            self.HP = self.HP_MAX
            self.exp_final += 30
