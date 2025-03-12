#add import
import question_c

def main():

    play_game = '0'
    
    
    while (play_game != 'N'):
        
        play_game = input("Do you want to play a guessing game? Y or N:").upper()

        if (play_game.upper() == 'N'):
            print("Exiting....")
            break
        
        elif (play_game.upper() == 'Y'):
            print("Guessing game started.")
            number_guess = int(input("Guess a number between 1 and 5: "))
            
            while (number_guess < 1 or number_guess > 5):
                number_guess = int(input("Guess a number between 1 and 5: "))
            
            random_number = question_c.get_random_number()
            while (number_guess != random_number):
                number_guess = int(input("Incorrect guess! Guess again: "))

            if (number_guess == random_number):
                print("You guessed correctly!")
                
            play_again = '0'
            
            while(play_again != 'Y'):
                
                play_again = input("Would you like to try again Y or N?").upper()

                if (play_again.upper() == 'Y'):
                    play_game = '0'
                    break
                elif (play_again.upper() == 'N'):
                    print("Exiting....")
                    break
                else:
                    print("Invalid response")

            if (play_again == 'Y'):
                continue
            else:
                break

        else:
            print("Invalid response.")


main()