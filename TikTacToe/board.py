class InvalidSizeArgException(Exception):
    pass


class Board(object):

    def __init__(self):
        self._size = None

    def draw(self, size):
        if not size.isdigit():
            raise InvalidSizeArgException
        self._set_size(int(size))
        self._print_board()

    def _set_size(self, size):
        self._size = size

    def _print_board(self):
        even_line = ' ---' * self._size
        odd_line = '|   ' * (self._size + 1)
        row = even_line + '\n' + odd_line + '\n'
        all_rows = row * self._size
        final_row = even_line
        board = all_rows + final_row
        print (board)
