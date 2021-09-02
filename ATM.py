class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("Your Balance is: $100")

    def cashwithrawal(self, amount):
        new_amount = 100-amount 
        print("You withdrawed: " + str(amount) + " Your remaining balance is: " + str(new_amount))

def main():
        name = input("Hello what is your name?")
        print("Hello, " + name)
        cardnumber = input("Insert your cardnumber: ")
        pin = input("Enter your pin: ")
        new_user = Atm(cardnumber, pin)

        print("Choose your activity")
        print("1. Balance Enquiry")
        print("2. Cash Withdrawal")
        activity = int(input("Enter your activity choice: "))

        if (activity == 1):
            new_user.balanceinquiry()
        elif (activity == 2):
            amount = int(input("Enter the amount: "))
            new_user.cashwithrawal(amount)
        else:
            print("Enter a valid number")

if __name__ == "__main__":
    main()