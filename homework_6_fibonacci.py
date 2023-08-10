# Reversed fibonacci sequence

def fibonacci(n, a, b):
    if n > 0:
        fibonacci(n - 1, b, a + b)

        print(a, end=" ")


fibonacci(21, 1, 2)


# Alternative way
def fibonacci(a, b, length, series=[]):
    if len(series) == length:
        series.reverse()
        return series + [1, 0]

    series.append(a + b)
    return fibonacci(b, a + b, length, series)


print(fibonacci(0, 1, 21))
