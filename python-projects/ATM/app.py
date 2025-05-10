
class ATM :

    def __init__(self):
        self.pin = "9932"
        self.balance = 24000
        self.is_authenticated = False
    
    def check_pin(self, input_pin):
        if input_pin == self.pin:
            self.is_authenticated = True
            print("PIN verified successfully. \n")
        else:
            print("Incorrect PIN")

    def check_balance(self):
        if self.is_authenticated:
            print(f" Current Balance is {self.balance}.\n")
        else:
            print("Please enter the correct PIN \n")

    def deposit(self, amount):
     if self.is_authenticated:
        if amount > 0:
            amount += self.balance
            print(f"Rs {amount:.2f} deposited succssfully.")
            print(f"New Balance is {self.balance:.2f}\n")
        else: 
            print("Deposit must  be positive.\n ")
     else:
        print("Please enter a correct PIN first.\n ")
    
    def withdraw(self, amount):
        if self.is_authenticated:
         if amount <= 0:
            print("withdraw amount must be positively\n")
         elif amount > self.balance:
            print("Insufficient Blance. \n")
         else:
            self.balance -= amount
            print(f" Rs. {amount:.25} withdraw successfully")
            print(f"New balamce Rs. {self.balance:.2f}\n")
        else:
           print("Please enter a right PIN forst ")
    
    def exit(self):

        print(" Thank you for using the ATM. ")
        return False
    
    def menu(self):
       print( "Welcome to the ATM" )
       attempts = 0
       while attempts < 3:
         input_pin =  input("Please enter 4 digit PIN: ")
         if input_pin == self.pin:
            self.is_authenticated = True
            print("PIN varified successfully \n")
            break
         else:
            attempts += 1
            print(f" Incorrect PIN. Attempts left: {3 - attempts} ")
         
       else:
            print(" Too many incorrect attempts. Exiting.")
            return
         
       while True:
            print("ATM MENU")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Please select an option (1-4): ")

            if choice == "1":
               self.check_balance()

            elif choice == "2":
               try:
                  amount = float(input(" Enter amount to deposit: "))
                  self.deposit(amount)
               except ValueError:
                 print("Invalid input. Please enter a numeric value. \n")

            elif choice == "3":
               try:
                  amount = float(input(" Enter amount to withdraw : "))
                  self.withdraw(amount)
               except ValueError:
                  print("Invalid input. Please enter a numeric value. \n")

            elif choice == "4":
               if not self.exit():
                  break
            else:
               print(" Invalid selection. Please choose a valid option \n")
               
if __name__ == "__main__":
   atm = ATM()
   atm.menu()
             

