#质数是只能被1和它本身整出的数，编程
#输入一个数字，求其以内全部的质数。
def prime():
    print('请输入合适的范围：')
    num=int(input())
    if num>=0:
        for i in range(1,num+1):
            k=0
            for j in range (1,i+1):
                if i%j==0:
                    k+=1
                    continue
            if k<3:
                print(i)
    else:
        print('请输入正确的数字')
        prime()
prime()
