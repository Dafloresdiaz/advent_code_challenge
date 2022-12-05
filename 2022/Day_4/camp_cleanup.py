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

def ranges_fully_covers() -> int:
    values = eliminate_space_character()
    pairs = 0
    for value in values:
        sections_elf = value.split(",")
        range_areas_first_elf = sections_elf[0].split("-")
        range_areas_second_elf = sections_elf[1].split("-")
        first_area = [area for area in range(int(range_areas_first_elf[0]), int(range_areas_first_elf[1])+1)]
        second_area = [area for area in range(int(range_areas_second_elf[0]), int(range_areas_second_elf[1])+1)]
        check_1 = all(item in first_area for item in second_area)
        check_2 = all(item in second_area for item in first_area)
        if check_1 or check_2:
            pairs += 1
    return pairs

def ranges_overlap() -> int ():
    values = eliminate_space_character()
    pairs_overlap = 0
    for value in values:
        sections_elf = value.split(",")
        range_areas_first_elf = sections_elf[0].split("-")
        range_areas_second_elf = sections_elf[1].split("-")
        first_area = [area for area in range(int(range_areas_first_elf[0]), int(range_areas_first_elf[1])+1)]
        second_area = [area for area in range(int(range_areas_second_elf[0]), int(range_areas_second_elf[1])+1)]
        for area in first_area:
            if area in second_area:
                pairs_overlap += 1
                break

    return pairs_overlap

print("First part pairs: " + str(ranges_fully_covers()))
print("Second part pairs: " + str(ranges_overlap()))