# session 3 for the day



#1 Variables and Data Types: Create a string, an integer, and a floating point number. The string should be named mystring and should contain the word "hello". The floating point number should be named myfloat and should contain the number 10.0, and the integer should be named myint and should contain the number 20.


mystring = "hello"

myfloat = 10.0

myint = 20

#2Basic Operations: Write a Python program to add two numbers, where one is given by the user.

x = int(input("Enter a number to add: "))

y = int(input("Enter another number to add: "))

answer = x + y

print(f"Answer: {answer}")

#3String Manipulation: Given the string "Learning Python is Fun!", write a Python code to count the number of vowels in the string.

string = "Learning Python is Fun!"
num = 0
for x in string.lower():
    if x in 'aeiou':
        num += 1
print(num)


# 4Mathematical Operators: Write a program to compute the future value of a specified principal amount, rate of interest, and a number of years. Ask the user to input the values.

principle = float(input("Principle: "))

rate_of_return = float(input("Rate of Return: "))

years = int(input("No. of years: "))

future_value = (principle * rate_of_return * years)
print(future_value)

#Correct. However, the formula for future value you used is incorrect. The correct formula for future value is FV = PV * (1 + r/n)^(nt), where PV is the present value (principal), r is the annual interest rate (in decimal), n is the number of times that interest is compounded per year, and t is the number of years the money is invested for. If you're not compounding the interest, the formula is simply FV = PV * (1 + r*t)


# 5Comparison Operators: Write a Python program that asks the user for two numbers and returns True if both numbers are even and False otherwise.

x = int(input("Number 1: "))
y = int(input("Number 2: "))

if x % 2 == 0 and y % 2 == 0:
    print("True")
else:
    print("False")


#6Control Flow (If, Else): Write a program that asks the user to input a grade (0-100). If the grade is 90 or above, it should print "A". If it's 80-89, it should print "B". If it's 70-79, it should print "C". If it's 60-69, it should print "D". If it's below 60, it should print "F".

grade = int(input("Give me a grade(0-100): "))

if grade < 60:
    print("F")
elif grade < 70:
    print("D")
elif grade < 80:
    print("C")
elif grade < 90:
    print("B")
elif grade < 100:
    print("A")
elif grad > 100:
    print("A+")

# 7Loops: Write a Python program that uses a for loop to print all the multiples of 3 from 3 to 30.

for x in range(3, 31):
    if x % 3 == 0:
        print(x)
# 8Loops: Write a Python program using a while loop that prints the first 10 natural numbers in reverse order.

x = 10
while x <= 10 and x > 0:
    print(x)
    x -= 1


#9 Functions: Write a function is_prime that takes a number as an argument and returns True if the number is prime, and False otherwise
x = int(input("Give me a number, I will tell you if it is prime: "))

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(x))


#10Control Flow and Functions: Write a function leap_year that takes a year as an argument and returns True if it's a leap year and False if it's not.

year = int(input("Give me a year I will tell you if it is a leap year: "))

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(leap_year(year))