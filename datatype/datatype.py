#%%
# python 有几种数据类型
# 1. 整数型 int
# 2. 浮点型 float
# 3. 元组 tuple
# 4. 字典 dictionary
# 5. 列表 list
# 6. 字符类型 str
# 7. 集合类型 set
# %%
a = 3 #整数型
print(a)
print(f"the type of variable a is {'int' if isinstance(a, int) == True else 'unknow'}")

# %%
a = 3.14
print(a)
print(f"the type of variable a is {'float' if isinstance(a, float) == True else 'unknow'}")

# %%
a = (1, 2, 3)
print(a)
print(f"the type of variable a is {'tuple' if isinstance(a, tuple) == True else 'unknow'}")

# %%
a = [1, 2, 3]
print(a)
print(f"the type of variable a is {'list' if isinstance(a, list) == True else 'unknow'}")

#%%
a = "'123'"
print(a)
print(f"the type of variable a is {'str' if isinstance(a, str) == True else 'unknow'}")

#%%
a = {
    "yang": 0, 
    "yong": 1,
    "xi": 2
}
print(a)
print(f"the type of variable a is {'dict' if isinstance(a, dict) == True else 'unknow'}")
#%%
a = {1, 2, 3}
print(a)
print(f"the type of variable a is {'set' if isinstance(a, set) == True else 'unknow'}")

#%%
# 整数型，和浮点型 没啥注意的东西， float 类型 计算的时候会有精度损失 的问题。

#%%
# 元组型
# 可以 用 len 
# 元组型 变量 是在内存上 不可改变的，可以索引数据

#%%
# 索引 从 0 开始， 0 代表 第一个元素, 负数代表从后往前索引
a = (4, 5, 2, 10)
print(a[0]) # 取 第一个元素
print(a[0:3]) # 取 第一个 到 第三个元素 a[0, 1, 2]. 索引 左面 是被索引到的 但是 索引右边 是不被包括的
print(f"the length of a is {len(a)}")
print(4 in a)
# this code will be wrong.
try:
    a[0] = 19
except:
    print("the error occurred.")
#%%
a = [9, 8, 7, 6]
k = a.pop(0) # 0 代表 弹出 第一个元素 默认 弹出 最后一个元素
print(f"the {k} is popped, the rest is {a}")
a.append(9) # 在 列表的尾部添加 元素
print(a)
print(a + [11, 90]) # + 代表链接
print(a[0])
print(a[1:5])
a[2] = 220
print(a)
print(9 in a)
g = iter(a) # 变成 迭代器
print(next(g))

#%%
# string type
# string like tuple unchage and the same index thing like tuple and list.
a = "123"
b = '234'
c = """jsdf"""
print(a + b + c)
try: 
    b[0] = "23"
except TypeError:
    print("TypeError: 'str' object does not support item assignment")

kk = ".".join([a, b, c])
print(kk)
d = kk.split(".")
print(d)
# %%
