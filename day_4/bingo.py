import numpy as np

def obtain_input():
    """
    Description: Obtain the first line from the obtain, this line represents the bingo numbers.
    Then is to create the list 
    Return: 
    """
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    first_line = [int(n) for n in lines.pop(0).split(',')]
    boards = []
    board = []
    for line in lines[1:]:
        if not line:
            boards.append(board)
            board = []
        else:
            board.append([int(n) for n in line.strip().split()])
            
    boards.append(board)
    return first_line, boards

def winner_board():
    bingo_numbers, boards = obtain_input()
    counts = np.zeros(shape=(len(boards), 5, 5))
    for number in bingo_numbers:
        for i, board in enumerate(boards):
            for y, row in enumerate(board):
                if number in row:
                    index = row.index(number)
                    counts[i][y][index] = 1

        for j, count in enumerate(counts):
            if any(n for n in count.sum(axis=0) == 5) or any(j for j in count.sum(axis=1) == 5):
                break
        else:
            continue
        break
    print(counts)
winner_board()