class atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
        
    def checkBalance(self):
        print("Your Balance: $5,000")

    def withdrawCash(self, amount):
        new_amount=5000-amount
        print("Your Withdrawn Amount:"+str(amount)+"Your Remaining Amount:"+str(new_amount))

def main():
    card_number=input("Insert Your Card Number:")
    pin_number=input("Enter Your Pin Number:")
    new_user=atm(card_number, pin_number)
    print("Choose Your Activity:")
    print("1. Balance Enquiry 2. Withdraw Cash")
    activity=int(input("Enter The Activity Number:"))
    
    if(activity==1):
        new_user.checkBalance()
    elif(activity==2):
        amount=int(input("Enter the amount you want to withdraw:"))
        new_user.withdrawCash(amount)
    else:
        print("Enter a valid number.")

main()
        

        
        
