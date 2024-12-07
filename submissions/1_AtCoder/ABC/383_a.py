n = int(input())
t1 = t2 = v = sum = 0

for i in range(n):
    t2, v = map(int, input().split())
    if sum >= (t2 - t1):
        sum = sum - (t2 - t1) + v
    else:
        sum = v
    t1 = t2
print(sum)