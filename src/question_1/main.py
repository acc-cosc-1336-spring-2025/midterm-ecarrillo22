#add import
import question_a

def main():

    sales_amount = int(input("Enter the sales amount to determine bonus pay: "))

    result = question_a.get_bonus_pay_amount(sales_amount)

    if(sales_amount <= -1 or sales_amount >= 2000):
        print(result)
    else:
        print(f"The bonus pay amount based on ${sales_amount} is ${result:.2f}.")

main()