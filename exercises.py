# exercise 1 Vowel or Consonant

def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()
    vowels = 'aeiou'
    
    if letter.isalpha():
        if letter in vowels:
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetical character.")
    

# Call the function to test
check_letter()

# Exercise 2: Old enough to vote?

def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        else:
            voting_age = 18
            if age >= voting_age:
                print("You are eligible to vote.")
            else:
                print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

# Call the function to test
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
def calculate_dog_years():
    try:
        dog_age = int(input("Input a dog's age: "))
        if dog_age < 0:
            print("Age cannot be negative.")
        else:
            if dog_age <= 2:
                dog_years = dog_age * 10
            else:
                dog_years = 20 + (dog_age - 2) * 7
            print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")

# Call the function to test
calculate_dog_years()

# Exercise 4: Weather Advice
def weather_advice():
    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()

    if cold == 'yes' and raining == 'yes':
        print("Wear a waterproof coat.")
    elif cold == 'yes' and raining == 'no':
        print("Wear a warm coat.")
    elif cold == 'no' and raining == 'yes':
        print("Carry an umbrella.")
    elif cold == 'no' and raining == 'no':
        print("Wear light clothing.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# Call the function to test
weather_advice()

# Exercise 5: What's the Season?
def determine_season():
    # Your control flow logic goes here
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    date = int(input("Enter the day of the month: ").strip())
    if (month == "Dec" and date >= 21) or (month in ["Jan", "Feb"]) or (month == "Mar" and date <= 19):
        season = "Winter"

    elif (month == "Mar" and date >= 20) or (month in ["Apr", "May"]) or (month == "Jun" and date <= 20):
        season = "Spring"

    elif (month == "Jun" and date >= 21) or (month in ["Jul", "Aug"]) or (month == "Sep" and date <= 21):
        season = "Summer"

    elif (month == "Sep" and date >= 22) or (month in ["Oct", "Nov"]) or (month == "Dec" and date <= 20):
        season = "Fall"

    else:
        print("Invalid input. Please check your input.")
        return

    print(f"{month} {date} is in {season}.")

# Call the function
determine_season()

# Exercise 6: Number Guessing Game

def guess_number():
    # Set the target number
    target = 42
    
    # Inform the user about the game
    print("Guess the number between 1 and 100. You have 5 attempts.")
    
    # Allow up to 5 guesses
    for attempt in range(1, 6):
        # Prompt the user for a guess
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        # Check the guess and provide feedback
        if guess == target:
            print("Congratulations, you guessed correctly!")
            return
        elif guess < target:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        # Notify the user if it's their last chance
        if attempt == 5:
            print("Last chance!")
    
    # If the loop completes without a correct guess
    print("Sorry, you failed to guess the number in five attempts.")

# Call the function
guess_number()