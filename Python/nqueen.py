def solve_n_queens(n):
    def is_not_under_attack(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or \
                board[prev_row] - prev_row == col - row or \
                board[prev_row] + prev_row == col + row:
                return False
        return True
            
    def place_queens(n, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_not_under_attack(row, col):
                board[row] = col
                place_queens(n, row + 1)
                board[row] = 0

    result = []
    board = [0] * n
    place_queens(n, 0)
    return result

# Example: Get all solutions for 4-queens problem
solutions = solve_n_queens(4)
for sol in solutions:
    for x in sol:
        print('.' * x + 'Q' + '.' * (len(sol) - x - 1))
    print("\n")
