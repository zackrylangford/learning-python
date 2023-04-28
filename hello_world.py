# 1

integer = 1

print(type(integer))

boobox = True

print(type(boobox))


number = 2.0 

print(type(number))

words = "This is words"

print(type(words))


#2
radius = 5

print(3.14159 * radius**2)

#3
string = "Python is fun!"

print(string.upper())

#4
a = 7 
b = 5

print(a)
print(b)

#5

a = 15
b = 9

if a > b:
    print("True")
else: 
    print("False")

#6
number = int(input())

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
#7

for x in range(0,10):
    print(x)


#8

numbers = int(input())

while numbers <= 100:
    add = int(input())
    numbers += add
    print(numbers)

#9

def multiply(x,y):
    return(x*y)

x = int(input())
y = int(input())
print(multiply(x,y))


#10

def fizz_buzz(num):
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
 