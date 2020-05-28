import random
board = [[0] * 10 for i in range(10)]
dy = [2,1,-1,-2,-2,-1,1,2]
dx = [1,2,2,1,-1,-2,-2,-1]
n = 0
def random_dfs(y, x, current):
  if current == n**2: return True
  index_list = list(range(8))
  random_index_list = random.sample(index_list, 8)
  for i in random_index_list:
    next_y = y + dy[i]
    next_x = x + dx[i]
    if next_y < 0 or next_y >= n or next_x < 0 or next_x >= n: continue
    if board[next_y][next_x]: continue
    board[next_y][next_x] = current+1
    if random_dfs(next_y, next_x, current+1): return True
    board[next_y][next_x] = 0
  return False
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
def main():
  global n
  n = int(input())
  board[n-1][n-1] = 1
  dfs(n-1,n-1,1)
  # random_dfs(n-1,n-1,1)
  for i in range(n):
    for j in range(n):
      print("%2d" % board[i][j], end=" ")
    print()
if __name__ == "__main__":
  main()