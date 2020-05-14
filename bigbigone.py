#%%
import pandas as pds

#%%
df = pds.read_excel("data.xlsx")

#%%
df.head(2)

#%%
df.groupby(by=["gender"]).count()

# %%
print("我爱你")

# %%
