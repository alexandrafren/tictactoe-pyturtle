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

    def set_board(self, index, player):
        self._board[index] = player

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
        pen.goto(0, 280)
        pen.write("Type Spot Number (1-9) to make your move", align="center", font=("Courier", 24, "normal"))


class Game:

    def __init__(self):
        self._board = Board()
        self._state = "UNFINISHED"

    def game_state(self, spot):
        if self._state != "UNFINISHED":
            return False
        else:
            if self._board.get_board()[spot] == " ":
                return True
            else:
                return False

    def make_move1(self):
        if self.game_state(0):
            player_turn = self._board.get_current_player()
            self._board.set_board(0, player_turn)
            t = turtle.Turtle()
            if player_turn == "x":
                t.shape("purplecross.gif")
                self._board.set_current_player("o")
            else:
                t.shape("purplecircle.gif")
                self._board.set_current_player("x")
            t.penup()
            t.goto(-180, 180)
            self.game_won()
        else:
            return False

    def make_move2(self):
        if self.game_state(1):
            player_turn = self._board.get_current_player()
            self._board.set_board(1, player_turn)
            t = turtle.Turtle()
            if player_turn == "x":
                t.shape("purplecross.gif")
                self._board.set_current_player("o")
            else:
                t.shape("purplecircle.gif")
                self._board.set_current_player("x")
            t.penup()
            t.goto(0, 180)
            self.game_won()
        else:
            return False

    def make_move3(self):
        if self.game_state(2):
            player_turn = self._board.get_current_player()
            self._board.set_board(2, player_turn)
            t = turtle.Turtle()
            if player_turn == "x":
                t.shape("purplecross.gif")
                self._board.set_current_player("o")
            else:
                t.shape("purplecircle.gif")
                self._board.set_current_player("x")
            t.penup()
            t.goto(180, 180)
            self.game_won()
        else:
            return False

    def make_move4(self):
        if self.game_state(3):
            player_turn = self._board.get_current_player()
            self._board.set_board(3, player_turn)
            t = turtle.Turtle()
            if player_turn == "x":
                t.shape("purplecross.gif")
                self._board.set_current_player("o")
            else:
                t.shape("purplecircle.gif")
                self._board.set_current_player("x")
            t.penup()
            t.goto(-180, 0)
            self.game_won()
        else:
            return False

    def make_move5(self):
        if self.game_state(4):
            player_turn = self._board.get_current_player()
            self._board.set_board(4, player_turn)
            t = turtle.Turtle()
            if player_turn == "x":
                t.shape("purplecross.gif")
                self._board.set_current_player("o")
            else:
                t.shape("purplecircle.gif")
                self._board.set_current_player("x")
            t.penup()
            t.goto(0, 0)
            self.game_won()
        else:
            return False

    def make_move6(self):
        if self.game_state(5):
            player_turn = self._board.get_current_player()
            self._board.set_board(5, player_turn)
            t = turtle.Turtle()
            if player_turn == "x":
                t.shape("purplecross.gif")
                self._board.set_current_player("o")
            else:
                t.shape("purplecircle.gif")
                self._board.set_current_player("x")
            t.penup()
            t.goto(180, 0)
            self.game_won()
        else:
            return False

    def make_move7(self):
        if self.game_state(6):
            player_turn = self._board.get_current_player()
            self._board.set_board(6, player_turn)
            t = turtle.Turtle()
            if player_turn == "x":
                t.shape("purplecross.gif")
                self._board.set_current_player("o")
            else:
                t.shape("purplecircle.gif")
                self._board.set_current_player("x")
            t.penup()
            t.goto(-180, -180)
            self.game_won()
        else:
            return False

    def make_move8(self):
        if self.game_state(7):
            player_turn = self._board.get_current_player()
            self._board.set_board(7, player_turn)
            t = turtle.Turtle()
            if player_turn == "x":
                t.shape("purplecross.gif")
                self._board.set_current_player("o")
            else:
                t.shape("purplecircle.gif")
                self._board.set_current_player("x")
            t.penup()
            t.goto(0, -180)
            self.game_won()
        else:
            return False

    def make_move9(self):
        if self.game_state(8):
            player_turn = self._board.get_current_player()
            self._board.set_board(8, player_turn)
            t = turtle.Turtle()
            if player_turn == "x":
                t.shape("purplecross.gif")
                self._board.set_current_player("o")
            else:
                t.shape("purplecircle.gif")
                self._board.set_current_player("x")
            t.penup()
            t.goto(180, -180)
            self.game_won()
        else:
            return False

    def game_won(self):
        board = self._board.get_board()
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]
        for s in wins:
            if board[s[0]] == board[s[1]] and board[s[1]] == board[s[2]] and board[s[0]] != " ":
                self._state = board[s[0]]
                pw = turtle.Turtle()
                pw.speed(0)
                pw.color("white")
                pw.penup()
                pw.hideturtle()
                pw.goto(0, -280)
                pw.write("Player {} won!".format(board[s[0]]), align="center", font=("Courier", 24, "normal"))



def main():
    gm = turtle.Screen()
    gm.title("Tic Tac Toe")
    gm.bgcolor("pink")
    gm.setup(width=800, height=650)
    gm.tracer(0)
    gm.register_shape("purplecross.gif")
    gm.register_shape("purplecircle.gif")
    g = Game()
    gm.onkeyrelease(g.make_move1, 1)
    gm.onkeyrelease(g.make_move2, 2)
    gm.onkeyrelease(g.make_move3, 3)
    gm.onkeyrelease(g.make_move4, 4)
    gm.onkeyrelease(g.make_move5, 5)
    gm.onkeyrelease(g.make_move6, 6)
    gm.onkeyrelease(g.make_move7, 7)
    gm.onkeyrelease(g.make_move8, 8)
    gm.onkeyrelease(g.make_move9, 9)
    gm.listen()

    while True:
        gm.update()

if __name__ == "__main__":
    main()


