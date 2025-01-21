# "a" means "Try Again, Later"
n = input()
stones = [int(x) for x in input().split()]

for i in range(len(stones)):
    for j in range(i):
        if stones[j] > 0:
            stones[j] -= 1
            stones[i] += 1

ans = ""
for stone in stones:
    ans += str(stone) + " "
ans = ans.strip()

print(ans)