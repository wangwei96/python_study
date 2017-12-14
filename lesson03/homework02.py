#
import fib

def fiblist():
    print('请输入所需的斐波那契数列的项数')
    num=int(input())
    for i in range(1,num+1):
        fib.fib(i)

fiblist()
