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
    """
    Decription: Function to calculate the depth and horizontal position.
    To calculate this, the input has the direction and we need to follow this instructions: 
        - forward X increases the horizontal position by X units.
        - down X increases the depth by X units.
        - up X decreases the depth by X units.
    Return: The product of the horizontal position and depth
    """
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

def calculate_depth_with_aim():
    """
    Decription: Function to calculate the depth and horizontal position.
    To calculate this, the input has the direction and we need to follow this instructions: 
        - down X increases your aim by X units.
        - up X decreases your aim by X units.
        - forward X does two things:
            - It increases your horizontal position by X units.
            - It increases your depth by your aim multiplied by X.
    Return: The product of the horizontal position and depth
    """
    horizontal_position = 0
    depth = 0
    aim = 0
    values = obtain_input()

    for value in values:
        direction_value = value.split(" ")
        if direction_value[0] == 'forward':
            horizontal_position += int(direction_value[1])
            depth += aim * int(direction_value[1])
        elif direction_value[0] == 'down':
            aim += int(direction_value[1])
        elif direction_value[0] == 'up':
            aim -= int(direction_value[1])
    return (horizontal_position * depth)


print(calculate_depth())
print(calculate_depth_with_aim())