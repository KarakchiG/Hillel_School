with open("nums and letters.txt", "w") as file:
    file.write("1 2 3 You\n4 5 6 are\n7 8 9 Smart\n")


def calculate_sum_of_nums(filename):
    total_sum = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                numbers = line.split()
                for number in numbers:
                    try:
                        num = float(number)
                        total_sum += num
                    except ValueError:
                        pass
    except FileNotFoundError:
        print("File not found!")

    return total_sum


sum_of_numbers = calculate_sum_of_nums("nums and letters.txt")
print("Total sum is:", sum_of_numbers)
