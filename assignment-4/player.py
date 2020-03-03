import game_rules, random
from copy import deepcopy
###########################################################################
# Explanation of the types:
# The board is represented by a row-major 2D list of characters, 0 indexed
# A point is a tuple of (int, int) representing (row, column)
# A move is a tuple of (point, point) representing (origin, destination)
# A jump is a move of length 2
###########################################################################

# I will treat these like constants even though they aren't
# Also, these values obviously are not real infinity, but close enough for this purpose
NEG_INF = -1000000000
POS_INF = 1000000000

class Player(object):
    """ This is the player interface that is consumed by the GameManager. """
    def __init__(self, symbol): self.symbol = symbol # 'x' or 'o'

    def __str__(self): return str(type(self))

    def selectInitialX(self, board): return (0, 0)
    def selectInitialO(self, board): pass

    def getMove(self, board): pass

    def h1(self, board, symbol):
        return -len(game_rules.getLegalMoves(board, 'o' if self.symbol == 'x' else 'x'))


# This class has been replaced with the code for a deterministic player.
class MinimaxPlayer(Player):
    def __init__(self, symbol, depth):
        super(MinimaxPlayer, self).__init__(symbol)
        self.depth = depth

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    # Edit this one here. :)
    def getMove(self, board):
        legal_moves = game_rules.getLegalMoves(board, self.symbol)
        if len(legal_moves) > 0:
            return self.get_max(board, self.symbol, self.depth)[1]
        else:
            return None

    def get_max(self, board, symbol, depth):
        legal_moves = game_rules.getLegalMoves(board, symbol)

        if depth == 0 or len(legal_moves) == 0:
            result = [self.h1(board, symbol), None]
            return result

        else:
            our_move = None
            max_val = float('-inf')
            for move in legal_moves:
                new_board = game_rules.makeMove(board, move)
                val = self.get_min(new_board, self.opposite_symbol(symbol), depth - 1)[0]
                if val > max_val:
                    max_val = val
                    our_move = move
            result = [max_val, our_move]
            return result

    def get_min(self, board, symbol, depth):
        legal_moves = game_rules.getLegalMoves(board, symbol)

        if depth == 0 or len(legal_moves) == 0:
            result = [self.h1(board, symbol), None]
            return result

        else:
            our_move = None
            min_val = float('inf')
            for move in legal_moves:
                new_board = game_rules.makeMove(board, move)
                val = self.get_max(new_board, self.opposite_symbol(symbol), depth - 1)[0]
                if val < min_val:
                    min_val = val
                    our_move = move
            result = [min_val, our_move]
            return result

    def opposite_symbol(self, symbol):
        if symbol == 'x':
            return 'o'
        else:
            return 'x'

# This class has been replaced with the code for a deterministic player.
class AlphaBetaPlayer(Player):
    def __init__(self, symbol, depth):
        super(AlphaBetaPlayer, self).__init__(symbol)
        self.depth = depth

    # Leave these two functions alone.
    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    # Edit this one here. :)
    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0:
            return self.get_max(board, self.symbol, self.depth, float('-inf'), float('inf') )[1]
        else:
            return None

    def get_max(self, board, symbol, depth, alpha, beta):
        legal_moves = game_rules.getLegalMoves(board, symbol)

        if depth == 0 or len(legal_moves) == 0:
            result = [self.h1(board, symbol), None]
            return result

        else:
            our_move = None
            max_val = float('-inf')
            for move in legal_moves:
                new_board = game_rules.makeMove(board, move)
                val = self.get_min(new_board, self.opposite_symbol(symbol), depth - 1, alpha, beta)[0]
                if val > max_val:
                    max_val = val
                    our_move = move
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    break
            result = [max_val, our_move]
            return result

    def get_min(self, board, symbol, depth, alpha, beta):
        legal_moves = game_rules.getLegalMoves(board, symbol)

        if depth == 0 or len(legal_moves) == 0:
            result = [self.h1(board, symbol), None]
            return result

        else:
            our_move = None
            min_val = float('inf')
            for move in legal_moves:
                new_board = game_rules.makeMove(board, move)
                val = self.get_max(new_board, self.opposite_symbol(symbol), depth - 1, alpha, beta)[0]
                if val < min_val:
                    min_val = val
                    our_move = move
                if val < beta:
                    beta = val
                if alpha >= beta:
                    break
            result = [min_val, our_move]
            return result

    def opposite_symbol(self, symbol):
        if symbol == 'x':
            return 'o'
        else:
            return 'x'


class RandomPlayer(Player):
    def __init__(self, symbol):
        super(RandomPlayer, self).__init__(symbol)

    def selectInitialX(self, board):
        validMoves = game_rules.getFirstMovesForX(board)
        return random.choice(list(validMoves))

    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return random.choice(list(validMoves))

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return random.choice(legalMoves)
        else: return None


class DeterministicPlayer(Player):
    def __init__(self, symbol): super(DeterministicPlayer, self).__init__(symbol)

    def selectInitialX(self, board): return (0,0)
    def selectInitialO(self, board):
        validMoves = game_rules.getFirstMovesForO(board)
        return list(validMoves)[0]

    def getMove(self, board):
        legalMoves = game_rules.getLegalMoves(board, self.symbol)
        if len(legalMoves) > 0: return legalMoves[0]
        else: return None


class HumanPlayer(Player):
    def __init__(self, symbol): super(HumanPlayer, self).__init__(symbol)
    def selectInitialX(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
    def selectInitialO(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')
    def getMove(self, board): raise NotImplementedException('HumanPlayer functionality is handled externally.')


def makePlayer(playerType, symbol, depth=1):
    player = playerType[0].lower()
    if player   == 'h': return HumanPlayer(symbol)
    elif player == 'r': return RandomPlayer(symbol)
    elif player == 'm': return MinimaxPlayer(symbol, depth)
    elif player == 'a': return AlphaBetaPlayer(symbol, depth)
    elif player == 'd': return DeterministicPlayer(symbol)
    else: raise NotImplementedException('Unrecognized player type {}'.format(playerType))

def callMoveFunction(player, board):
    if game_rules.isInitialMove(board): return player.selectInitialX(board) if player.symbol == 'x' else player.selectInitialO(board)
    else: return player.getMove(board)
