#!/usr/bin/env python3

def happy_new_year():
    i=0
    while i<=10:
        print(10-i) if((10-i)!=0) else print("Happy New Year!")
        i += 1

def square_integers(int_list):
    int_list = [int**2 for int in int_list]
    return int_list

def fizzbuzz():
    i=1
    while i<=100:
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        elif(i%3==0):
            print('Fizz')
        elif(i%5==0):
            print('Buzz')
        else:
            print(i)
        i += 1
