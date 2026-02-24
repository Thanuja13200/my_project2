try:
    a = int(input("Enter number1: "))
    b = int(input("Enter number2: "))
    result = a / b
except Exception as e:
    print("Error:", e)
else:
    print("Result:", result)