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