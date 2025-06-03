# bank_atm_simulation.py
transactions = []

def withdrawal(amount, balance):
   
    if amount % 500 != 0 and amount % 1000 != 0:
        return False, "The Withdrawal amount must be a multiple of 500 or 1000 naira."

    
    total_deduction = amount + 100
    
    if amount < 0:
    	print("Error!!")
    	    
    if amount > 0.9 * balance:
        return False, "You Cannot withdraw more than 90% of your balance."

    if balance - total_deduction < 199:
        return False, "Insufficient balance after transaction. Minimum balance of 199 naira must remain."

    return True, "" 

def print_transactions(transaction_history):
    if not transaction_history:
        print("No transactions yet.")
    else: 
        print("\nTransaction Log:")
        for index, value in enumerate(log, start=1):
            print(f"{index}. Withdrawn: ₦{value['withdrawn']}, Fee: ₦{value['transaction_fee']}, Remaining Balance: ₦{value['balance']}")

def main():
    transactions = []
    
    while True:
        try:
            balance_input = input("Enter your account balance (₦): ")
            balance = float(balance_input)
            if balance > 0:
                break
            else:
                print("Initial balance must be a positive number.")
        except ValueError:
            print("Initial balance must be a positive number.")
    
    while True: 
        print(f"\nCurrent Balance: ₦{balance}")
        userInput = input("Do you want to make a withdrawal? (yes/no/view transactions): ").lower()

        if userInput == 'no':
            print("GoodBye!! Have a nice day")
            break
        elif userInput == 'view transactions':
            print_transactions(transactions)
            continue
        elif userInput == 'yes':
            try:
                amount_input = input("Enter amount to withdraw (max ₦20,000): ")
                amount = float(amount_input)
                
                if amount > 20000:
                    print("You can only withdraw a maximum of ₦20,000 per transaction.")
                    continue
                
                valid_transaction, message = withdrawal(amount, balance)
                if not valid_transaction:
                    print(f"Invalid transaction: {message}")
                    continue
                
                transaction_fee = 100
                total = amount + transaction_fee
                
                if total > balance:
                    print("Insufficient balance for this withdrawal and fee.")
                    continue
                
                balance -= total
                transactions.append({
                    "withdrawn": amount,
                    "transaction_fee": transaction_fee,
                    "balance": balance
                })

                print(f"Successfully withdrew ₦{amount}. Fee: ₦{transaction_fee}. Remaining Balance: ₦{balance}")

            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid choice. Please type 'yes', 'no', or 'view transactions'.")

if __name__ == "__main__":
    main()