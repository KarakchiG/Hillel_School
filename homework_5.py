def processing_arguments(arg1, arg2):
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 * arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):
        return f"{arg1} {arg2}"
        # We can also use arg1 + " " + arg2
    else:
        return arg1, arg2


if __name__ == "__main__":
    result1 = processing_arguments(1, "Hello")
    result2 = processing_arguments("Hello", "World")
    result3 = processing_arguments(5, 6)
    print(f"First result is {result1}, Second result is {result2}, Third result is {result3}")


# Alternative
def processing_args(arg1, arg2):
    operation = (
        (lambda x, y: x * y) if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float))
        else (lambda x, y: f"{arg1} {arg2}") if isinstance(arg1, str) and isinstance(arg2, str)
        else (lambda x, y: (x, y))
    )
    return operation(arg1, arg2)


if __name__ == "__main__":
    result1 = processing_args(1, "Hello")
    result2 = processing_args("Hello", "World")
    result3 = processing_args(5, 6)
    print(f"First result is {result1}, Second result is {result2}, Third result is {result3}")
