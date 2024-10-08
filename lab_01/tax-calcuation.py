def calculate_tax(income):
    if income <= 10000:
        tax = income * 0.05
    elif income <= 50000:
        tax = (10000 * 0.05) + ((income - 10000) * 0.10)
    elif income <= 100000:
        tax = (10000 * 0.05) + (40000 * 0.10) + ((income - 50000) * 0.20)
    else:
        tax = (10000 * 0.05) + (40000 * 0.10) + (50000 * 0.20) + ((income - 100000) * 0.30)
    
    return tax

income = float(input("Enter your income: "))
tax = calculate_tax(income)

print(f"The total tax amount an income of ${income} is: ${tax:.2f}")



