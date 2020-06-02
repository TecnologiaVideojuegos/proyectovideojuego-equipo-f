def stat_ataque(ataque):
    #multiplicador ataque
    ataque = ataque + (ataque * 0.23)
    
    return ataque

def stat_vida(vida):
    #multiplicador vida
    vida = vida + (vida * 0.205)

    return vida

def stat_defensa(defensa):
    #multiplicador defensa
    defensa = defensa + (defensa * 0.27)

    return defensa

def exp(exp_actual,lvl_aliado,lvl_enemigo):
    #Comprobador de diferencia de niveles entre aliado y enemigo
    dif_nivel = lvl_aliado - lvl_enemigo
    #si nivel aliado es mayor->dara menos exp
    #si nivel aliado es menor->dara mas exp
    #si los niveles son iguales->dara un numero base de exp
    if dif_nivel == 0:
        exp_actual = exp_actual +  8
    elif dif_nivel > 0:
        exp_actual = exp_actual + 5
    elif dif_nivel < 0:
        exp_actual = exp_actual + 13

    return exp_actual

def numeroRandom (lim_inf,lim_sup):
    #funcion para crear un random entero entre dos valores 
    num = random.randint(lim_inf,lim_sup)

    return num
    
#estos valores son provisionales
lvl_maximo = 40     #el level maximo que se puede alcanzar
lvl_aliado = 6      #este level se tiene que ir comprobando a en cada momento, este es un valor ejemplo
lvl_enemigo = 4     #este level se tiene que ir comprobando a en cada momento, este es un valor ejemplo
exp_actual = 0      #exp en cada momento del pokemon
exp_final = 50      #exp que se puede conseguir en cada nivel

#valores estadisticas bases (lvl 1)
vida = numeroRandom(20,25) #random 20-25 vida inicial
ataque = numeroRandom(8,10) #random 8-10 ataque inicial
defensa = numeroRandom(3,4) #random 3-4 defensa inicial

i = 0
for i in range (9):
    #bucle para comprobar como se veran las stats de nivel 1-10
    ataque = stat_ataque(ataque)    #entre nivel 1-10 las estadisticas suben valores proporcionales a las estadisticas del nivel
    vida = stat_vida(vida)
    defensa = stat_defensa(defensa)
    vida_resultado = (ataque - defensa) * 0.5      #calculo en caso de que un bicho ataque a otro y no sea favorecedor,caso practico,fuego ataca a agua
    print("vida:",vida,"ataque:",ataque,"defensa:",defensa)

for i in range (30):
    #bucle para comprobar como se veran las stats de nivel 11-40
    ataque = ataque + 3     #a partir de nivel 10, las estadisticas suben valores fijos
    vida = vida + 5
    defensa = defensa + 2
    print("vida:",vida,"ataque:",ataque,"defensa:",defensa)

exp_actual = exp(exp_actual,lvl_aliado,lvl_enemigo)
print("exp actual:",exp_actual)



