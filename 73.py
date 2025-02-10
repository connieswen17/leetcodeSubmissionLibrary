class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append((i, j))
        
        for (a, b) in zeroes:
            for k in range(0, len(matrix)):
                matrix[k][b] = 0
            for l in range(0, len(matrix[a])):
                matrix[a][l] = 0
