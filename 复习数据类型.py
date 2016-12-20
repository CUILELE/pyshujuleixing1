# /user/bin/env python
#  -*- coding:utf-8 -*-
# Author:CLL

name = 'cll'#变量name的值为："cll"
name,name2 = 'cll','cll1'
NAME = 1常亮大写吧 不要更改
python解释器在加载 .py 文件中的代码时，会对内容进行编码（默认ascill）

msg = '''
name:%s
age：%d
job：%
'''%(name,age,job)
name 对应的是%s 不是name，而name只是字符串表示用的。
ask码  uniko utf8 ===

pyc 就是编译后的字节码

总结数据类型
数字  str字符串 list列表 tuple元组 dict字典 set无序不重复的的序列列表

数据类型初识
一.数字
   int()得到一个整数。
   float()得到有个小数。
   complex()复数

二.布尔值 真或假 1或0

三.字符串 'cll'
列:字符串连接
name = 'cll'
print('i am %s'%name)字符串是 %s;整数 %d;浮点数%f
字符串常用功能

1.移除空白 strip()去掉空格，移除空白语法 字符串.strip()
2.分割 split() 转为数组列表 字符串.split(分隔符)
join()转为字符串 ''.join(字符串)
3.长度 len(str)
4.索引 1 find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回-1
    find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回-1
    python 的index方法是在字符串里查找子串第一次出现的位置，类似字符串的find方法，不过比find方法更好的是，如果查找不到子串，会抛出异常，而不是返回-1
5.切片str[0:8]
6.startswith(c)	检查是否以c开头 语法str.startswith();参数三个 检测的字符串，开始位置，结束位置。
    print str.startswith( 'c', 2, 4 );
7.count()	计算子字符串c出现的次数 语法str.count(str,0,9)检测的字符串，开始位置，结束位置。
8.upper()	返回大写形式lower()返回小写形式

四.列表 列表的内容可变，可以包含任意对象，使用中括号表示。
 创建列表list= ['cll',1,2,3,40]
 基本操作  列表的方法主要用于改变里面的内容，下面列出列表常用的方法。
    1.索引：list.index[1]
    2.切片：list[0:2]结果'cll',1 list[0:]算最后一个 list[0:4][0:1]结果为cll
    3.修改：list[1] = 'cll1'
    4.追加:
        list.insert(2,'clllname')参数从第几个插，插入内容
        list.append()最后一个插入 一个参数插入的内容
    5.删除：
        list.remove()参数删除的元素
        del list[0:1] 结果是[1, 2, 3, 40]是一个全局的删除。
    6.长度:len(list)
    7.循环:for val in list:
            print(val) val是每个值

    8.包含或判断一个列表是否有这个元素 可以通过in和not in关键字来判读一个list中是否包含一个元素
       if 1 in list:
           print('1 in list')

       if 1 not in list:
           print('1 not in list')
    9.步长 隔一个取一个 参数3个 开始位置，结束位置，步长选择从几位选一个就是跳的意思。
        list[::2]
    10.count()	计算子出现的次数list.count(1)
    11.index()  第几位出现index 索引
    12.extend()合并列表 list.extend(列表)
    13.resevers()翻转列表
    14.list.pop()删除最后一个，括号里可以添加删除第几个
    15.list.copy()只copy第一层 list2= list.copy()如果深度需要引入标准库深copy完全克隆一份，软copy相当于一个软连接。
        import copy
        name4 = copy.deepcopy(name)#等于内存中保留两份数据完全独立
    16.list.sort() 排序3.0版本不能拍字符串只能数字

五.元组
    不可变列表 只读  生成之后不能改,。只能统计数据 获取到那个数据。不想改就是只读。
    r = (1,2,3,4,5,6)就两个操作 一个索引一个查看
    list((r))元组转列表

六.字典(Dictionary) 自己有去重功能 key:value 中间冒号区分，字典是另一种可变容器模型，且可存储任意类型对象。
    dict = {key1 : value1, key2 : value2 } key(键)是唯一的但值不必值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
    基本操作：
    dict = {
        110229:{
            'name':'cll',
            'age':10,
            'job':'web'
        },
        11021129:{
            'name':'cll1',
            'age':1980,
            'job':'ss'
        }
    }
    1.索引
        查看：dict[110229].name查看一般都用下边那种，不会报错
        获取查看:ck = dict[110229].name
    2.新增: dict[110229]['qq'] = 421673757
    3.删除:del dict[110229]
        dict[110229].pop('name')
    4.updata更新 dict.update(新字典)
    5.看所有values keys看所有keys dict.values() dict.keys()
    6.判断是否有 110229 in dict
    7.循环一个字典for key in dict：
                    print(key,dict[key])
    8.dict.setdefault(916460542,'haha')取一个key如果不存在就添加一个key：value
    9.dict.clear()清空字典
    10. dict.items()返回字典的（键，值）元组对的列表.
    11.len(dict)

七.集合set()
   tuple算是list和str的杂合(杂交的都有自己的优势,上一节的末后已经显示了),那么set则可以堪称是list和dict的杂合.
   set拥有类似dict的特点:可以用{}花括号来定义；其中的元素没有序列,也就是是非序列类型的数据;而且,set中的元素不可重复,这就类似dict的键.
   set也有继承了一点list的特点:如可以原处修改(事实上是一种类别的set可以原处修改,另外一种不可以)
   创建两种方法 set = {11,22,33}  set= set()
   基本操作：(集合支持一系列标准操作，包括并集、交集、差集和对称差集)
        set = {11,22,33}
        set1 = {22,33,44}
        1.添加 set.add()
        2.删除 set.discard()移除指定元素不报错
               set.remove()
               set.pop()移除某个元素并且获取到这个元素赋值一个变量随机的，因为集合就是无序的 知道就行不常用
        3.清空集合 ser.clear()
        4.set.copy()
        5.长度len(set)
        6.是不是这个集合的判断 11 in set  11 not in set
        7.difference a中存在b中不存在no = set.difference(set1) 11
        8.set.intersection(set1)	求交集，返回同时在s和t中的项目
        9.set.isdisjoint(set1)判断连个集合有没有交集s和t中没有相同项，返回True
        10.set.issubset()判断是不是子序列 set.issuperset()判断是不是父序列
        11.set.union(set1)返回一个新的两个都有的set
        11.1set.symmetric_difference 都不存在的会覆盖之前的，如果以后不用之前的可以这么用11 44
        12.set.update()结果是11,22,33,44 update更新接受可以迭代的对象。只要是update就相当于给set从新赋值了相当于批量添加  有列表元组字符串都行只要能循环
        13.set.intersection_update(set1) 结果是22,33更新成两个交集
        14.set.symmetric_difference_update(set1)结果是11,44更新两个都没有的
        15.s.difference_update(set1)更新不存在的结果是11 a中存在b中不存在的
