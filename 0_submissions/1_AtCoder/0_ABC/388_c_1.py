import bisect

n = input()
mochis = [int(x) for x in input().split()]
cntr = 0

for i, mochi1 in enumerate(mochis):
    index = bisect.bisect_left(mochis, mochi1*2)
    if index < len(mochis):
        cntr += len(mochis) - index

print(cntr)