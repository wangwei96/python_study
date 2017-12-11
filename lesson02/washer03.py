# 洗衣流程
print('请输入水位')
level = input()

'''
if xxx:
  do...
elif xxx:
  do...
else:
  do...
'''
#高水位
if level=='h':
    print('注水30L')
    print('搅拌25min')
#中水位
elif level=='m':
    print('注水20L')
    print('搅拌20min')
#低水位
elif level=='l':
    print('注水15L')
    print('搅拌15min')
print('放水')

# 甩干流程
print('请输入甩干次数')
times=int(input())

for i in range(times):
    print('注水30L')
    print('搅拌5min')
    print('放水')
    print('高速搅拌20min')
