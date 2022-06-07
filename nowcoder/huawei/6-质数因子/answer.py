from timex import timeit
import math

@timeit
def func1(num):
    s = ''
    prime = 2
    sqrt = math.sqrt(num)
    while prime < sqrt+1:
        if num%prime != 0:
            prime += 1
        else:
            num = num //prime
            sqrt = math.sqrt(num)
            s += str(prime)+' '
            prime = 2
    if num>=2:
        s += str(num)+' '
    print(s)

@timeit
def func2(n):
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            n = n // i
            print(i, end=" ")
    if n > 2:
        print(n, end=" ")
    print()

@timeit
def func3(n):
    res = []
    while not n % 2:
        n//=2
        res.append(2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        while not n % i:
            n //= i
            res.append(i)
    if n > 1:
        res.append(n)
    print(" ".join(map(str, res)))


num = int(input())

func1(num)
func2(num)
func3(num)
