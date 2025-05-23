a = list(range(10))
print(a)
b = list(range(1,11))
print(b)
#生成[1x1, 2x2, 3x3, ..., 10x10]
#eg1：循环
L=[]
for x in range(1,11):
    L.append(x*x)
print(L)
#eg2：列表生成式
b = [x*x for x in range(1,11)]
print(b)

b=[x*x for x in range(1,11)if x%2==0]#加入条件
print(b)
c = [a+b for a in 'abc' for b in 'ABC' ]#全排列#两层
print(c)

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os#导入os模块
A = [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(A)

#for循环其实可以同时使用两个甚至多个变量
my_dict = {'a':3,'b':4,'qwe':567}    #不建议使用 dict 作为变量名，因为它会覆盖 Python 内置的 dict 类型
for k,v in my_dict.items():
    print(k,'=',v)

#因此，列表生成式也可以使用两个变量来生成list：
my_dict = {'a':3,'b':4,'qwe':567,'abc':123}
M = [k + '=' + str(v) for k,v in my_dict.items()]
print(M)

L = ['Hello', 'World', 'IBM', 'Apple']
M = [s.lower() for s in L]
print(M)

#在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else

#test
L1=['Hello',1,None,'star','GOOD']
L2=[]
for x in L1:
    if isinstance(x,str)==True:
        L2.append(x)
M=[s.lower() for s in L2]
print(M)
if M==['hello','star','good']:
    print('测试成功')
else:
    print('测试失败')

#test2
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')