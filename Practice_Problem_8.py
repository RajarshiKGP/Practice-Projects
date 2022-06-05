'''
Python Problem 8: Fake Multiplication Tables | Python Tutorials For Absolute Beginners In Hindi #117
The task you have to perform is “Fake Multiplication Tables”. This task consists of a total of 15 points to evaluate your performance.

Problem Statement:-
 Rohan das is a fraud by nature. Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.

Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!

So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.

Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.

Note: Rohan’s function returns a list of numbers like this

Rohan Das’s Function Input:
rohanMultiplication(6)

Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]

You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None

You cannot learn to code by just watching the code implementation until you start to doing it yourself.
'''

from random import randint

lstF = []
lstC = []

def faultyTable(n):
    a = randint(n, 10*n)
    print(a)
    def f(x): return n*x
    for i in range(1, 11):
        if abs(a-f(i)) <= n//2:
            lstF.append(a)
        else:
            lstF.append(f(i))
    return lstF


def detector(n, args):
    flag = 1
    for i in range(10):
        if (args[i]) % n == 0:
            lstC.append(args[i])
        else:
            flag = 0
            print(f"{args[i]} is wrong")
            lstC.append(int((args[i-1] + args[i+1]) / 2))
    return flag


if __name__ == '__main__':
    num = int(input("Enter the number: "))
    print(faultyTable(num))
    f = detector(num, lstF)
    if f == 0:
        print("The correct table should be:")
        print(lstC)
