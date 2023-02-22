class Solution:
  def findDiagonalOrder(self, mat):
    m, n = len(mat), len(mat[0])
    length = m * n
    ans = []
    row, col = 0, 0
    for i in range(length):
      ans.append(mat[row][col])
      if (row + col) % 2 == 0:
        if col == n - 1:
          row += 1
        elif row == 0:
          col += 1
        else:
          row -= 1
          col += 1
      else:
        if row == m - 1:
          col += 1
        elif col == 0:
          row += 1
        else:
          row += 1
          col -= 1
    return ans
