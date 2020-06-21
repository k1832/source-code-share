from tabulate import tabulate
def dfs(y, x, current):
  if current == n**2: return True
  for i in range(8):
    next_y = y + dy[i]
    next_x = x + dx[i]
    if next_y < 0 or next_y >= n or next_x < 0 or next_x >= n: continue
    if board[next_y][next_x]: continue
    board[next_y][next_x] = current+1
    if dfs(next_y, next_x, current+1): return True
    board[next_y][next_x] = 0
  return False
n = int(input())
board = [[0] * n for i in range(n)]
dy = [2,1,-1,-2,-2,-1,1,2]
dx = [1,2,2,1,-1,-2,-2,-1]
board[n-1][n-1] = 1
dfs(n-1,n-1,1)
print(tabulate(board,tablefmt="grid"))