class Atm(object):

    def __init__(self, card_num, pin_num):
        self.card_num = card_num
        self.pin_num = pin_num
    
    def cash_with_drawl(self, amount):
        print("withdrawing...")
    
    def balance_enquiry(self):
        print("Please wait while we get your balance")
    
    def deposit(self, amount):
        print("Depositing")