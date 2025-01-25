n = input()
an = [int(x) for x in input().split()]
flag = "Yes"

x = an[1] / an[0]

for i in range(1, len(an)-1):
  if an[i+1] != x*an[i]:
      flag = "No"

print(flag)