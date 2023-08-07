# https://colab.research.google.com/drive/11cB94tJnMGuQ2NWtsAk5A5aYS1kJVWtj?usp=sharing

import math

def calculate_annuity(principal, rate, time, continuous=False):
    if continuous:
        return principal * math.exp(rate * time)
    else:
        return principal * ((1 + rate) ** time)

def calculate_monthly_payment(principal, rate, time):
    monthly_rate = rate / 12
    num_payments = time * 12
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
    return monthly_payment

def estimate_retirement_balance(principal, rate, time):
    return principal * (1 + rate) ** time

def time_to_double(principal, rate):
    if rate <= 0:
        return float('inf')
    time = math.log(2) / math.log(1 + rate)
    return time

def solve_log_equation(base, result):
    return math.log(result, base)

def convert_to_scientific_notation(number):
    coefficient, exponent = "{:.2e}".format(number).split('e')
    return coefficient, int(exponent)

def convert_from_scientific_notation(coefficient, exponent):
    return float(coefficient) * 10 ** int(exponent)

# Main program
while True:
    print("Select operation:")
    print("1. Calculate Annuity")
    print("2. Calculate Monthly Mortgage Payment")
    print("3. Estimate Retirement Investment Balance")
    print("4. Determine Time to Double Amount")
    print("5. Solve Logarithmic Equation")
    print("6. Convert to Scientific Notation")
    print("7. Convert from Scientific Notation")
    print("8. Exit")
    
    choice = int(input("Enter choice (1/2/3/4/5/6/7/8): "))
    
    if choice == 8:
        print("Exiting the calculator.")
        break
    
    if choice >= 1 and choice <= 7:
        if choice in [1, 2, 3, 4]:
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter rate: "))
            time = float(input("Enter time: "))
        
        if choice == 1:
            continuous = input("Calculate with continuous growth? (y/n): ").lower() == 'y'
            result = calculate_annuity(principal, rate, time, continuous)
            print("Annuity:", result)
        
        elif choice == 2:
            result = calculate_monthly_payment(principal, rate, time)
            print("Monthly Mortgage Payment:", result)
        
        elif choice == 3:
            result = estimate_retirement_balance(principal, rate, time)
            print("Estimated Retirement Investment Balance:", result)
        
        elif choice == 4:
            result = time_to_double(principal, rate)
            print("Time to Double:", result, "years")
        
        elif choice == 5:
            base = float(input("Enter base of the logarithm: "))
            result = float(input("Enter the result of the logarithm: "))
            solution = solve_log_equation(base, result)
            print("Solution of the logarithmic equation:", solution)
        
        elif choice == 6:
            number = float(input("Enter a number: "))
            coefficient, exponent = convert_to_scientific_notation(number)
            print("Scientific Notation:", coefficient, "x 10^", exponent)
        
        elif choice == 7:
            coefficient = input("Enter the coefficient: ")
            exponent = int(input("Enter the exponent: "))
            result = convert_from_scientific_notation(coefficient, exponent)
            print("Converted Value:", result)
    
    else:
        print("Invalid choice. Please select a valid option.")
