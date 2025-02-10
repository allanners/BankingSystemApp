# Domain Layer - consists of the entities representing domain concepts

class Account:
    def __init__(self, account_id, customer_id, account_number, balance=0.0):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, customer_id, name, email, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number


# Use Case Layer - business logic of the application

class CreateAccount:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def create_account(self, customer_id, name, email, phone_number):
        # Create a new customer
        customer = Customer(customer_id, name, email, phone_number)
        
        # Create a new account
        account_id = len(self.account_repository.accounts) + 1  # generates ID based on the number of existing accounts
        account_number = f"ACCT-{account_id:05d}" # generates an account number in the format "ACCT-00001"
        new_account = Account(account_id, customer.customer_id, account_number)

        # Save account to repository
        self.account_repository.save_account(new_account)
        return new_account


class MakeTransaction:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def make_transaction(self, account_id, amount, transaction_type):
        account = self.account_repository.find_account_by_id(account_id)
        if transaction_type == 'deposit':
            account.deposit(amount)
        elif transaction_type == 'withdraw':
            account.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type. Use 'deposit' or 'withdraw'.")
        return account.get_balance()


class GenerateAccountStatement:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def generate_account_statement(self, account_id):
        account = self.account_repository.find_account_by_id(account_id)
        statement = f"Account ID: {account.account_id}\n" \
                    f"Account Number: {account.account_number}\n" \
                    f"Balance: {account.get_balance()}\n"
        return statement


# Infrastructure Layer

class AccountRepository:
    def __init__(self):
        self.accounts = []

    def save_account(self, account):
        self.accounts.append(account)

    def find_account_by_id(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account
        raise ValueError("Account not found.")

    def find_accounts_by_customer_id(self, customer_id):
        return [account for account in self.accounts if account.customer_id == customer_id]


# Test Scenario

def main():
    # Create an account repository
    account_repository = AccountRepository()

    # Create use case instances
    create_account_use_case = CreateAccount(account_repository)
    make_transaction_use_case = MakeTransaction(account_repository)
    generate_statement_use_case = GenerateAccountStatement(account_repository)

    # Create a new account
    new_account = create_account_use_case.create_account(
        customer_id=1, 
        name="Juan Dela Cruz", 
        email="juandelacruz@example.com", 
        phone_number="09561543429"
    )
    print(f"Created Account: {new_account.account_number} with initial balance: {new_account.get_balance()}")

    # Make a deposit
    new_balance = make_transaction_use_case.make_transaction(new_account.account_id, 100.0, 'deposit')
    print(f"New Balance after deposit: {new_balance}")

    # Make a withdrawal
    new_balance = make_transaction_use_case.make_transaction(new_account.account_id, 50.0, 'withdraw')
    print(f"New Balance after withdrawal: {new_balance}")

    # Generate account statement
    statement = generate_statement_use_case.generate_account_statement(new_account.account_id)
    print("Account Statement:")
    print(statement)

if __name__ == "__main__":
    main()