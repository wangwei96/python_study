import os
import os.path

def showdir(dirname, level):
    subdirs = list(os.listdir(dirname))
    for subdir in subdirs:
        print("--"*level,subdir,"--"*level)
        subdir = dirname + "\\"+subdir
        if not os.path.isdir(subdir):continue
        showdir(subdir, level+1)

def getdir():
    dirname=input('请输入网址')
    showdir(dirname, 0)
getdir()
