#請利用 python 的 tuple 實作函數 fib(n) 回傳第 n 項的Fibonacci 數字.
#例如: fib(5) 回傳 5, fib(7) ) 回傳 13
#1 1 2 3 5 8 13..
# fib(3)=2

def fib(n):
    a = 0
    b = 1
    # a, b= 0,1
    for i in range(1,n):
        a,b = b, a+b
    return b

print(fib(3))
print(fib(5))
print(fib(7))


def fib2(n):
    a = 0
    b = 1
    for i in range(1,n):
        c = a + b
        a = b
        b = c