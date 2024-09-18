#BMI Calculator
string1 = input("Enter your weight in (kg): ")
string2 = input("Enter your height in meters (m): ")

w = int(string1)
h = int(string2)

bmi = w/h

print (f"Your BMI is : {bmi}\nyou are healthy?")