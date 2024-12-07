# Time Limit Exceeded: O(n^2)
class Solution(object):
    def firstUniqChar(self, s: str) -> int:
        encount = []
        for i, c_i in enumerate(s):
            flag = False
            for j, c_j in enumerate(s[i+1:]):
                if c_i == c_j:
                    flag = True
                    encount.append(j+i+1)
            if flag == False and not i in encount:
                return i
        return -1