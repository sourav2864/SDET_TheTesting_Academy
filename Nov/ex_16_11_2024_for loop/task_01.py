"""
Write a program that prints numbers from 1 to 100. However,
for multiples of 3, print "Fizz" instead of the number,
and for multiples of 5, print "Buzz."
For numbers that are multiples of both 3 and 5, print "FizzBuzz."
"""

for a in range(1, 100):
    if a % 3 == 0:
        print("Fizz")
    elif a % 5 == 0:
        print("Buzz")
    elif a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
    else:
        print(a)
