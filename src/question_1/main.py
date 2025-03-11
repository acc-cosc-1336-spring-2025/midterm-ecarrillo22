#add import
import question_a

def main():

    sales_amount = int(input("Enter the sales amount to determine bonus pay: "))

    result = question_a.get_bonus_pay_amount(sales_amount)

    print(f"The bonus pay amount based on ${sales_amount} is ${result}.")

main()