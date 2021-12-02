def obtain_input():
    """
    Decription: Function to obtain the values form the txt file, handle the "\n" character at the end of the string
    Return: A list of string values
    """
    with open("input.txt") as f:
        input = f.readlines()
        for position in range(len(input)):
            input[position] = input[position].rstrip("\n")
    return input

def calculate_depth():
    horizontal_position = 0
    depth = 0
    values = obtain_input()

    for value in values:
        direction_value = value.split(" ")
        if direction_value[0] == 'forward':
            horizontal_position += int(direction_value[1])
        elif direction_value[0] == 'down':
            depth += int(direction_value[1])
        elif direction_value[0] == 'up':
            depth -= int(direction_value[1])
    
    return (horizontal_position * depth)


print(calculate_depth())