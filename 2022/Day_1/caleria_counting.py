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


def calorie_counting_part_one() -> int:
    """
    Description: Obtain the values from the input and return the elf with the most
    higher value of calories, just the calories.
    """
    values = eliminate_space_character()
    calorie_count = 0
    elf_with_most_calories = 0
    for value in values:
        if value != "":
            calorie_count += int(value)
        else:
            if elf_with_most_calories < calorie_count:
                elf_with_most_calories = calorie_count
            calorie_count = 0
    return elf_with_most_calories

def calorie_top_three_part_two() -> int:
    """
    Description: Obtain the top three values from the input and
    return the total calories form the top three.
    """
    values = eliminate_space_character()
    calorie_count = 0
    elfs_with_most_calories = 0
    elfs_list = []
    for value in values:
        if value != "":
            calorie_count += int(value)
        else:
            elfs_list.append(calorie_count)
            calorie_count = 0
    elfs_list.sort(reverse=True)
    return elfs_list[0] + elfs_list[1] + elfs_list[2]

print("First part value: " + str(calorie_counting_part_one()))
print("Second part value: " + str(calorie_top_three_part_two()))
