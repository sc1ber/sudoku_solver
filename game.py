def empty(puzzle):
    #scans for an empty slot
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c

    return None, None

def check(puzzle, row, col, guess):
    #checks puzzle

    #checks for duplicate in row
    for r in range(9):
        if puzzle[r][col] == guess:
            return False

    #checks for duplicate in column
    for c in range(9):
        if puzzle[row][c] == guess:
            return False

    #find start of mini box
    rowstart = (row // 3) * 3
    colstart = (col // 3) * 3

    #guess inside the mini box
    for r in range(rowstart, rowstart + 3):
        for c in range(colstart, colstart + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve(puzzle):
    #solves the puzzle

    #initialize empty slot
    row, col = empty(puzzle)

    #if none
    if row is None:
        return True

    #guess number 1-9
    for guess in range(1, 10):
        #check if guess is correct
        if check(puzzle, row, col, guess):
            puzzle[row][col] = guess
            if solve(puzzle):
                return True
        puzzle[row][col] = 0

    return False

def main():
    #initializing puzzle
    puzzle = [
    [ 0, 0, 0, 0, 0, 7, 0, 0, 1],
    [ 0, 7, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 8, 2, 0, 7, 0, 0],
    [ 0, 8, 2, 0, 0, 0, 0, 0, 4],
    [ 0, 0, 0, 0, 1, 3, 0, 0, 9],
    [ 0, 3, 0, 0, 8, 0, 2, 7, 0],
    [ 0, 0, 0, 9, 0, 6, 4, 0, 3],
    [ 0, 0, 9, 0, 0, 0, 0, 5, 0],
    [ 0, 0, 1, 0, 0, 2, 0, 0, 0]
    ]
    solve(puzzle)

    #printing the puzzle
    for r in range(9):
        for c in range(9):
            print(puzzle[r][c], end = " ")
            if c == 8:
                print("")

if __name__ == "__main__":
    main()
