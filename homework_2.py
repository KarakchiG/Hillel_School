# Validate user input using isalpha() and isspace() methods.

while True:

    user_word = input("Please, enter your word here: ")
    if user_word.isalpha() and not user_word.isspace():
        break
    print("Invalid input. Please try again.")

print(f"Word '{user_word}' has {len(user_word)} letters.")


"""
Alternative. Validate using isalpha() and strip() methods. And a little more information for the user about his 
invalid input.
"""


while True:

    user_word = input("Please, enter your word here: ")

    if not user_word.strip():
        print("You didn't enter any word. Try again, please.")
        continue

    if not user_word.isalpha():
        print("The word should contain only letters. Try again, please")
        continue

    break

print(f"Word '{user_word}' has {len(user_word)} letters.")


"""
We can also import a library (like nltk) to check if it is a real word (to avoid a case when user input contains 
two or more words without spaces). 
"""