class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        i = 0
        middle = 0

        while i < numRows:
            j = 0
            row = []
            
            while j <= i:
                if j == 0:
                    row.append(1)
                elif j == i:
                    row.append(1)
                else:
                    middle = triangle[i - 1][j - 1] + triangle[i - 1][j]
                    row.append(middle)
                j = j + 1
            triangle.append(row)
            i = i + 1
        return triangle