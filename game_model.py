import chess

class GameModel:
    player_freeze_time = 20

    def __init__(self):
        self.player = 0
        self.counter = 0
        self.cur_actions = []
        self.started = False
        self.player_freeze = {}

    def init(self, num_boards=1):
        '''
        Initialize game.
        Can initialize with more game boards for more players!
        '''

        self.num_boards = int(num_boards)
        self.board = {}
        self.board_size = [8*num_boards, 8]
        self.last_start = self.counter
        self.num_players = num_boards * 2
        for who, (x, y0, y1) in enumerate([(0, 0, 1), (0, 7, 6), (8, 0, 1), (8, 7, 6)][:self.num_players]):
            for dx, piece in enumerate(chess.first_row):
                p = piece(who, (x+dx, y0), self)
                if piece == chess.King:
                    p.on_die = lambda who=who: self.king_captured(who)
                chess.Pawn(who, (x+dx, y1), self)

    def in_bounds(self, pos):
        for x, s in zip(pos, self.board_size):
            if not (0 <= x < s):
                return False
        return True

    def add_action(self, act_type, *params):
        'Queue an action to be executed'
        self.cur_actions.append((act_type, params))
