class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        stck = {}

        for c in list(map(chr, range(ord('a'), ord('z')+1))):
            stck[c] = 0
        
        for c in magazine:
            stck[c] += 1
        
        for c in ransomNote:
            stck[c] -= 1
        
        for c in list(map(chr, range(ord('a'), ord('z')+1))):
            if stck[c] < 0:
                return False
        
        return True