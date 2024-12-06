class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        tmp_sum_max = 0
        for account in accounts:
            tmp_sum = 0
            for i in account:
                tmp_sum += i
            if tmp_sum_max < tmp_sum:
                tmp_sum_max = tmp_sum
        return tmp_sum_max