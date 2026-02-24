class InsufficientBalanceError(Exception):
    pass

balance = 1000
amount = 1500

try:
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")
except InsufficientBalanceError as e:
    print(e)