#编写一个函数，输出某个目录下面的文件层级
import os
    
def file_name(file):
    for root, dirs, files in os.walk(file):
        print('当前目录路径',root) #当前目录路径
        for dirname in dirs:
            print('当前路径下所有子目录',dirname) #当前路径下所有子目录
        for filesname in files:
            print('当前路径下所有非目录子文件',filesname) #当前路径下所有非目录子文件

def get_file():
    print ('***获取当前目录***')
    file_dir=os.getcwd()
    print(file_dir)
    f=open ('namelist.txt')
    ls=f.readlines()
    print(ls)
    f.close()
    
    for i in ls:
        print(i)
        file_name(i)

get_file()


