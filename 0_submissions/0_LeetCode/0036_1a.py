class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardMap = collections.defaultdict(list)
        for i in range(9):
            for j in range(9):
                digit = board[i][j]
                if digit != '.':
                    if digit in boardMap:
                        for x, y in boardMap[digit]:
                            if i==x or j==y or (i//3==x//3 and j//3==y//3):
                                return False
                    boardMap[digit].append([i,j])
        return True