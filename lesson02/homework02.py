'''斐波那契数列是两个1构成，从第三项开始，每一项是由前面两项的和构成，
   如下：1，1，2，3，5... 请通过编程得到数列的前100项，
   并输出99项与100项的比值。
'''
def Fibonacci():
    print('请输入合适的范围，要求是大于0的数字：')
    put=int(input())
    j=1
    k=0
    x=0
    if put==1:
        print('斐波那契数第 1 位是',j)
    elif put>1:
        print('斐波那契数第 1 位是',j)
        for i in range(1,put):
            x=j
            j+=k
            k=x
            print('斐波那契数第',i+1,'位是',j)
            ratio=k/j
        print('斐波那契数第',put-1,'项与第',put,'项的比是',ratio)
    else :
        print('请输入正确的值：')
        Fibonacci()

Fibonacci()
