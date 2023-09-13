# age 信息可以抽取的形式：

31 to 235
235.2 ± 2

234±0.3
235.1
from 231 to 235
223
480.3 similar to 452
212-211

ca:.850

先统计一下有 excel 几个矿床

然后 to one 处理

# 文件备注

all_Ma.txt 所有的初始源句子 可是带有重复语句
all_Ma_out.txt 执行 readtxt.py 文件的第一个函数之后输出的去除重复句子的原始句子

kc_name.xlsx 是给定的矿床的名字 2056个；  第一次最后剩1360 ；之后最后剩下1287

all_5w_ages.xlsx 是通过正则表达式筛选句子出来的表格 包含多种形式的年龄在一个空格中  对比在new后缀中的表2
out_all_ages.xlsx 是上面一个 all_5w_ages.xlsx 文件 拆分为多行 中心值 和 误差 两列数据的形式

test_remove_error.xlsx 是多行变为少行之前的表格 需要通过策略缩减数据量



out_all_ages_new.xlsx  3.98w    

out_all_ages_new_quxia1.0.xlsx  3.34w  这个数据没有考虑单行丢失和双行数据差距大全部丢失

out_all_ages_new_quxia1.0.xlsx  3.37w  这个数据考虑单行丢失和双行数据差距大全部丢失  多了300多行
