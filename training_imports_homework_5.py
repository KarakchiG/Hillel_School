from homework_5 import processing_arguments, processing_args

result4 = processing_arguments(2, 3)
print(f"The result is {result4}")

result5 = processing_args(2, 3)
print(f"The result is {result5}")



def process_arguments():
    arg1 = input("Enter the first argument: ")
    arg2 = input("Enter the second argument: ")

    try:
        arg1 = float(arg1)
        arg2 = float(arg2)
        return arg1 * arg2
    except ValueError:
        return f"{arg1} {arg2}"


print(process_arguments())
