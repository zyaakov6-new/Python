SUMNUM = 0
numbers = []
while True:
    user_input = input("Add number\nType Quit to finish: ")
    if user_input.lower() == 'quit':
        break
    try:
        number = int(user_input)
        SUMNUM += number
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number or 'quit'.")


print(f"The sum is: {SUMNUM}")
