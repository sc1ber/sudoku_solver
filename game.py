def solve(puzzle):
    return None

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

    #printing the puzzle
    for r in range(9):
        for c in range(9):
            print(puzzle[r][c], end = " ")
            if c == 8:
                print("")

if __name__ == "__main__":
    main()


