class UPIPayument:
    def __init__(self, from_upi_id: str, to_upi_id: str, payer_name: str, reciever_name:str):
        self.from_upi_id = from_upi_id
        self.to_upi_id = to_upi_id
        self.payer_name = payer_name
        self.reciever_name = reciever_name

    def pay(self):
        print(f"payment transactions completed!! \n from user {self.payer_name}-{self.from_upi_id} to {self.reciever_name}-{self.to_upi_id}")

class CardInformation:
    def __init__(self,cardNumber: int, card_holder_name: str, exp_date: str, cvv:int):
        self.cardNumber = cardNumber
        self.card_holder_name = card_holder_name
        self.exp_date = exp_date
        self.cvv = cvv
    
class debitCard(CardInformation):
    def __init__(self,cardNumber: int, card_holder_name: str, exp_date: str, cvv:int):
        super().__init__(cardNumber, card_holder_name, exp_date, cvv)

    def pay(self):
        print(f"payment transactions completed!! - Using {self.card_holder_name}'s Debit card")

class creditCard(CardInformation):
    def __init__(self,cardNumber: int, card_holder_name: str, exp_date: str, cvv:int):
        super().__init__(cardNumber, card_holder_name, exp_date, cvv)

    def pay(self):
        print(f"payment transactions completed!! - Using {self.card_holder_name}'s Credit card")


print("type the curresponding number for your payment:\n 1. UPI \n 2. Credit Card \n 3. Debit Card \n 4. Pay on Delivery \n 5. Cancel order")
user_payment_option = int(input("Enter the number corresponding to the payment Option: "))
if user_payment_option == 1:
    print("you have choosen UPI Payment Option...")
    from_upi_id = input("Enter Your UPI ID: ")
    to_upi_id = input("Enter the UPI ID of the reciever: ")
    payer_name = input("Enter Your Name: ")
    reciever_name = input("Enter the reciever's Name: ")

    upi_payment = UPIPayument(from_upi_id, to_upi_id, payer_name, reciever_name)
    upi_payment.pay()

elif user_payment_option == 2:
    print("you have choosen Credit Card payment Option...")
    cardNumber = input("Enter Your Card Number: ")
    card_holder_name = input("Enter Card holder's Name as mentioned on the card: ")
    exp_date = input("Enter Card expiery date mentioned on the card(format: mm/yy): ")
    cvv = input("Enter your card CVV number: ")

    credit_card_payment = creditCard(cardNumber, card_holder_name, exp_date, cvv)
    credit_card_payment.pay()

elif user_payment_option == 3:
    print("you have choosen Debit Card payment Option...")
    cardNumber = input("Enter Your Card Number: ")
    card_holder_name = input("Enter Card holder's Name as mentioned on the card: ")
    exp_date = input("Enter Card expiery date mentioned on the card(format: mm/yy): ")
    cvv = input("Enter your card CVV number: ")

    debit_card_payment = debitCard(cardNumber, card_holder_name, exp_date, cvv)
    debit_card_payment.pay()
    
elif user_payment_option == 4:
    print ("you have choosen pay on delivery option and hence we will start disbatching the order")

elif user_payment_option == 5:
    print("order cancelled, Please checkout some other products on our application...")

else:
    print("You have not selected the correct option. Please try again by entering the corresponding number of your choise of payment like 1 or 2 ")