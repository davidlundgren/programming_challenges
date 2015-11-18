import collections
import fileinput


def I(operands, board):
    m, n = map(int, operands)
    return [['O' for _ in range(n)] for _ in range(m)]


def C(operands, board):
    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            board[i][j] = 'O'
    return board


def L(operands, board):
    x, y, c = operands
    board[int(x) - 1][int(y) - 1] = c
    return board


def V(operands, board):
    x, y1, y2, c = operands
    for row in range(int(y1) - 1, int(y2)):
        board[row][int(x) - 1] = c
    return board


def H(operands, board):
    x1, x2, y, c = operands
    for col in range(int(x1) - 1, int(x2)):
        board[int(y) - 1][col] = c
    return board


def K(operands, board):
    x1, x2, y1, y2 = map(int, operands[:-1])
    c = operands[-1]
    for row in range(x1 - 1, x2 - 1):
        for col in range(y1 - 1, y2 - 1):
            board[row][col] = c
    return board


def neighbors(x, y, m, n):
    cells = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
    return [(a, b) for a, b in cells if a >= 0 and b >= 0 and a < m and b < n]


def F(operands, board):
    m = len(board)
    n = len(board[0])
    # fill requires BFS from X, Y
    x, y, c = operands
    r_color = board[int(x) - 1][int(y) - 1]
    cell = (int(x) - 1, int(y) - 1)
    r = {cell}
    bag = collections.deque(neighbors(*cell, m, n))
    seen = set()
    while bag:
        visiting = bag.popleft()
        seen.add(visiting)
        u, v = visiting
        try:
            if r_color == board[u][v]:
                r.add(visiting)
                to_visit = [n for n in neighbors(*visiting, m, n) if n not in seen]
                bag.extend(to_visit)
        except IndexError:
            print(u, v)
            raise
    for x, y in r:
        board[x][y] = c
    return board


def S(operands, board):
    file_name = operands[0]
    board_string = '\n'.join(''.join(row) for row in board)
    print(file_name)
    print(board_string)
    return board


def X(operands, board):
    raise StopIteration


OPERATIONS = {'I': I, 'C': C, 'L': L, 'V': V, 'H': H,
              'K': K, 'F': F, 'S': S, 'X': X}


if __name__ == '__main__':
    board = None
    for line in fileinput.input():
        operation, *operands = line.strip().split()

        if operation not in OPERATIONS:
            continue

        try:
            board = OPERATIONS[operation](operands, board)
        except StopIteration:
            break
