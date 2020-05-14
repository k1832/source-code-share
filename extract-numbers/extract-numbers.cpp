#include <iostream>
#include <string>
#include <stack>
using namespace std;
bool have_seen[101];
stack<int> numbers;
int digits[189];
bool dfs(int curr_index) {
  if(curr_index >= 189) return true;
  if(!digits[curr_index]) return false;
  int curr_num = digits[curr_index];
  for(int num_digits = 1; num_digits <= 2; ++num_digits) {
    if(num_digits==2) curr_num = 10*curr_num + digits[curr_index+1];
    if(have_seen[curr_num]) continue;
    have_seen[curr_num] = true;
    if(dfs(curr_index + num_digits)) {
      numbers.push(curr_num);
      return true;
    }
    have_seen[curr_num] = false;
  }
  return false;
}
/***** MAIN *****/
int main() {
  string s; cin >> s;
  for(int i = 0; i < s.size(); ++i) {
    digits[i] = s[i] - '0';
  }
  dfs(0);
  while(!numbers.empty()) {
    cout << numbers.top();
    numbers.pop();
    if(numbers.size()) cout << ",";
  }
  cout << "\n";
  return 0;
}
