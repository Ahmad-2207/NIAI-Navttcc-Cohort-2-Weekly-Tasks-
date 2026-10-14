# Task 27: Exercises on user defined exception handling

# 1. A simple custom exception
class NegativeNumberError(Exception):
    """Raised when a negative number is not allowed."""

def square_root(x):
    if x < 0:
        raise NegativeNumberError(f"Cannot take square root of {x}")
    return x ** 0.5

try:
    print(square_root(16))
    print(square_root(-4))
except NegativeNumberError as e:
    print("Custom error caught:", e)

# 2. Custom exception with extra data (guessing game from the Programiz tutorial)
class ValueTooSmallError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

secret = 10
for guess in [4, 15, 10]:
    try:
        if guess < secret:
            raise ValueTooSmallError
        elif guess > secret:
            raise ValueTooLargeError
        print(f"{guess} is correct!")
    except ValueTooSmallError:
        print(f"{guess} is too small, try again")
    except ValueTooLargeError:
        print(f"{guess} is too large, try again")

# 3. Customising the error message and attributes
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is not enough to withdraw {amount}")

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount
        return self.balance

account = BankAccount(500)
try:
    account.withdraw(200)
    print("Remaining:", account.balance)
    account.withdraw(900)
except InsufficientBalanceError as e:
    print("Error:", e)
    print("Short by:", e.amount - e.balance)

# 4. Exception hierarchy: catch a family of errors with the base class
class AppError(Exception):
    pass

class DatabaseError(AppError):
    pass

class NetworkError(AppError):
    pass

for err in (DatabaseError("db down"), NetworkError("no wifi")):
    try:
        raise err
    except AppError as e:
        print(type(e).__name__, "->", e)
