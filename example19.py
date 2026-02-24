lst = [10, 20, 30]

try:
    i = int(input("Enter index: "))
    print(lst[i])
except IndexError:
    print("Index out of range")