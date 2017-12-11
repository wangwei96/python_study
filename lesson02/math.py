# 求1+2+3+...+100=？
s=0
for i in range(1,101):
    s +=i
print('从1到100的和为：',s)

#求2+4+6+...+100=？
s=0
for i in range(1,101):
    if i%2==0:
        s +=i
print('从1到100的偶数的和为：',s)

#求1+3+5+...+99=？
s=0
for i in range(1,101):
    if i%2==0:continue
    s +=i
print('从1到100的奇数的和为：',s)

# 打印0-100，必须是偶数，各个数位相加为9
for i in range(1,100):
    if i%2==0 and i%10 + i//10==9:
        print(i)
