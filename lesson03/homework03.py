#用埃拉托色尼筛输出0-n的质数的list
'''
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 
            2 3   5   7   9    11    13    15
            2 3   5   7        11    13      
            2 3   5   7        11 12 13 14 
            2 3   5   7        11    13    
'''
'''
ls=list(range(10))
print(ls)
del ls[2]
print(ls)
'''
#用埃拉托色尼筛输出0-n的质数的函数（第一版本）
def getlist(x=100):
    lg=[]
    ls=list(range(x))
    for i in range(x):
        if ls[i]==0:
            ls[i]=0
        elif ls[i]==1:
            ls[i]=0
        else:
            for r in range(i,x):
                if ls[i]!=0:
                    if ls[r]%ls[i]==0 and ls[r]/ls[i]!=1:
                        ls[r]=0
    for i in range(x):
        if ls[i]!=0:
            lg.append(ls[i])
    return lg
            
#设置n，调用函数
def setlist():
    print('请输入n的数值:')
    x=int(input())
    print('0 -',x,'的质数为:',getlist(x))

setlist()
