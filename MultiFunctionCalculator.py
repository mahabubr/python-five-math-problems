# https://colab.research.google.com/drive/1fO9Ut-XkF9dIiHTVxDrDz2802uMFPcAd#scrollTo=pAqyaopggmPJ

import fractions

# Function to solve proportions
def solve_proportion(a, b, c):
    return (b * c) / a

# Function to solve for x in equations of the form ax + b = c
def solve_equation(a, b, c):
    return (c - b) / a

# Function to factor square roots
def factor_square_root(number):
    factors = []
    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

# Function to convert decimals to fractions
def decimal_to_fraction(decimal):
    fraction = fractions.Fraction(decimal).limit_denominator()
    return f"{fraction.numerator}/{fraction.denominator}"

# Function to convert decimals to percents
def decimal_to_percent(decimal):
    return decimal * 100

# Function to convert fractions to decimals
def fraction_to_decimal(numerator, denominator):
    return numerator / denominator

# Function to convert fractions to percents
def fraction_to_percent(numerator, denominator):
    decimal = fraction_to_decimal(numerator, denominator)
    return decimal_to_percent(decimal)

# Function to convert percents to decimals
def percent_to_decimal(percent):
    return percent / 100

# Function to convert percents to fractions
def percent_to_fraction(percent):
    decimal = percent_to_decimal(percent)
    fraction = fractions.Fraction(decimal).limit_denominator()
    return f"{fraction.numerator}/{fraction.denominator}"

# Testing the functions
def test_functions():
    print(solve_proportion(2, 4, 6))
    print(solve_equation(3, 6, 15))
    print(factor_square_root(36))
    print(decimal_to_fraction(0.75))
    print(decimal_to_percent(0.5))
    print(fraction_to_decimal(3, 4))
    print(fraction_to_percent(5, 8))
    print(percent_to_decimal(25))
    print(percent_to_fraction(60))

# Call the test function
test_functions()
