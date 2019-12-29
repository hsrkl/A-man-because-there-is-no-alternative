import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score1 = 0
score2 = 0

# Paddle A
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("#00C1FF")
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("#FF1B00")
paddle2.penup()
paddle2.goto(350, 0)
paddle2.shapesize(stretch_wid=5, stretch_len=1)

# Ball
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("#FFDC00")
paddle.penup()
paddle.goto(0, 0)
paddle.dx = 0.1
paddle.dy = -0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("0 - 0", align="center", font=("Courier", 24, "normal"))


# Function
def paddle1up():
    y = paddle1.ycor()
    y += 40
    paddle1.sety(y)


def paddle1down():
    y = paddle1.ycor()
    y -= 40
    paddle1.sety(y)


def paddle2up():
    y = paddle2.ycor()
    y += 40
    paddle2.sety(y)


def paddle2down():
    y = paddle2.ycor()
    y -= 40
    paddle2.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle1up, "w")
wn.onkeypress(paddle1down, "s")
wn.onkeypress(paddle2up, "Up")
wn.onkeypress(paddle2down, "Down")

# Main loop
while True:
    wn.update()

    # move ball

    paddle.setx(paddle.xcor() + paddle.dx)
    paddle.sety(paddle.ycor() + paddle.dy)

    # border checking
    if paddle.ycor() > 290:
        paddle.sety(290)
        paddle.dy *= -1

    if paddle.ycor() < -290:
        paddle.sety(-290)
        paddle.dy *= -1

    if paddle.xcor() > 390:
        paddle.goto(0, 0)
        paddle.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("{} - {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if paddle.xcor() < -390:
        paddle.goto(0, 0)
        paddle.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("{} - {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if paddle1.ycor() > 260:
        paddle1.sety(260)

    if paddle2.ycor() > 260:
        paddle2.sety(260)

    if paddle1.ycor() < -260:
        paddle1.sety(-260)

    if paddle2.ycor() < -260:
        paddle2.sety(-260)

    if 340 < paddle.xcor() < 350 and (paddle2.ycor() + 40 > paddle.ycor() > paddle2.ycor() - 40):
        paddle.setx(340)
        paddle.dx *= -1

    if -340 > paddle.xcor() > -350 and (paddle1.ycor() + 40 > paddle.ycor() > paddle1.ycor() - 40):
        paddle.setx(-340)
        paddle.dx *= -1
