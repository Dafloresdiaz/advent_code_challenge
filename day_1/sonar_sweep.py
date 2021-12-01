def eliminate_space_character():
    """
    Decription: Function to obtain the values form the txt file, handle the "\n" character at the end of the string
    Return: A list of integer values
    """
    with open("input.txt") as f:
        input = f.readlines()
        for position in range(len(input)):
            input[position] = int(input[position].rstrip("\n"))
    return input

def sonar_sweep():
    """
    Decription: Function to obtain the total count of increments from the input.
                The input is coming from a txt file
    Return: Integer value to know the increments form the input
    """
    values = eliminate_space_character()
    increment_count = 0
    for value in range(len(values)):
            if value != 0:
                if values[value-1] < values[value]:
                    increment_count += 1
    return increment_count
        

print(sonar_sweep())