class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        stck = {}

        for c in magazine:
            if c not in stck:
                stck[c] = 1
            else:
                stck[c] += 1

        for c in ransomNote:
            if c in stck and stck[c] > 0:
                stck[c] -= 1
            else:
                return False
        
        return True