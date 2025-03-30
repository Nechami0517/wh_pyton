import datetime


def run_time(func):
    def inner(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        end = datetime.datetime.now()
        return end - start;
    return inner
@run_time
def print_number(n):
    for i in range(n):
        print(f" {i } ")
#print(print_number(10));

#ex2

dict = {}
def cache(func):
    def inner(n):

        if dict.keys().__contains__(n):

            return dict[n]
        else:
            num = func(n)
            dict[n] = num;
            return  num;
    return inner





@cache
@run_time
def calc_Fibonacci(num):
    n = num
    num1 = 0
    num2 = 1
    next_number = num2
    count = 1

    while count <= n:

        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    return  next_number


print(calc_Fibonacci(45455));