#质数是只能被1和它本身整出的数，编程找出100以内全部的质数。
for i in range(1,101):
    k=0
    for j in range (1,i+1):
        if i%j==0:
            k+=1
            continue
    if k<3:
        print(i)

