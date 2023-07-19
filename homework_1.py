first = 10
second = 30


# First task


print(first + second)
print(first * second)
print(first - second)
print(first / second)
print(first ** second)
print(first // second)
print(first % second)


# Second task


result = first < second
print("first < second:", result)


result = first > second
print("first > second:", result)


result = first == second
print("first == second:", result)


result = first != second
print("first != second:", result)


# Alternative second task (if we need all results in one variable)


results = [first < second, first > second, first == second, first != second]

for result in results:
    print(result)


# Third task
hello_world_concatenation = "Hello " + "world!"