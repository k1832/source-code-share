import re
def getRepeatedString(repeat_count, string):
  orig_string = string
  for i in range(repeat_count-1):
    string += orig_string
  return string

def decodeString(s):
  # 最初の"["の位置を取得
  first_opening_bracket_index = s.find('[')
  if first_opening_bracket_index < 0:
    return s
  first_num_index = re.search(r'\d', s).start()
  
  # 最初の繰り返し数と、それより左の文字列を取得
  repeat_count = int(s[first_num_index : first_opening_bracket_index])
  left_string = s[:first_num_index]

  # 最初の"["に対応する"]"のindexを取得
  num_left_brackets = 1
  i = first_opening_bracket_index + 1
  while(num_left_brackets > 0):
    if s[i] == "[": num_left_brackets += 1
    elif s[i] == "]": num_left_brackets -= 1
    i += 1
  first_closing_bracket_index = i-1

  # 最初の"[]"より後の文字列
  right_string = s[i:] if i < len(s) else ""

  # 最初の"[]"の中身
  s_inside_brackets = s[first_opening_bracket_index+1 : first_closing_bracket_index]

  # 最初の"[]"内を解決
  middle_string = getRepeatedString(repeat_count, decodeString(s_inside_brackets))
  return left_string + middle_string + decodeString(right_string)

def main():
  in_s = input()
  print(decodeString(in_s))
if __name__ == "__main__":
  main()
