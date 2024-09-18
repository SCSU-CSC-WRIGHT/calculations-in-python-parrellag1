#Simple Interest Rate Claculator
string1 = input("Enter the principal amount: ")
string2 = input("Enter the interest rate: ")
string3 = input("Enter the time period (in years): ")

p = int(string1)
r = int(string2)
t = int(string3)

intrate = p*r*t/100

print(f"Your simple interest is: {intrate}")