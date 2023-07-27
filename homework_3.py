# Using if/else statements and set() function

user_string = input("Please, enter your string here: ")
unique_characters = set(user_string)

if len(unique_characters) > 10:
    print(True)
else:
    print(False)


# Alternative one-liner

print(len(set(input("Please, enter your string here: "))) > 10)