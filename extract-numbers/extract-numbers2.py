from collections import defaultdict
element_list = []
digit_list = []
have_seen = defaultdict(lambda: False)
def dfs(current_i):
  if current_i >= len(digit_list): return True
  if digit_list[current_i] == 0: return False
  num = digit_list[current_i]
  if not have_seen[num]:
    have_seen[num] = True
    if dfs(current_i+1):
      element_list.append(num)
      return True
    have_seen[num] = False
  num *= 10
  num += digit_list[current_i+1]
  if have_seen[num]: return False
  have_seen[num] = True
  if dfs(current_i+2):
    element_list.append(num)
    return True
  have_seen[num] = False
  return False
def main():
  string = str(input())
  global digit_list
  digit_list = [int(i) for i in string]
  dfs(0)
  element_list.reverse()
  print(element_list)
if __name__ == "__main__":
  main()
