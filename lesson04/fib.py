def fibnum(lim,a=1,b=0,lev=1):
    print(a+b)
    if lev==lim:return a+b
    return fibnum(lim,b,a+b,lev+1)

def getlim():
    lim=int(input('请输入界限:'))
    print('第',lim,'位斐波那契数是',fibnum(lim))

getlim()
