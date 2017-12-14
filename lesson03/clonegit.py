'''a = 'asfdgasfdas'
print(a.replace('a', '*'))
print(len(a)-len(a.replace('a','')))
print(a.upper())

import os
f = open('abc.txt', 'w')
f.write('my file')
f.close()



import os
f= open('abc.txt','w')
f.write('hello')
f.close()
'''
import os

f=open ('namelist.txt')
ls=f.readlines()
f.close()

for i in ls:
    name=i.split('/')[-2]
    os.mkdir(name)
    os.system('git clone %s %s'%(i+'.git',name))
