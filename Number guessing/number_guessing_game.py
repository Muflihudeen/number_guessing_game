import random 

print("Select a difficulty level:")
print("1. Easy (1- 10)")
print("2. Medium (1- 50)")
print("3. Hard (1- 100)")

choice = int(input("Enter your choice (1/2/3):"))
if choice == 1:
    number = random.randint(1, 10)
elif choice == 2:
    number = random.randint(1, 50)
else:
    number = random.randint(1, 100)

attempts = 0 

guess = int(input("Guess the number:"))

while guess != number:
    attempts += 1
    
    if guess < number:
        print("Too low! Try again.")
    else:       
        print("Too high! Try again.")

    guess = int(input("Guess again:"))

attempts += 1 

print("Correct!")

print("You got it in", attempts, "attempts!")
