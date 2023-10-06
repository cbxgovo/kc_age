from math import *

def function_1_1():
    #请在此添加代码，输出字符串I LOVE China!
    #********** Begin *********#
    print("I LOVE China!")
    #********** End **********#

def function_1_2():
    #请在此添加代码，输入姓名、入学年份后，输出欢迎信息“欢迎*级*同学”，*用输入的姓名与入学年份替代
    #********** Begin *********#
    name=input()
    year=int(input())
    print("欢迎%d级%s同学" % (year,name))
    #********** End **********#

def function_1_3():
    #请在此书写代码，学号与姓名是字符串，高数与计算机成绩是float型，输出时要按照格式输出平均分显示小数点2位
    #********** Begin *********#
    num=input("学号：")
    name = input("姓名：")
    # a,b= int(input().split())
    a,b = map(float,input('高数、计算机成绩：').split()) 
    c = float((a+b)/2)
    print('%s%s的平均成绩为%.2f'%(num,name,c))
    #********** End **********# 

def function_1_4():
    # 选择题 DBBA
    print('选择题 DBBA')

# 2的这三个是重复的题目
def function_2_1():
    # coding=utf-8

    # 存放姓氏和名字的变量
    first_name = input()
    last_name = input()

    # 请在下面添加字符串拼接的代码，完成相应功能
    ###### Begin ######
    full_name = first_name + " " + last_name
    print(full_name)

    ####### End #######

def function_2_2():
    # 编写python代码，要求如下
    # step1: 将输入的源字符串source_string首尾的空格删除；
    # step2: 将step1处理后的字符串的所有单词的首字母变为大写，并打印输出；
    # step3: 将step2转换后的字符串的长度打印输出出来。
    source_string = input("Enter the source string: ")
    # Step 1: Remove leading and trailing spaces
    trimmed_string = source_string.strip()
    
    # Step 2: Capitalize the first letter of each word
    # capitalized_string = ' '.join(word.capitalize() for word in trimmed_string.split())
    capitalized_string = trimmed_string.title()
    print(capitalized_string)
    
    # Step 3: Print the length of the processed string
    # print("Length of the processed string:", len(capitalized_string))
    print(len(capitalized_string))

    # Example usage
   
def function_2_3():
    # Example usage
    # source_string = input("Enter the source string: ")
    source_string = input()
    # Step 1: Check if 'day' is a substring
    # if 'day' in source_string:
    #     print("'day' is a substring in the input string.")
    # else:
    #     print("'day' is not a substring in the input string.")
    index = source_string.find('day')
    first_day_index = index

    print(first_day_index)

    
    # Step 2: Replace 'day' with 'time'
    replaced_string = source_string.replace('day', 'time')
    # print("String after replacement:", replaced_string)
    print(replaced_string)
    
    # Step 3: Split the string by spaces
    split_string = replaced_string.split(' ')
    # print("List of words after splitting by spaces:", split_string)
    print(split_string)


def function_3_1():
    # coding=utf-8

    # 创建并初始化menu_list列表
    menu_list = []
    while True:
        try:
            food = input()
            menu_list.append(food)
        except:
            break

    # 对menu_list进行元组转换以及元组计算等操作，并打印输出元组及元组最大的元素
    menu_tuple = tuple(menu_list)
    print(menu_tuple)

    if menu_tuple:
        max_element = max(menu_tuple, key=lambda x: x[0])
        # print("元组中首字母最大的元素:", max_element)
        print(max_element)

def function_3_2():
    # coding=utf-8
    import json
    # 创建并初始化menu_dict字典
    menu_dict = {}
    while True:
        try:
            food = input()
            price = int(input())
            menu_dict[food] = price
        except:
            break

    # 添加一道菜名lamb，价格为50
    menu_dict['lamb'] = 50

    # 获取fish的价格并打印出来
    fish_price = menu_dict.get('fish')
    print("Fish price:", fish_price)

    # 将fish的价格改为100
    menu_dict['fish'] = 100

    # 删除noodles这道菜
    menu_dict.pop('noodles', None)

    # 输出新的menu_dict菜单
    # print("Updated menu_dict:")
    # for food, price in menu_dict.items():
    #     print(f"{food}: {price}")
    updated_menu_str = str(menu_dict).replace('"', "'")
    print(updated_menu_str)

def function_3_3():
    # coding=utf-8

    # 创建并初始化menu_dict字典
    menu_dict = {}
    while True:
        try:
            food = input()
            price = int(input())
            menu_dict[food] = price
        except:
            break

    # 遍历输出菜单的键
    # print("Keys in the menu_dict:")
    for key in menu_dict.keys():
        print(key)

    # 遍历输出菜单的值
    # print("Values in the menu_dict:")
    for value in menu_dict.values():
        print(value)

def function_3_4():
    # coding=utf-8

    # 初始化menu1字典，输入两道菜的价格
    menu1 = {}
    menu1['fish'] = int(input())
    menu1['pork'] = int(input())

    # menu_total列表现在只包含menu1字典
    menu_total = [menu1]

    # 添加menu2菜单并更新菜品价格
    menu2 = {'fish': menu1['fish'] * 2, 'pork': menu1['pork'] * 2}
    menu_total.append(menu2)

    # 输出新的menu_total列表
    print(menu_total)


def function_4_1():
    # 获取小球运动时间输入
    # t = float(input("请输入小球运动时间（秒）: "))
    t = float(input())
    g = 9.81  # 地球重力加速度，单位：m/s^2
    h = 25 * t - 0.5 * g * t ** 2  # 计算高度

    # 调用函数计算高度
    height = h

    # 输出计算得到的高度
    # print("小球在时间", t, "秒时的高度为", height, "米。")
    print('%.1f'%height)

def function_4_2():
    # 输入华氏度
    # fahrenheit = float(input("请输入华氏度: "))
    fahrenheit = float(input())
    celsius = (fahrenheit - 32) / 1.8

    # 调用函数进行转换
    celsius =  round(celsius, 2)

    # 输出结果
    print(f"华氏{fahrenheit:.2f}度=摄氏{celsius:.2f}度")

# 公式 麻烦 无语
def function_4_3():
    # 这里类或函数中不允许使用通配符导入Pylance 通过两种方式。头歌不用考虑，直接引入不用写函数.
    # 1. py文件头部引入
    # 2.下面这样分模块引入
    # from math import *
    from math import tanh;sqrt;cosh;log

    g = 9.8  # 重力加速度，单位：m/s^2
    m = 0.25  # 小球质量，单位：kg
    u = 0.5  # 阻尼系数

    t = int(input(""))

    v = 0.0  # 初始速度，单位：m/s
    x = 0.0  # 初始位置，单位：米

    # 计算速度v 不考虑摩擦的时候
    # v = u + g * t
    v = (sqrt(m*g/u))*tanh((sqrt(u*g/m))*t)

    # 计算运动距离x
    # x = u * t + 0.5 * g * t ** 2
    x = (m/u)*log(cosh((sqrt(u*g/m))*t))

    # 输出结果
    print("当t={}秒时，速度v={:.2f}米/秒".format(t, v))
    print("{}秒后，小球位置为向下{:.2f}米".format(t, x))

# 公式 麻烦 无语
def function_4_4():
    # 本程序计算小球向上斜抛在不同时间点的高度
    # from math import * # 直接省事全引入吧
    theta = int(input())  # 单位：角度

    # 转为弧度
    theta1 = (theta/180)*pi
    #   请在此添加实现代码   #
    # ********** Begin *********#
    # 转为m/s
    v = float(25/3.6)

    g = 9.8
    y_0 = 1
    x = 0.5

    y = x*(tan(theta1)) - ((1/(2*v*v))*((g*x*x)/(cos(theta1)*cos(theta1)))) + y_0


    print('y值计算结果为：%.5f米'%y)

    # ********** End **********#

def function_5_1():
    # 本程序计算1-N整数平方的累加和
    N = int(input())

    # 初始化总和为 0
    total_sum = 0

    # 使用循环计算平方之和
    for i in range(1, N+1):
        total_sum += i**2

    # 打印结果
    print(total_sum)


    # ********** End **********#

def function_5_2():
#请验证输入的列表N_list中的整数是否为三位数，并返回三位数整数的百位数值

# N_list = [int(i) for i in input().split(',')]

#   请在此添加实现代码   #
# ********** Begin *********#
    def validate_and_get_hundreds_digit(numbers_list):
        # 用于存储符合条件的三位数的百位数值
        hundreds_digits = []

        for num in numbers_list:
            if 100 <= num <= 999:
                # 获取百位数值
                hundreds_digit = (num // 100) % 10
                hundreds_digits.append(hundreds_digit)

        return hundreds_digits

    # 输入整数列表
    # 输入逗号分隔的整数，并将其存入列表
    input_str = input()

    # 使用split函数将输入字符串分割成整数字符串列表
    int_strings = input_str.split(',')

    # 将整数字符串转换为整数并存入列表
    int_list = [int(num) for num in int_strings if num.strip().isdigit()]

    # 获取符合条件的三位数的百位数值
    hundreds_digits_list = validate_and_get_hundreds_digit(int_list)
    # 输出结果
    print(hundreds_digits_list)

    # ********** End **********#

def function_5_3():
    # 本程序要求返回算到N_list列表中每一项时的圆周率值，并用列表进行存储，最终输出列表结果

    N_list = [int(i) for i in input().split(',')]
    n_list=[]
    #   请在此添加实现代码   #
    # ********** Begin *********#
    #遍历元素
    for i in N_list:#i=2*n-1
        n=1
        pi=0
        while(2*n-1<=i):
            pi=pi+4*((-1)**(n-1)/(2*n-1))
            n=n+1
        n_list.append(pi)
    #print(n_list)
    print(["{:.8f}".format(i) for i in n_list])

    # ********** End **********#

def function_5_4():
    # 请用函数实现Machin公式计算，包含隐含参数N

    def arctg(x, N=5):   # 迭代项数N的缺省值是5，即如果调用时不给值就用5
        #   请在此添加实现代码   #
        # ********** Begin *********#
        i = 1
        sum = 0
        while(i<=N):
            k = pow(x,2*i-1)/(2*i-1)
            s = pow(-1,i-1)
            sum += k*s
            i = i+1
        return sum
        # ********** End **********#

def function_5_5():
    # 请实现ln函数
    def ln(x, N=50):
        '''
        :param x: 输入值
        :param N: 迭代项数
        :return: 对数值，误差的绝对值
        '''
        #   请在此添加实现代码   #
        # ********** Begin *********#
        from math import log, fabs
        i = 1
        sum = 0.0
        while (i <= N):
            k = float((pow(-1, i + 1) * pow(x - 1, i)) / i)
            sum += k
            i = i + 1
        s2 = fabs(sum - log(x))
        return sum, s2
        # ********** End **********#

def function_pandas_1():
    # -*- coding: utf-8 -*-
    from pandas import Series,DataFrame
    import  pandas as pd

    def create_series():
        '''
        返回值:
        series_a: 一个Series类型数据
        series_b: 一个Series类型数据
        dict_a：  一个字典类型数据
        '''
        # 请在此添加代码 完成本关任务
        # ********** Begin *********#
    # 请在此添加代码 完成本关任务
        # ********** Begin *********#
        series_a=Series([1,2,5,7],index=['nu', 'li', 'xue', 'xi'])
        dict_a={'ting':1, 'shuo':2, 'du':32, 'xie':44}
        series_b=Series(dict_a)
    
        # ********** End **********#
    
        # 返回series_a,dict_a,series_b
        return series_a,dict_a,series_b

        # ********** End **********#

        # 返回series_a,dict_a,series_b
        return series_a,dict_a,series_b

def function_pandas_2():
    # -*- coding: utf-8 -*-
    from pandas import Series,DataFrame
    import  pandas as pd

    def create_dataframe():
        '''
        返回值:
        df1: 一个DataFrame类型数据
        '''
        # 请在此添加代码 完成本关任务
        # ********** Begin *********#
        dictionary={'states':['','','','',''],
                'years':['','','','',''],
                'pops':['','','','','']}
        df1=DataFrame(dictionary)
        df1=DataFrame(dictionary,index=['one','two','three','four','five'])
        df1['new_add']=[7,4,5,8,2]
    
    
        # ********** End **********#

        # ********** End **********#

        #返回df1
        return df1

def function_pandas_3():
    # -*- coding: utf-8 -*-
    from pandas import Series,DataFrame
    import  pandas as pd
    def read_csv_data():
        '''
        返回值:
        df1: 一个DataFrame类型数据
        length1: 一个int类型数据
        '''
        # 请在此添加代码 完成本关任务
        # ********** Begin *********#

        df1=pd.read_csv('test3/uk_rain_2014.csv', header=0)
        df1.columns=['water_year','rain_octsep','outflow_octsep','rain_decfeb', 
                    'outflow_decfeb', 'rain_junaug', 'outflow_junaug']
        length1=len(df1)
    

        #返回df1,length1
        return df1,length1









if __name__ == '__main__':
    # function_1_1()
    # function_1_2()
    # function_1_3()
    # function_1_4()

    # function_2_1()
    # function_2_2()
    # function_2_3()

    # function_3_1()
    # function_3_2()
    # function_3_3()
    # function_3_4()

    # function_4_1()
    # function_4_2()
    # function_4_3() # 手写公式 麻烦
    # function_4_4() # 手写公式 超级 麻烦

    # function_5_1() 
    # function_5_2() 
    # function_5_3() 
    # function_5_4() 
    # function_5_5() 

    # function_pandas_1()
    # function_pandas_2()
    function_pandas_3()
    # pandas其他 https://blog.csdn.net/weixin_61800684/article/details/124515918

    # 实验1-12 https://blog.csdn.net/weixin_61800684/category_11780530.html





