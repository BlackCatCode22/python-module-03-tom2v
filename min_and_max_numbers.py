# min_and_max_numbers.py
# demo code for Module 03
# dH, 2/13/25, Fresno, CA

print("\n Welcome to The Min and Max Program! \n")

numbers = []

while True:
    # Prompt the user for a number or "done" to end
    user_input = input("\n  Enter a number or 'done' to end the program: ")

    # Check if the user entered 'done' to break the loop
    if user_input == "done":
        break

    try:
        # Convert input to a float and add it to the list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        # If conversion fails, notify the user and continue the loop
        print("\n INvalid input, enter a number or 'done' to end.\n")

#Check if the list is not empty before calculating the min and max
if numbers:
    print("\n The maximum is: ", max(numbers))
    print("\n The minimum is: ", min(numbers))
else:
    print("\n No numbers were entered.")