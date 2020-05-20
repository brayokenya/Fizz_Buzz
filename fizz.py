number = 100

for number in range(0, number+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # print(number)
    elif number % 5 == 0:
        print("Buzz")

    elif (number % 3 == 0):
        print("Fizz")

    else:
        print(number)
