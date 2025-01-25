a_list = [int(x) for x in input().split()]
flag = "No"

for i in range(len(a_list)-1):
    b_list = a_list.copy()
    b_list[i], b_list[i+1] = b_list[i+1], b_list[i]

    if [1, 2, 3, 4, 5] == b_list:
        flag = "Yes"
        break

print(flag)