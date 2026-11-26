
class BankAccount:
    def __init__(
        self,
        owner: str,
        account_type: str,
        balance: float
    ) -> None:
        self.owner = owner
        # Use the setters for validation
        self.account_type = account_type
        self.balance = balance   

    @property
    def account_type(self) -> str:
        return self._account_type

    @account_type.setter
    def account_type(self, new_type: str) -> None:
        valid_types = ["Savings", "Current"]
    
        if new_type in valid_types:
            self._account_type = new_type
        else:
            raise ValueError("Invalid account type!")
    
    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, new_balance: float) -> None:
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            raise ValueError("Balance cannot be negative!")

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")

        self.balance = self.balance + amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")

        if amount > self.balance:
            raise ValueError("Insufficient balance!")

        self.balance = self.balance - amount

    def display_info(self) -> None:
        print(f"Owner: {self.owner}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

#----------------------------------------------------
# Creating an Account
print("=" * 50)
print("ACCOUNT CREATION TEST")
print("=" * 50)
account = BankAccount("Alia", "Savings", 1000)
account.display_info()

# Testing Account Type Property
print("\n" + "=" * 50)
print("ACCOUNT TYPE TEST")
print("=" * 50)
account.account_type = "Current"
print("Updated Account Type:", account.account_type)

try:
    account.account_type = "Business"
except ValueError as error:
    print("Error:", error)
print("Account Type after invalid update:", account.account_type)

# Testing Balance Getter and Setter
print("\n" + "=" * 50)
print("BALANCE PROPERTY TEST")
print("=" * 50)
account.balance = 2000
print("Updated Balance:", account.balance)
try:
    account.balance = -500
except ValueError as error:
    print("Error:", error)

print("Balance after invalid update:", account.balance)

# Testing Deposit
print("\n" + "=" * 50)
print("DEPOSIT TEST")
print("=" * 50)
account.deposit(500)
print("After depositing 500:", account.balance)
try:
    account.deposit(-100)
except ValueError as error:
    print("Error:", error)
print("Balance after invalid deposit:", account.balance)

# Testing Withdraw
print("\n" + "=" * 50)
print("WITHDRAW TEST")
print("=" * 50)
account.withdraw(300)
print("After withdrawing 300:", account.balance)
try:
    account.withdraw(5000)
except ValueError as error:
    print("Error:", error)

try:
    account.withdraw(-100)
except ValueError as error:
    print("Error:", error)

print("Balance after invalid withdrawals:", account.balance)

# Testing Zero Balance
print("\n" + "=" * 50)
print("ZERO BALANCE TEST")
print("=" * 50)

account.withdraw(account.balance)
print("Balance after withdrawing all money:", account.balance)

# Final Account Information
print("\n" + "=" * 50)
print("FINAL ACCOUNT INFORMATION")
print("=" * 50)
account.display_info()

