def generate_nums(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


for num in generate_nums(10, 20):
    print(num)
