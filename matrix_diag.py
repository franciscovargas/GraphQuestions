class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        out = []
        diag = 0
        x, y = 0, 0
        while len(out) != m*n:
            out.append(matrix[x][y])
            if min(diag, n-1) == y and diag % 2 == 0:
                if y  + 1 <  n:
                    y += 1
                else:
                    x += 1
                diag += 1
            elif  x == min(diag, m-1) and diag % 2 != 0:
                if  x + 1 < m:
                    x += 1
                else:
                    y += 1
                diag += 1
            elif y != min(diag, n-1) and diag % 2 == 0:
                x -= 1
                y += 1
            elif x  != min(diag, m-1) and diag % 2 != 0:
                x += 1
                y -= 1

        return out
