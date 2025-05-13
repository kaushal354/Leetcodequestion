class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0


        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0


        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0



        # return zeros
        return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
getzero = Solution()
print(getzero.setZeroes(matrix))
        