import turtle
import random

turtle.Screen().bgcolor("black")
turtle.Screen().title("Yerçekimi Simülatörü")
turtle.Screen().setup(800,600)

topsayısı = int(input("top sayısını yazın:"))
solX = int(input("Sol duvarın x koordinatını yazın:"))
sagX = int(input("Sag duvarın x koordinatını yazın:"))
duvarY = int(input("duvarların y koordinatını yazın:"))
kenar_uzunluğu = int(input("Duvarların uzunluğunu yazın:"))
yansiyan_enerji = float(input("duvarlar enerjinin ne kadarını yansıtıyor?"))

basketball = "basketball.gif"
apple = "apple.gif"
earth = "earth.gif"
beachball = "beachball.gif"

balls = []
gravity = -0.1
shapes = [basketball, earth, beachball, apple]
for shape in shapes:
    turtle.addshape(shape)
colors = ["red","purple","blue","green"]
for i in range(topsayısı):
    balls.append(turtle.Turtle())

for ball in balls:
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors),"green")
    ball.penup()
    ball.goto(random.randint(solX+10,sagX-10),duvarY-10)
    ball.pendown()
    ball.dy = -1
    ball.dx = random.randint(-3,3)

def draw_the_borders(a, solX, sagX, kenar_uzunluğu):
    a.color("blue")
    a.penup()
    a.goto(solX,duvarY)
    a.pendown()
    a.goto(solX,duvarY-kenar_uzunluğu)
    a.goto(sagX,duvarY-kenar_uzunluğu)
    a.goto(sagX,duvarY)
    a.hideturtle()

pen = turtle.Turtle()
draw_the_borders(pen, solX, sagX, kenar_uzunluğu)

while True:
    for ball in balls:
        ball.dy += gravity
        if ball.xcor() > sagX - 10 or ball.xcor() < solX + 10:
            ball.dx *= -1
        if ball.ycor() <= duvarY-kenar_uzunluğu + 10:
            ball.dy *= -yansiyan_enerji
        ball.sety(ball.ycor()+ball.dy)
        ball.setx(ball.xcor()+ball.dx)
    
turtle.Screen().mainloop()
