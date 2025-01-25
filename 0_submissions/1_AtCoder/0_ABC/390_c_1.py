imax = jmax = -1
imin = jmin = 10000
flag = "Yes"

h, w = input().split()
h = int(h)
ss = [[1]]*h
for i in range(h):
    ss[i] = input()

for i, s in enumerate(ss):
    for j, m in enumerate(s):
        if m == "#":
            imax = max(imax, i)
            imin = min(imin, i)
            jmax = max(jmax, j)
            jmin = min(jmin, j)

for i, s in enumerate(ss):
    for j, m in enumerate(s):
        if m == ".":
            if i <= imax and i >= imin and j <= jmax and j >= jmin:
                flag = "No"

print(flag)