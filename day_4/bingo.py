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
    total = 0
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
                marked_board = count
                board_number = j
                winner_number = number
                for i, board in enumerate(boards):
                    if i == board_number:
                        normal_winner_board = board
                break
        else:
            continue
        break
    
    #* Print the number of the winner board to know the list of the numbers
    for x in range(5):
        for y in range(5):
            if int(marked_board[x][y]) == 0:
                total += int((normal_winner_board[x][y]))
    print(f"Last Number: {winner_number}, \nBoard: {board_number},\nMarked Numbers:\n{marked_board},\nScore: {total*winner_number}")
            

winner_board()