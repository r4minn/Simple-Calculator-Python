
print("\033[96m                                   ▄▄\033[96m")
print("\033[96m                                   ██\033[96m")
print("\033[96m▀███▄███ ▄█▀██▄ ▀████████▄█████▄ ▀███ ▀████████▄\033[96m")
print("\033[96m  ██▀ ▀▀██   ██   ██    ██    ██   ██   ██    ██\033[96m")
print("\033[96m  ██     ▄█████   ██    ██    ██   ██   ██    ██\033[96m")
print("\033[96m  ██    ██   ██   ██    ██    ██   ██   ██    ██\033[96m")
print("\033[96m▄████▄  ▀████▀██▄████  ████  ████▄████▄████  ████▄\033[96m")
print("                                                 by ramin")

print("Operators: +, -, /, *, **")
print()

a = float(input("Enter the first number: "))
op = input("Enter operation: ")
b = float(input("Enter the second number: "))


if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    c = (a / b) if b != 0 else print("Can't divide with zero")
    print(c)
elif op == "**":
    print(a ** b)
else:
    print("Invalid operator")

print("")
paa = input("Press ENTER to exit")


