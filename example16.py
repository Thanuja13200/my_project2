try:
    f = open("sample.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    f.close()
    print("File closed")