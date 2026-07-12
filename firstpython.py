p = int(input("Principal amount: "))
r = float(input("Rate of interest: "))
t = int(input("Time in years: "))

SI=(p*r*t)/100
Amt = p * (pow((1 + r / 100), t))
CI = Amt - p
print("Amount Generated:", Amt)
print("Compound interest:", CI)
print("Simple interest:", SI)
