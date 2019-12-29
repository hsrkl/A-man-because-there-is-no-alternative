import turtle



# Backdrop
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Man
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("green")
paddle1.shapesize(stretch_len=1, stretch_wid=1)
paddle1.penup()
paddle1.goto(0, 0)


# Function
def paddle1up():
    y = paddle1.ycor()
    y += 5
    paddle1.sety(y)


def paddle1down():
    y = paddle1.ycor()
    y -= 5
    paddle1.sety(y)


def paddle2down():
    x = paddle1.ycor()
    x += 5
    paddle1.setx(x)


def paddle3down():
    x = paddle1.ycor()
    x -= 5
    paddle1.setx(x)


wn.listen()
wn.onkeypress(paddle1up, "w")
wn.onkeypress(paddle1down, "s")
wn.onkeypress(paddle2down, "d")
wn.onkeypress(paddle3down, "a")

while True:
    wn.update()
