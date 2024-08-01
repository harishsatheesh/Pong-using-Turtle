import turtle 

left_score = 0
right_score = 0

wn = turtle.Screen() #create a window

wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0) #stops the window from updating, speed up game

#Left Paddle

left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5,stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350,0) 
left_paddle.speed(0)

#right Paddle

right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5,stretch_len=1)
right_paddle.penup()
right_paddle.goto(350,0) 
right_paddle.speed(0)

#ball 
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.speed(0)
ball.dx = 2 
ball.dy = 2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup() 
pen.goto(0,260)
pen.write(f"Left Player: {left_score} | Right Player: {right_score}", align="center",font=("Courier",24,"normal"))

def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20 
    right_paddle.sety(y) 

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20 
    right_paddle.sety(y) 

wn.listen()
wn.onkeypress(left_paddle_up,"w")
wn.onkeypress(left_paddle_down,"s")
wn.onkeypress(right_paddle_up,"Up")
wn.onkeypress(right_paddle_down,"Down")

while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy) 

    #Border checking
    #Top and bottom 
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1

    #left and right
    if ball.xcor()>350:
        ball.goto(0,0)
        ball.dx *= -1 
        left_score+=1 
        pen.clear()
        pen.write(f"Left Player: {left_score} | Right Player: {right_score}", align="center",font=("Courier",24,"normal"))

    
    elif ball.xcor() < -350:
        ball.goto(0,0)
        ball.dx *=-1
        right_score+=1
        pen.clear()
        pen.write(f"Left Player: {left_score} | Right Player: {right_score}", align="center",font=("Courier",24,"normal"))

    if ball.xcor() < -340 and ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50:
        ball.dx *= -1

    if ball.xcor() > 340 and ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50:
        ball.dx *=-1 