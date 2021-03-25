import turtle

gm = turtle.Screen()
gm.title("Tic Tac Toe")
gm.bgcolor("lightpink")
gm.setup(width=800, height=600)
gm.tracer(0)

player_turn = "x"


class Game():

    def __init__(self):
        self.line(-100, 0, 25, .5)
        self.line(100, 0, 25, .5)
        self.line(0, 100, .5, 25)
        self.line(0, -100, .5, 25)
        self.title()
        self.board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def line(self, start, stop, width, len):
        line = turtle.Turtle()
        line.shape("square")
        line.color("white")
        line.penup()
        line.goto(start, stop)
        line.shapesize(stretch_wid=width, stretch_len=len)

    def title(self):
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Type Spot Number (1-9) to make your move", align="center", font=("Courier", 24, "normal"))


def draw(token):
    if token == "x":
        t = turtle.Turtle()
        t.goto(-50,-50)
        t.goto(50,50)
        t.hideturtle()
        u = turtle.Turtle()
        u.goto(50,-50)
        u.goto(-50,50)
        u.hideturtle()
    else:
        v = turtle.Turtle()
        v.penup()
        v.goto(-180, -250)
        v.pendown()
        v.circle(60)
        v.hideturtle()

def make_move(player_turn):
    draw(player_turn)
    if player_turn == "x":
        player_turn = "o"
    else:
        player_turn = "x"





Game()
make_move("x")
make_move("o")


while True:
    gm.update()