import cmd

from TikTacToe import board


class InvalidBoardArgException(Exception):
    pass


class TikTacToeCommand(cmd.Cmd):
    """command processor."""

    def cmdloop(self, intro):
        if not intro:
            raise InvalidBoardArgException
        self._board = intro
        return cmd.Cmd.cmdloop(self, intro)

    def do_draw(self, size):
        """draw [size]
        Draw the tik tac toe board"""
        try:
            self._board.draw(size)
        except board.InvalidSizeArgException:
            print('invalid size !!!')

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    aBoard = board.Board()
    TikTacToeCommand().cmdloop(aBoard)