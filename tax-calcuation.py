income = int(input("Enter your income: "))

tax = 0

if income <= 10000:
    tax = 0.05 * income

elif income > 10000 and income <= 50000:
    tax = 0.1 * income

elif income > 50000 and income <= 100000:
    tax = 0.2 * income

elif income > 100000:
    tax = 0.3 * income


print(f"Tax of ${income} is: {tax}")
