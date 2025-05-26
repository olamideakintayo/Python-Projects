accounts = []

def create_account(name, phone, balance):
    if not name:
        raise ValueError("Name cannot be empty.")
    if not phone.isdigit():
        raise ValueError("Phone must contain digits only.")
    try:
        balance = float(balance)
    except ValueError:
        raise ValueError("Balance must be a valid number.")
    if balance < 0.0:
        raise ValueError("Balance cannot be negative.")
    
    account = {"name": name, "phone": phone, "balance": balance}
    accounts.append(account)
    return "account"

def deposit(phone, amount):
    amount = float(amount)
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.")

    for account in accounts:
        if account["phone"] == phone:
            account["balance"] += amount
            return account["balance"]

    raise ValueError("Account with this phone number not found.")

def withdraw(phone, amount):
    amount = float(amount)
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")

    for account in accounts:
        if account["phone"] == phone:
            if account["balance"] < amount:
                raise ValueError("Insufficient funds.")
            account["balance"] -= amount
            return account["balance"]

    raise ValueError("Account with this phone number not found.")

def get_all_accounts():
    return accounts

def find_account_by_phone(phone):
    for account in accounts:
        if account["phone"] == phone:
            return account
    raise ValueError("Account with this phone number not found.")
