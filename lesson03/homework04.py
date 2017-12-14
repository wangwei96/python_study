#编写一个函数，输出某个目录下面的文件层级
import os

print ('***获取当前目录***')
file_dir=os.getcwd()
f=open ('namelist.txt')
ls=f.readlines()
f.close()

for i in ls:
    name=i.split('/')[-2]
    file=file_dir+'\\'+name
    
def file_name(file):
    for root, dirs, files in os.walk(file):
        print('当前目录路径',root) #当前目录路径
        for dirname in dirs:
            print('当前路径下所有子目录',dirname) #当前路径下所有子目录
        for filesname in files:
            print('当前路径下所有非目录子文件',filesname) #当前路径下所有非目录子文件

'''
setnum=1
getnum=open ('num.txt','r+')
getnum.write('%s'%setnum)
num=getnum.readlines()
setnum=num+1
getnum.close()


print(num)
'''
file_name(file)


