#include <iostream>
using namespace std;
const int dy[] = {2,1,-1,-2,-2,-1,1,2}, dx[] = {1,2,2,1,-1,-2,-2,-1};
int n, board[10][10];
bool dfs(int y, int x, int current) {
  if(current == n*n) return true;
  for(int i = 0; i < 8; ++i) {
    int next_y = y + dy[i], next_x = x + dx[i];
    if(next_y < 0 || next_y >= n || next_x < 0 || next_x >= n) continue;
    if(board[next_y][next_x]) continue;
    board[next_y][next_x] = current+1;
    if(dfs(next_y, next_x, current+1)) return true;
    board[next_y][next_x] = 0;
  }
  return false;
}
int main() {
  cin >> n;
  board[n-1][n-1] = 1;
  dfs(n-1, n-1, 1);
  for(int i = 0; i < n; ++i) {
    for(int j = 0; j < n; ++j) {
      printf("%2d ", board[i][j]);
    }
    cout << "\n";
  }
}