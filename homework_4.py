# Task 1

while True:
    word = input('Enter the word which contains "o": ')
    if len(word.strip()) == 0:
        print("You did not enter any word. Please, try again.")
    elif "o" in word.lower():
        break
    else:
        print("The word should contain letter 'o'. Please, try again.")

print("Great!")

# Task 1 (Alternative way)

while not any("o" in char.lower() for char in input("Please, enter the word which contains 'o':  ")):
    print("The word should contain letter 'o'. Please, try again.")

print("Great!")

# Task 2

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for i in lst1:
    if type(i) == str:
        lst2.append(i)

print(lst2)

# Task 2 (Alternative way)

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [i for i in lst1 if isinstance(i, str)]
print(lst2)

# Task 3

list_of_nums = list(range(100))
sum_of_even_nums = 0
for num in list_of_nums:
    if num % 2 == 0:
        sum_of_even_nums += num

print(sum_of_even_nums)

# Task 3 (Alternative way)

list_of_nums = list(range(100))
sum_of_even_nums = sum(num for num in list_of_nums if num % 2 == 0)
print(sum_of_even_nums)