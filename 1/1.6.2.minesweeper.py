import sys


def increment_neighbors(i, j, field):
    field[i - 1][j - 1] += 1 # upper-left
    field[i - 1][j] += 1 # upper
    field[i - 1][j + 1] += 1 # upper-right

    field[i][j - 1] += 1 # left
    field[i][j + 1] += 1 # right

    field[i + 1][j - 1] += 1 # lower-left
    field[i + 1][j] += 1 # lower
    field[i + 1][j + 1] += 1 # lower-right


def minesweeper(board):
    m = len(board)
    n = len(board[0])

    # we add 2 for padding
    field = [[0 for _ in range(n + 2)] for _ in range(m + 2)]

    # calculate counts
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == '*':
                increment_neighbors(i + 1, j + 1, field)

    # insert mines
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == '*':
                field[i + 1][j + 1] = '*'

    # we drop the first and last row and column
    field = [row[1:-1] for row in field[1:-1]]
    return '\n'.join(''.join(map(str, row)) for row in field)


if __name__ == '__main__':
    lines = [line.strip() for line in sys.stdin]
    board_num = 0
    for i, line in enumerate(lines):
        try:
            m, n = map(int, line.split())
        except ValueError:
            continue # skip ahead to next board

        # exit on '0 0' line
        if not m or not n:
            sys.exit(0)

        board_num += 1
        board = lines[i + 1:i + 1 + m]
        print('Field #{}'.format(board_num))
        print(minesweeper(board))
        print()
