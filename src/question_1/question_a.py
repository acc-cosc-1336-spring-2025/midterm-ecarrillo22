#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_bonus_pay_amount(sales):

    if (sales < 0):
        return "Invalid arguments"
    elif (sales >= 0 and sales <= 499):
        bonus_pay = sales * .05
        return bonus_pay
    elif (sales >= 500 and sales <= 999):
        bonus_pay = sales * .06
        return bonus_pay
    elif (sales >= 1000 and sales <= 1499):
        bonus_pay = sales * .07
        return bonus_pay
    elif (sales >= 1500 and sales <= 1999):
        bonus_pay = sales * .08
        return bonus_pay
    else:
        return "Invalid arguments"
