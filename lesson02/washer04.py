# 洗衣流程
def wash():
    print('请输入重量')
    heavy = int(input())
    if heavy <=10:
        level = 'l'
        times = 2
    elif heavy>10 and heavy<20:
        level = 'm'
        times = 3
    elif heavy>=20 and heavy<30:
        level = 'h'
        times = 4
    else:
        level = 'out'
        times = 0

#高水位
    if level=='h':
        print('注水30L')
        print('搅拌25min')
        print('放水')
#中水位
    elif level=='m':
        print('注水20L')
        print('搅拌20min')
        print('放水')
#低水位
    elif level=='l':
        print('注水15L')
        print('搅拌15min')
        print('放水')
    elif level=='out':
        print('重量过高，请减少衣物！！！')
        wash()

# 甩干流程
    for i in range(times):
        print('注水30L')
        print('搅拌5min')
        print('放水')
        print('高速搅拌20min')
wash()
