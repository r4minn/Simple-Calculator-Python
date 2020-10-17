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

a = float(input("Scrie primul numar: "))
op = input("Operatia dorita: ")
b = float(input("Scrie al doilea numar: "))


if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    c = (a / b) if b != 0 else print("Nu poti impartii la zero")
    print(c)
elif op == "**":
    print(a ** b)
else:
    print("Operatie invalida")

print("")
paa = input("Apasa ENTER pentru a iesi")
