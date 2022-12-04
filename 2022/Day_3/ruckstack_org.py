min_priorities = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
}
upper_priorities = {
    'A':27,
    'B':28,
    'C':29,
    'D':30,
    'E':31,
    'F':32,
    'G':33,
    'H':34,
    'I':35,
    'J':36,
    'K':37,
    'L':38,
    'M':39,
    'N':40,
    'O':41,
    'P':42,
    'Q':43,
    'R':44,
    'S':45,
    'T':46,
    'U':47,
    'V':48,
    'W':49,
    'X':50,
    'Y':51,
    'Z':52,
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

def calculate_priorities_ruckstack() -> int:
    values = eliminate_space_character()
    priorities_total = 0
    for value in values:
        items = value.strip()
        half = (len(items)//2)
        first_half = items[0:half]
        second_half = items[half:]
        for char in first_half:
            if char in second_half:
                priorities_total +=  min_priorities.get(char) if char in min_priorities else upper_priorities.get(char)
                break
    return priorities_total

def calculate_group_priorities_ruckstack() -> int:
    values = eliminate_space_character()
    priorities_total = 0
    group = []
    for value in values:
        group.append(value)
        if len(group) == 3:
            for char in group[0]:
                if char in group[1] and char in group[2]:
                    priorities_total +=  min_priorities.get(char) if char in min_priorities else upper_priorities.get(char)
                    break
            group = []
    return priorities_total

print("First part sum priorities: " + str(calculate_priorities_ruckstack()))
print("Second part sum priorities: " + str(calculate_group_priorities_ruckstack()))