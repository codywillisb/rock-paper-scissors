# Rock Paper Scissors game (with Big Bang choices!!)

# Import library (to randomise CPU choice)
import random

# Array of all choices available (empty to start)
choices = []

# ----- User Choice Function -----
def get_user_choice(chosen_choices): # only lets user choose choices from respective modes
    prompt_choices = ", ".join(chosen_choices) # puts choices list into a comma separated string variable (for the printed output to user, has no impact on the game's functionality)
    while True:
        user_choice = input("Enter either " + prompt_choices + ": ").lower() # ask for input, convert to lower-case
        if user_choice in chosen_choices: # check if choice is valid
            return user_choice # returns choice & breaks True loop
        else:
            print("You can't create new moves, cheater! Try again.") # prints error msg & user retries, doesn't break True loop

# ----- CPU Choice Function -----
def get_cpu_choice(chosen_choices): # only lets cpu choose choices from chosen mode
    return random.choice(chosen_choices) # randomly chooses an item from the list of choices

# ----- Determines Winner Function -----
def determine_winner(user_choice, cpu_choice):
    if user_choice == cpu_choice: # if both choices are the same
        return "tie"
    
    # Dictionary where each key is a move, and its value is a list of moves it defeats.
    winning_combos = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

    # Decides if user or computer won (if the computer's choice is in the list of moves that the user's choice defeats)
    if cpu_choice in winning_combos[user_choice]:
        return "user"
    else: # if it isn't, cpu wins
        return "cpu"
    
# ----- Main Game Function -----
def start_game():
    print("Let's play Rock, Paper, Scissors (but extra!)")
    # Players scores (to start)
    user_score = 0
    cpu_score = 0

    while True: # main game loop to keep running each round until stopped by user
        while True: # another loop so the break doesn't break the entire main game loop
            # Choose mode "Normal" or "BIG BANG"
            mode = input("Choose your mode: 'normal' or 'big bang' (with lizard, spock): ").lower()
            if mode == "normal":
                choices = ['rock', 'paper', 'scissors'] # choose only normal r/p/s choices
                break # end True loop
            elif mode == "big bang":
                choices = ['rock', 'paper', 'scissors', 'lizard', 'spock'] # choose all choices
                break # end True loop
            else:
                print("There's only two modes, 'normal' or 'big bang'. Please try again (make sure to spell it correctly!)") # error message, user puts in mode again (doesn't break True loop)

        # Print choices, determine and print the winner
        user_choice = get_user_choice(choices)
        cpu_choice = get_cpu_choice(choices)
        result = determine_winner(user_choice, cpu_choice)
        print("You chose: " + user_choice)
        print("Computer chose: " + cpu_choice)

        # Prints who won
        if result == "user":
            print("You win!")
            user_score += 1
        elif result == "cpu":
            print("You lose!")
            cpu_score += 1
        else:
            print("Tie!")

        # Display scores after each round
        print(f"\n--- Score ---")
        print(f"You: {user_score}")
        print(f"Computer: {cpu_score}")
        print(f"---------------")

        # Ask to continue or not
        while True:
            play_again = input("\nDo you want to play another round? (yes/no): ").lower()
            if play_again in ['yes', 'no']: # Check input is yes / no.
                break
            else:
                print("You mispelt (maybe)!. Please enter Yes / No.") # error message & asks user again, does not break True loop

        if play_again == 'no': # End the game / while True loop
            break
    
    print("\nThanks for playing! Here is the final score:")
    print(f"You: {user_score}")
    print(f"Computer: {cpu_score}")

# Checks if the script is being run directly.
if __name__ == "__main__":
    start_game() # if so, game starts!