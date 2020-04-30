#include <bits/stdc++.h>
using namespace std;

using ll = long long;
#define int long long
using P = pair<int, int>;

#define LOG(variable) cout << #variable":\t" << (variable) << endl
#define LOGCON(i, container) for(int (i) = 0; (i) < (container).size(); ++(i)) cout << (i) << ":\t" << (container)[(i)] << endl
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPS(i, r, n) for (int i = (r); i < (n); ++i)
#define REPR(i, n) for(int i = (n); i >= 0; --i) // from n to 0
#define REPRS(i, n, r) for(int i = (n); i >= (r); --i) // from n to r
#define REPOBJ(itr, obj) for(auto itr = (obj).begin(); itr != (obj).end() ; ++itr)
#define REPROBJ(itr, obj) for(auto itr = (obj).rbegin(), e = (obj).rend(); itr != e; ++itr)
#define COUTB(x) cout << (x) << "\n"
#define COUTS(x) cout << (x) << " "
#define PB push_back
#define SORT(obj) sort((obj).begin(), (obj).end())
#define SORTR(obj) sort((obj).begin(), (obj).end(), greater<>())
#define ALL(obj) (obj).begin(), (obj).end()
#define MOD 1000000007
#define PI (acos(-1))

int in() {int x; cin>>x; return x;}
string stin() {string s; cin>>s; return s;}

string solve(string s) {
  auto pos = s.find("[");
  if(pos==string::npos) return s;

  string repeat_count_s = "";
  int i = pos-1;
  while(i >= 0 && ('0' <= s[i] && s[i] <= '9')) {
    repeat_count_s = s[i] + repeat_count_s;
    --i;
  }
  int repeat_count = stoi(repeat_count_s);
  string before_s = i>=0
    ? s.substr(0,i+1)
    : "";

  int rest_bracket = 1;
  i = pos+1;
  string inside_bracket = "";
  while(rest_bracket > 0) {
    if(s[i] == ']') --rest_bracket;
    else if(s[i] == '[') ++rest_bracket;
    if(rest_bracket > 0) inside_bracket += s[i];
    ++i;
  }
  string after_s = i < s.size()
    ? s.substr(i)
    : "";
  inside_bracket = solve(inside_bracket);
  string middle_s = inside_bracket;
  for(int i = 0; i < repeat_count-1; ++i) {
    middle_s += inside_bracket;
  }
  return before_s + middle_s + solve(after_s);
}

/***** MAIN *****/
signed main() {
  string s = stin();
  cout << solve(s);
  cout << "\n";
  return 0;
}
/***** MAIN *****/
