#利用递归计算斐波那契数列第lim项的值
def fibnum(a=1,b=0,lim=4,lev=1):
    if lev==lim:
        return a
    return fibnum(a+b,a,lim,lev+1)

#输入一个数字，调用求斐波那契数列该项数值的函数
def fib(i):
    if i>0:
        print(fibnum(lim=i))
    else:
        print('请输入正确的值！！！')
        fib()
