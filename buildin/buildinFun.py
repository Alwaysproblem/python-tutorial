#%%
# python 有很多内嵌的函数， 先来 介绍一下

#%%[markdown]
# print 函数 在终端控制台打印
# ```
# def print(*values: object, \
#      sep: Text=..., end: Text=..., file: Optional[_Writer]=..., flush: bool=...)
# ```

#%%
a = 123
b = "yyx"
print(a)
print(a, b)
print(a, b, (1, 2, 3))
print(a, b, end="\n\n")
print(a, b, sep="\t")
# with open("kk.txt", "w") as txtfile:
#     print(a, b, file=txtfile)
# %%
# type, isinstance 是判断 变量类型的, isinstance 比较推荐用
a = "123"
b = 123
print(f"the type of a is {type(a)}")
print(f"the type of b is {type(b)}")
print(f"the type of a is str {isinstance(a, str)}")
print(f"the type of b is int {isinstance(b, int)}")

#%%
# max 取最大值， min 最小值， len 长度， abs 绝对值

#%%
a = [1, 2, 3, -1]
print(f"the max value of a is {max(a)}")
print(f"the min value of a is {min(a)}")
print(f"the len value of a is {len(a)}")
print(f"the aboslute value is {abs(-1)}")

#%%
range(1, 10)
print(*range(1, 10))
# %%
