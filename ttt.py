import turtle

gm = turtle.Screen()
gm.title("Tic Tac Toe")
gm.bgcolor("lightpink")
gm.setup(width=800, height=600)
gm.tracer(0)

def line(start, stop, width, len):
    line = turtle.Turtle()
    line.shape("square")
    line.color("white")
    line.penup()
    line.goto(start, stop)
    line.shapesize(stretch_wid=width, stretch_len=len)


line(-100, 0, 25, .5)
line(100, 0, 25, .5)
line(0, 100, .5, 25)
line(0, -100, .5, 25)


while True:
    gm.update()