class atm(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber,
        self.pinNumber = pinNumber
    def CashWithdrawl(self):
        print("Cash Withdrawl")
    def BalanceEnquiry(self):
        print("Balance Enquiry")
myCard = atm(4167-4949-4234-4657, 321)
print(myCard.CashWithdrawl())
print(myCard.BalanceEnquiry())