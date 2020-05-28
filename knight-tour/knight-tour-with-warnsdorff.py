import sys
board = [[0] * 30 for i in range(30)]
dy = [2,1,-1,-2,-2,-1,1,2]
dx = [1,2,2,1,-1,-2,-2,-1]
n = 0

def get_num_next_candidates(y, x):
  ret = 0
  for i in range(8):
    next_y = y + dy[i]
    next_x = x + dx[i]
    if next_y < 0 or next_y >= n or next_x < 0 or next_x >= n: continue
    if board[next_y][next_x]: continue
    ret += 1
  return ret

def dfs(y, x, current):
  if current == n**2: return True
  candidates = []
  for i in range(8):
    next_y = y + dy[i]
    next_x = x + dx[i]
    if next_y < 0 or next_y >= n or next_x < 0 or next_x >= n: continue
    if board[next_y][next_x]: continue
    num_next_candidates = get_num_next_candidates(next_y, next_x)
    candidates.append([next_y, next_x, num_next_candidates-1])
  candidates = sorted(candidates, key = lambda x: x[2])
  for candidate in candidates:
    board[candidate[0]][candidate[1]] = current+1
    if dfs(candidate[0], candidate[1], current+1): return True
    board[candidate[0]][candidate[1]] = 0
  return False

def main():
  global n
  n = int(input())
  if n > 30:
    print("It can't solve the problem with the number that is greater than 30.")
    sys.exit(1)
  board[n-1][n-1] = 1
  dfs(n-1,n-1,1)
  for i in range(n):
    for j in range(n):
      if n < 10: print("%2d" % board[i][j], end=" ")
      else: print("%3d" % board[i][j], end=" ")
    print()
if __name__ == "__main__":
  main()