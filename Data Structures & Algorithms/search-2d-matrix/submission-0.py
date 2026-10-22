class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        num_elements = rows * cols
        left, right = 0, num_elements - 1
        return self.binary_search(matrix, rows, cols, left, right, target)

    def binary_search(self, matrix, rows, cols, left, right, target):
        mid = (left + right) // 2
        # find where the element for mid is exactly
        row, col = mid // cols, mid % cols
        if left > right:
            return False
        elif matrix[row][col] == target:
            return True
        else:
            if target < matrix[row][col]:
                return self.binary_search(matrix, rows, cols, left, mid - 1, target)
            else:
                return self.binary_search(matrix, rows, cols, mid + 1, right, target)