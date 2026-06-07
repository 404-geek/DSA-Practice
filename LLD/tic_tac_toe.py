from enum import Enum

class Board_entities(Enum):
    EMPTY = " "
    X = "X"
    O = "O"

class Game_status(Enum):
    IN_PROGRESS = "in_progress"
    X_WINS = "X_wins"
    O_WINS = "O_wins"
    DRAW = "draw"

class Player:

    def __init__(self, name: str, symbol: Board_entities):
        self.name = name
        self.symbol = symbol

class Board:
    
    def __init__(self, size: int = 3):
        self.board = [[Board_entities.EMPTY] * size for _ in range(size)]
        self.size = size

    def _mark(self, r, c, symbol: Board_entities):

        if r < 0 or r >= self.size or c < 0 or c >= self.size:
            raise Exception("invalid cell")

        if self.board[r][c] != Board_entities.EMPTY:
            raise Exception("cell is not empty")
        
        self.board[r][c] = symbol

        if self._check(r, c, symbol):
            return f"{symbol} wins"
        else:
            return "continue"

    def _check(self, r, c, symbol: Board_entities):

        # implements a check of its adjacent cells and see if they are of same symbol

        # check row
        for i in range(self.size):
            if self.board[r][i] != symbol:
                break
        else:
            return True
        
        # check column
        for i in range(self.size):
            if self.board[i][c] != symbol:
                break
        else:
            return True
        
        # check diagonal
        if r == c:
            for i in range(self.size):
                if self.board[i][i] != symbol:
                    break
            else:
                return True
        
        # check anti-diagonal
        if r + c == self.size - 1:
            for i in range(self.size):
                if self.board[i][self.size - 1 - i] != symbol:
                    break
            else:
                return True

        return False

class TicTacToe:

    def __init__(self, player1: Player, player2: Player):
        self.board = Board()
        self.players = [player1, player2]
        self.move_count = 0
        self.current_player = 0
        self.game_status = Game_status.IN_PROGRESS

    def play(self, r, c):

        if self.game_status != Game_status.IN_PROGRESS:
            raise Exception("game is already over")

        current_player = self.players[self.current_player]
        result = self.board._mark(r, c, current_player.symbol)

        if result == "continue":
            self.move_count+=1
            # Switch players
            self.current_player = 1 - self.current_player
        else:
            self.game_status = Game_status.X_WINS if current_player.symbol == Board_entities.X else Game_status.O_WINS
        
        return self.game_status

    def return_status(self):
        return self.game_status.value
    
    def reset_game(self):
        self.board = Board(self.board.size)
        self.move_count = 0
        self.current_player = 0
        self.game_status = Game_status.IN_PROGRESS

    def get_current_player(self):
        return self.players[self.current_player].name


if __name__ == "__main__":
    
    player1 = Player(name="Alice", symbol=Board_entities.X)
    player2 = Player(name="Bob", symbol=Board_entities.O)
    game = TicTacToe(player1, player2)  
    game.play(0, 0)
    print(game.return_status())
    game.play(0, 1)
    print(game.return_status())
    game.play(1, 1)
    print(game.return_status())
    game.play(0, 2)
    print(game.return_status())
    game.play(2, 2)
    print(game.return_status())



        



        
