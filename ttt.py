import turtle


class Board:

    def __init__(self):
        self.line(-100, 0, 25, .5)
        self.line(100, 0, 25, .5)
        self.line(0, 100, .5, 25)
        self.line(0, -100, .5, 25)
        self.title()
        self._board = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]
        self._current_player = "x"

    def get_board(self):
        return self._board

    def get_current_player(self):
        return self._current_player

    def set_current_player(self, new_player):
        self._current_player = new_player

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


class Game:

    def __init__(self):
        self._board = Board()
        self._state = "UNFINISHED"

    def draw(self, token):
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

    def make_move(self, key):
        if self._state != "UNFINISHED":
            return False
        else:
            player_turn = self._board.get_current_player()
            self.draw(player_turn)
            if player_turn == "x":
                self._board.set_current_player("o")
            else:
                self._board.set_current_player("x")
            self.game_won()

    def game_won(self):
        board = self._board.get_board()
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]
        for s in wins:
            if board[s[0]] == board[s[1]] and board[s[1]] == board[s[2]] and board[s[0]] != " ":
                self._state = board[s[0]]



def main():
    gm = turtle.Screen()
    gm.title("Tic Tac Toe")
    gm.bgcolor("lightpink")
    gm.setup(width=800, height=600)
    gm.tracer(0)
    g = Game()
    gm.listen()
    gm.onkeypress(g.make_move(1), "1")
    gm.onkeypress(g.make_move(2), "2")
    gm.onkeypress(g.make_move(3), "3")
    gm.onkeypress(g.make_move(4), "4")
    gm.onkeypress(g.make_move(5), "5")
    gm.onkeypress(g.make_move(6), "6")
    gm.onkeypress(g.make_move(7), "7")
    gm.onkeypress(g.make_move(8), "8")
    gm.onkeypress(g.make_move(9), "9")
    g.game_won()
    while True:
        gm.update()


if __name__ == "__main__":
    main()
