def obtain_input() -> (list):
    """
    Description: Read the input fromt the input.txt file and create
    two different lists. These lists will be in order, smallest to largets.
    """
    with open("input.txt") as f:
        input = f.readlines()
        left_numbers = [None] * len(input)
        right_numbers = [None] * len(input)
        for position in range(len(input)):
            numbers = input[position].rstrip("\n").split()
            left_numbers[position] = int(numbers[0])
            right_numbers[position] = int(numbers[1])
    # Part one of the exercise
    #return sorted(left_numbers), sorted(right_numbers)
    return left_numbers, right_numbers

def distance_between_pairs(left_list: list, right_list: list) -> int:
    distance_list = []
    for position in range(len(left_list)):
        distance_list.append(
            abs(left_list[position] - right_list[position])
        )
    print(distance_list)
    return sum(distance_list)

def similarity(left_list: list, right_list: list) -> int:
    number_dic = {}
    similarity_count = 0
    total = 0
    for left_number in left_list:
        if left_number not in number_dic:
            number_dic[left_number] = 0
            for right_number in right_list:
                if left_number == right_number:
                    similarity_count += 1       
            number_dic[left_number] = left_number * similarity_count
            similarity_count = 0
            total += number_dic.get(left_number)
        else:
            total += number_dic.get(left_number)
    return total

if __name__ == "__main__":
    left_numbers, right_numbers = obtain_input()
    #distance_between_pairs(left_list=left_numbers, right_list=right_numbers)
    print(similarity(left_list=left_numbers, right_list=right_numbers))
