# %%
s = ""
pat = "Lin"
rx = 0.04
ry = 0.1
for y in range(30, -30, -1):
    for x in range(-30, 30):
        if ((x*rx)**2+(y*ry)**2-1)**3-(x*rx)**2*(y*ry)**3 < 0:
            s += pat[(x-y) % len(pat)]
        elif ((x*rx)**2+(y*ry)**2-1)**3-(x*rx)**2*(y*ry)**3 == 0:
            # s += pat[(x-y) % len(pat)]
            s += "-"
        else:
            s += " "
    s += "\n"
print(s)

# %%
