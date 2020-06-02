
class Fakemon:
    def __init__(self,nombre,tipo,nivel,exp_final,HP_MAX,ataque,defensa,imagen):
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
        self.nivel +=1
        self.contador_exp = 0
        #Planteamiento principal de subida de estadisticas(1-10)
        if(self.nivel<=10):
            self.HP_MAX *= 1.205
            self.ataque *= 1.23
            self.defensa *= 1.27
            self.HP = self.HP_MAX
            # Falta cuadro de texto indicando que pokemon ha subido de nivel
        #A partir de lvl 10 la suma de estadisticas es distintas(10-40)
        elif(10<self.nivel<=40):
            self.ataque += 3
            self.HP_MAX += 5
            self.defensa +=2
            self.HP = self.HP_MAX
            #Falta cuadro de texto indicando que pokemon ha subido de nivel
        else:
            self.HP = self.HP_MAX
            # Falta cuadro de texto indicando que pokemon ha subido de nivel máximo

