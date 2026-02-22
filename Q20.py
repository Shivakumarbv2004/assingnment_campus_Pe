# QUESTION NO 20:


# NUMBER SYSTEM FUNCTIONS PROGRAM


import math

# Step 1: Take input
number = int(input("Enter a number: "))

# Factorial
print("Factorial :", math.factorial(number))

# Prime check
is_prime = True
if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

print("Prime     :", is_prime)

# Fibonacci (nth)
n = number
a, b = 0, 1
for _ in range(n):
    a, b = b, a + b

print("Fibonacci :", a)

# Sum of digits
digit_sum = sum(int(d) for d in str(number))
print("Sum of Digits :", digit_sum)

# Reverse number
print("Reversed Number :", int(str(number)[::-1]))