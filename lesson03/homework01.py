import fib

def getnum():
    print('请输入所需要的斐波那契数列的项数')
    num=int(input())
    fib.fib(num)

getnum()
