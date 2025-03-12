class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        edge_length = len(matrix)
        top = 0
        bottom = edge_length - 1
        while top < bottom:
            for col in range(edge_length):
                matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col]
            top += 1
            bottom -= 1

        for row in range(edge_length):
            for col in range(row+1, edge_length):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        return matrix