# Tong's 6.5 Exercise min_and_max_numbers
#

# Empty list initialized
numbers = []

print("\nWelcome to The Min and Max Program!\n")

#Collects numbers into the list
while True:
    user_input = input("Enter a number or 'done' to end the program: ")

    # Check if the user entered 'done' to break the loop
    exit = user_input.lower()
    if exit == "done":
        break
    try:
        # Convert input to a float and add it to the list
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        # If conversion fails, notify the user and continue the loop
        print("\n INvalid input! Please, enter a number or 'done' to end.\n")


#Check if the list is not empty before calculating the min and max
totlist = len(numbers)
if numbers:
    print("\nA total of", totlist, "numbers were entered.")
    print("\nThe maximum number is: ", max(numbers))
    print("\nThe minimum number is: ", min(numbers))
else:
    print("\nNo numbers were entered.")