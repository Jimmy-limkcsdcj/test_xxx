#对x四舍五入，d是小数截取位数。不确定尾数通常发生在10^-16左右
round(x,d)
#浮点数可以采用科学计数法表示，用e或者E作为幂符号，例如4.3e-3表示0.0043
9.6E5
#复数类型
#数值运算操作符
x//y#整数除，例如10//3结果是3
x%y#余数，模运算，10%3结果为1
x**y#x的y次幂运算，y可以是小数
#二元操作符有对应的增强赋值操作符？？不掌握也不所谓，可以用一般的运算符替代表达，不足就是会比较冗余
#数值运算函数
abs(x)#求x的绝对值
divmod(x,y)#获得x除以y的商数和余数，即（x//y，x%y）例如divmod(x,y)结果为（3，1）
pow(x,y[,z])#幂余，（x**y）%z,[..]表示参数z可省略
round(x[,d])# round(-10.123235,3)的结果为-10.123
max(1,9,5,43)#
min(1,9,5,43)
#一些以函数形式提供的数值运算功能
int(x)#将x保留其整数部分，舍弃小数点后面的数字
float(x)#将x变成浮点数，例如float(12)结果为12.0；float（“1.23”）结果为1.23
complex(x)#将x变成复数，增加虚数部分，例如complex
print ("GL is handsome")

#天天向上的力量
#DayupQ1.py
dayup=pow(1.001,365)
daydown=(0.999,365)
print("向上:{:.2f},向上:{:.2f}".format(dayup,daydown))
#DayupQ2.py
dayfactor=0.005
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))

#DayupQ3.py
dayup=1.0
dayfactor=0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("工作日的力量:{:.2f}".format(dayup))

#DayupQ4.py#g根据df参数计算工作日力量的函数，参数不同，这段代码可以共用。def保留字用于定义函数。(注意缩进是否正确！！)
def dayUP(df):
    dayup=1
    for i in range(365):
        if i %7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
while dayUP(dayfactor)<37.78:
    dayfactor += 0.001
print("工作日的努力参数是:{:.3f}".format(dayfactor))

#天天向上的力量举一反三
#for..in..(计算思维，不太同于数学思维，是抽象和自动化结合的结果，借助计算机超强算力实现)
