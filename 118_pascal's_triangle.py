class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for r in range(numRows):
            cur_row = [1]*(r + 1)

            for cur in range(1, len(cur_row) - 1):
                cur_row[cur] = triangle[r - 1][cur - 1] + triangle[r - 1][cur]
            
            triangle.append(cur_row)
        
        return triangle
