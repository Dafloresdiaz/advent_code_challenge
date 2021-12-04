from collections import Counter

def obtain_input():
    """
    Description: Function to obtain the values form the txt file, handle the "\n" character at the end of the string
    Return: A list of string values
    """
    with open("input.txt") as f:
        input = f.readlines()
        for position in range(len(input)):
            input[position] = input[position].rstrip("\n")
    return input

def obtain_input_vertical(input = None):
    """
    Description: Function to obtain the values in vertical order
    Return: A list of values in vertical
    """
    count_char = 0
    gama_rate_bits = ""
    bits_vertical = []
    if input is None:
        input = obtain_input()
    while count_char < len(input[0]):
        for value in input:
            gama_rate_bits += value[count_char]
        bits_vertical.append(gama_rate_bits)
        gama_rate_bits = ""
        count_char += 1

    return bits_vertical

def obtain_common_and_least_common():
    """
    Description: Function to obtain the gamma and the epsilon by using the max and min values from the values
    Return: The product of gamma_rate and epsilon_rate
    """
    values = obtain_input_vertical(None)
    gamma_rate_bits = ""
    epsilon_rate_bits = ""
    for value in values:
        bit = Counter(value)
        gamma_rate_bits += max(bit, key=bit.get)
        epsilon_rate_bits += min(bit, key=bit.get)
    power_consuption  = int(gamma_rate_bits,2) * int(epsilon_rate_bits, 2)
    return power_consuption


def obtain_oxygen_or_cotwo(vertical_values, normal_values, change_bit = 0, mood = "most"):
    """
    Description: Function to obtain the oxygen ussing the different bit criteria
    Return: A list with the last value and change it to decimal
    """
    bit = Counter(vertical_values[0])
    max_value = max(bit, key=bit.get)
    min_value = min(bit, key=bit.get)
    value = '0' if max_value == min_value else min_value

    if mood == "most":
        value = '1' if max_value == min_value else max_value
    bits_reduction = []
    for value_string in normal_values:
        if value_string[change_bit] == value:
            bits_reduction.append(value_string)
    if len(bits_reduction) == 1:
        print(int(bits_reduction[0], 2))
    else:
        change_bit += 1
        mood = 'least' if mood == "least" else "most"
        obtain_oxygen_or_cotwo([obtain_input_vertical(bits_reduction)[change_bit]], bits_reduction, change_bit, mood)

print(obtain_common_and_least_common())
vertical_values = [obtain_input_vertical(None)[0]]
normal_values = obtain_input()
obtain_oxygen_or_cotwo(vertical_values, normal_values, 0)
print("-------------")
mood = 'least'
obtain_oxygen_or_cotwo(vertical_values, normal_values,0, mood)