#add import
import question_d

def main():

    end_run = '0'

    while (end_run != 'N'):

        end_run = input("Would you like to know if you number is prime? Y or N: ").upper()

        if(end_run.upper() == 'N'):
            print("Exiting....")
            break
        
        elif(end_run.upper() == 'Y'):
            num = int(input("Enter a number greater than 2: "))
            while (num < 2):
                num = int(input("Enter a number greater than 2: "))

            result = question_d.is_prime(num)

            if (result == True):
                print(f"Your number '{num}' is prime.")
            else:
                print(f"Your number '{num}' is not prime.")

            go_again = '0'

            while (go_again != 'Y'):

                go_again = input("Would you like to go again? Y or N: ").upper()

                if (go_again.upper() == 'Y'):
                    end_run = '0'
                    break
                elif(go_again.upper() == 'N'):
                    print("Exiting...")
                    break
                else:
                    print("Invalid response.")

            if (go_again == 'Y'):
                continue
            else:
                break

        else:
            print("Invalid response.")

main()