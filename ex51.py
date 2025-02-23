#Tong's 5.1 exercise

num = 0
tot = 0.0

#Introduction
print("\nI can calculate averages.  Enter (done) when you are finished entering numbers.\n")

#Main program
while True:
    sval = input("Enter a number: ")
    exit = sval.lower()
    if exit == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Please enter numbers only.")
        continue
    num = num + 1
    tot = tot + fval

# Prints results
if exit == "done" and num == 0:
   print("\nNo numbers entered. There is no average.")
else:
   print("\nThe total is",tot, "\nThere are",num,"numbers. \nYour average is",tot/num)


