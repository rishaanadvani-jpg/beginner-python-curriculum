# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
score1 = int(input("Enter the first test score: "))
score2 = int(input("Enter the second test score: "))
if score1 >= 50 and score2 >= 50:
    print("You passed both!")
else:
    print("You failed at least one.")


# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
lunch = input("Did you bring lunch? (yes/no) ")
water = input("Did you bring water? (yes/no) ")
if lunch.lower() == "yes" and water.lower() == "yes":
    print("You're fully ready!")
elif lunch.lower() == "yes" or water.lower() == "yes":
    print("You're somewhat ready.")
else:
    print("You're not ready.")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
input_number = int(input("Enter a number: "))
if input_number < 1 or input_number > 10:
    print("Out of range.")
else:
    print("In range.")


# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
input_score = int(input("Enter a test score (0-100): "))
if input_score >= 90:
    print("A")
elif input_score >= 80:
    print("B")
elif input_score >= 70:
    print("C")
elif input_score >= 60:
    print("D")
else:
    print("F")


# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
input_num1 = int(input("Enter the first number: "))
input_num2 = int(input("Enter the second number: "))
if input_num1 % 5 == 0 and input_num2 % 2 != 0:
    print("Interesting pair!")
else:
    print("Plain pair.")
