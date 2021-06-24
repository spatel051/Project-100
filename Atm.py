class Atm(object):
    def __init__(self, card_num, pin_num):
        self.card_num = card_num
        self.pin_num = pin_num
    
    def cash_with_drawl(self, amount):
        print("withdrawing...")
    
    def check_balance(self):
        print("Please wait while we get your balance")

def main():
    card_number = input("Insert your card number:- ")
    pin_number = input("Enter your pin number:- ")
    new_user = Atm(card_num, pin_num)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("Enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number")
main()
