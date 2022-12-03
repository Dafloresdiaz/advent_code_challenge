my_hand_values ={
    'X': 1, #rock
    'Y': 2, #paper
    'Z': 3 #scissors
}

my_hand_values_part_two ={
    'X': 0, #lose
    'Y': 3, #draw
    'Z': 6 #win
}

possible_games ={
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

possible_games_part_two ={
    "A X": 3,
    "A Y": 1,
    "A Z": 2,
    "B X": 1,
    "B Y": 2,
    "B Z": 3,
    "C X": 2,
    "C Y": 3,
    "C Z": 1,
}

def eliminate_space_character():
    """
    Description: Function to obtain the values form the txt file, handle the
    "\n" character at the end of the string
    Return: A list of integer values
    """
    with open("input.txt") as f:
        input = f.readlines()
        for position in range(len(input)):
            input[position] = input[position].rstrip("\n")
    return input

def rock_paper_scissors_game_part_one() -> int:
    values = eliminate_space_character()
    total = 0
    for value in values:
        game = value.split()
        my_value = my_hand_values.get(game[1])
        game_value = possible_games.get(value)
        total += my_value + game_value
    return total

def rock_paper_scissors_game_part_two() -> int:
    values = eliminate_space_character()
    total = 0
    for value in values:
        game = value.split()
        my_value = my_hand_values_part_two.get(game[1])
        game_value = possible_games_part_two.get(value)
        total += my_value + game_value
    return total

print("Games total score part one: " + str(rock_paper_scissors_game_part_one()))
print("Games total score two one: " + str(rock_paper_scissors_game_part_two()))