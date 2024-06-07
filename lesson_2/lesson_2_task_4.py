num = int(input("Введите n:"))
def fizz_buzz(num):
    for num in range(1, num+1):
        if(num % 3 == 0) and (num % 5 == 0):
            print("FizzBuzz")
        elif(num % 3 == 0):
            print("Fizz")
        elif(num % 5 == 0):
            print("Buzz")
        else:
            print(num)

fizz_buzz(num)