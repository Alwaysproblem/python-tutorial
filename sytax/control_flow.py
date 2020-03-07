#%%
# for loop
# for 变量 in 列表：
#    表达式
# else:
    # 表达式

#%%
for i in [1, 3, 4]:
    print(i)

#%% 或者 字符串
for c in "1234":
    print(c)

#%% 或者字符串 
table = {"first": "I", "second": "love", "third": "you"}
for key in table:
    print(f"{key}: {table[key]}")

#%% 或者 tuple
for i in (1, 2, 3):
    print(i)

#%%
print("==" * 20)
for i in (1, 2, 4):
    print(i)
else:
    print("end of loop")

#%% while loop
print("==" * 20)
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print(i)

#%% inner loop
print([-i for i in (0, 1, 2, 3, 4)])
print([-i for i in (0, 1, 2, 3, 3, 4) if i != 3])

#%%
con = {str(i): len(i) for i in ["I", "love", "you"]}
print(con)
# %% tuple and string is the same as above.

# %%
################################################
# %%
# if 条件句
# if 条件:
    # 表达式
#   else:
    #   表达式

# 或者：
# if expression:
#     pass
# elif expression:
#     pass
# else:
#     pass
#%%
if "I" == "I":
    print(f"'T' = 'T': {True}")
else:
    print(f"'T' = 'T': {False}")

# %%
day = "Monday"

if day == "Monday":
    print(day)
elif day == "Tuesday":
    print(day)
elif day == "Wednesday":
    print(day)
elif day == "Thursday":
    print(day)
elif day == "Friday":
    print(day)
elif day == "Saturday":
    print(day)
elif day == "Sunday":
    print(day)
else:
    print("None")

# %%
