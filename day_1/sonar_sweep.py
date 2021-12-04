def eliminate_space_character():
    """
    Description: Function to obtain the values form the txt file, handle the "\n" character at the end of the string
    Return: A list of integer values
    """
    with open("input.txt") as f:
        input = f.readlines()
        for position in range(len(input)):
            input[position] = int(input[position].rstrip("\n"))
    return input

def sonar_sweep_part_one(values = None):
    """
    Description: Function to obtain the total count of increments from the input.
                The input is coming from a txt file.
    Return: Integer value to know the increments from the input
    """
    if values is None:
        values = eliminate_space_character()
    increment_count = 0
    for value in range(len(values)):
            if value != 0:
                if values[value-1] < values[value]:
                    increment_count += 1
    return increment_count

def sonar_sweep_part_two():
    """
    Description: Function to obtain the total count of increments, the increments are calculate by 3 values,
                from the input.
                The input is coming from a txt file.
    Return: Integer value to know the increments from the input
    """
    values = eliminate_space_character()
    new_values = []
    increment_count = 0
    for value in range(len(values)):
        if value != (len(values)-2) and value != (len(values)-1):
            value_plus_one = value + 1
            value_plus_two = value + 2
            result = values[value] + values[value_plus_one] + values[value_plus_two]
            new_values.append(result)
    increment_count = sonar_sweep_part_one(new_values)
    return increment_count

print(sonar_sweep_part_one())
print(sonar_sweep_part_two())