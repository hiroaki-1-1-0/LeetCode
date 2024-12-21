class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if not(i % 3):
                if not(i % 5):
                    ans.append("FizzBuzz")
                    continue
                ans.append("Fizz")
                continue
            elif not(i % 5):
                ans.append("Buzz")
                continue
            ans.append(str(i))
        return ans