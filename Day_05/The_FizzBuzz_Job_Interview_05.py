i = 0 
for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)