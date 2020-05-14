from collections import defaultdict
have_seen = defaultdict(lambda: False)
element_list = []
def dfs(string):
  if not string: return True
  if string[0] == '0': return False
  for i in range(1, min(2,len(string))+1):
    sub_string = string[:i]
    if have_seen[sub_string]: continue
    have_seen[sub_string] = True
    if dfs(string[i:]):
      element_list.append(sub_string)
      return True
    have_seen[sub_string] = False
  return False
def main():
  string = str(input())
  dfs(string)
  element_list.reverse()
  print(element_list)
if __name__ == "__main__":
  main()