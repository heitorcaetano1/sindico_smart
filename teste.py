def solution(grid):
    m, n = len(grid), len(grid[0])
    result = ''
    for diagonal in range(m + n - 1):
        if diagonal < m:
            i = diagonal
            j = 0
        else:
            i = m - 1
            j = diagonal - m + 1
        while i >= 0 and j < n:
            result += grid[i][j]
            i -= 1
            j += 1
    return result

grid = [
  ['a', 'b', 'c', 'd'],
  ['e', 'f', 'g', 'h'],
  ['i', 'j', 'k', 'l']
]

print(solution(grid))  # Use a função correta aqui
