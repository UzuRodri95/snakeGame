import turtle
import time
import random

##########################################################################################
################### CREATION OF THE WINDOW, NAME AND BACKGROUND COLOR ####################
##########################################################################################
ventana = turtle.Screen()
ventana.title("SNAKE v1.0")
ventana.bgcolor("black")
ventana.setup(width=600,height=600)
ventana.tracer(0)

##########################################################################################
################################ HEAD OF THE SNAKE #######################################
##########################################################################################
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

##########################################################################################
#################################### INITIAL FOOD ########################################
##########################################################################################
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

##########################################################################################
################################ BODY OF THE SNAKE #######################################
##########################################################################################
cuerpo = []

##########################################################################################
################################### MARCADORES ###########################################
##########################################################################################
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("SCORE: 0   HIGH SCORE: 0", align = "center", font = ("Courier", 24, "normal"))
score = 0
highScore= 0

##########################################################################################
################################  UTIL FUNCTIONS  ########################################
##########################################################################################
#FUNCTION FOR SNAKE MOVEMENT
def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#SET OF FUNCTION FOR LINKING MOVEMENTS WITH CABEZA DIRECTION
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def derecha():
    cabeza.direction = "right"
def izquierda():
    cabeza.direction = "left"

#LINKING KEYBOARD KEYS WITH SNAKE MOVEMENTS
ventana.listen()
ventana.onkeypress(arriba,"Up")
ventana.onkeypress(abajo,"Down")
ventana.onkeypress(derecha,"Right")
ventana.onkeypress(izquierda,"Left")

#FUNCTION FOR CREATING FOOD IN A RANDOM PLACE
def crearComida():
    x = random.randint(-(ventana.window_width()/2 - 20), ventana.window_width()/2 - 20)
    y = random.randint(-(ventana.window_height()/2 - 20), ventana.window_height()/2 - 20)
    print("COORDENADAS COMIDA " + str(x) + " " + str(y))
    comida.goto(x,y)

#FUNCTION FOR MAKING THE SNAKE GROW
def crecer():
    nuevoSegmento = turtle.Turtle()
    nuevoSegmento.speed(0)
    nuevoSegmento.shape("square")
    nuevoSegmento.color("grey")
    nuevoSegmento.penup()
    cuerpo.append(nuevoSegmento)
    return True

#FUNCTION FOR MAKING SURE THAT THE HEAD SNAKE IS NOT TOUCHING THE EDGES
def comprobarColisionBorde():
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        for item in cuerpo:
            item.goto(2000,2000)
        cuerpo.clear()
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        score = 0
        texto.clear()
        texto.write("SCORE: {}  HIGH SCORE: {}".format(score, highScore), align="center", font=("Courier", 24, "normal"))


def comprobarColisionCuerpo():
    for segmento in cuerpo:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            for item in cuerpo:
                item.goto(2000, 2000)
            cuerpo.clear()
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            score = 0
            texto.clear()
            texto.write("SCORE: {}  HIGH SCORE: {}".format(score, highScore), align="center",
                        font=("Courier", 24, "normal"))

##########################################################################################
##################################### MAIN WHILE  ########################################
##########################################################################################
while True:
    comprobarColisionBorde()
    ventana.update()

    if cabeza.distance(comida) < 20:
        crearComida()
        if crecer():
            score += 10
            if score > highScore:
                highScore = score
            texto.clear()
            texto.write("SCORE: {}  HIGH SCORE: {}".format(score,highScore), align="center", font=("Courier", 24, "normal"))

    totalSegmentos = len(cuerpo)
    for indice in range(totalSegmentos - 1, 0 , -1):
        x = cuerpo[indice - 1].xcor()
        y = cuerpo[indice - 1].ycor()
        cuerpo[indice].goto(x,y)

    if totalSegmentos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x,y)

    movimiento()
    comprobarColisionCuerpo()

    time.sleep(0.1)

#WINDOWS IS OPENED TILL EXIT IS CLICKED
turtle.Screen().exitonclick()