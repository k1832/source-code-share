# -*- coding: utf-8 -*-
import os, copy, string
import queue
base = os.path.join(os.getcwd(), "files")

# alphabets = {"a":{"words": [WordCard], "num_available": len(alphabets["a"]["words"])}}
alphabets = {}

class WordCard():
  def __init__(self, word, have_seen, score=0):
    self.word = word
    self.have_seen = False
    self.score = score

def init_dictionary(current_dir):
  for name in os.listdir(current_dir):
    if os.path.isfile(os.path.join(current_dir, name)):
      first_letter = name[0].lower()
      if not first_letter in alphabets:
        alphabets[first_letter] = {}
      if not "words" in alphabets[first_letter]:
        alphabets[first_letter]["words"] = []
      alphabets[first_letter]["words"].append(WordCard(name, False))
    else:
      init_dictionary(os.path.join(current_dir, name))

def update_score():
  for key in alphabets:
    alphabets[key]["num_available"] = len(alphabets[key]["words"])
    for word in alphabets[key]["words"]:
      last_letter = word.word[-1].lower()
      word.score = len(alphabets[last_letter]["words"])
  for key in alphabets:
    alphabets[key]["words"].sort(key=lambda word: word.score)
  
  for key in alphabets:
    for word in alphabets[key]["words"]:
      last_letter = word.word[-1].lower()
      next_best_score = alphabets[last_letter]["words"][0].score
      word.score = min([word.score, next_best_score+1])

  # 末尾が同じものは1つでいい
  for key in alphabets:
    for i in range(len(alphabets[key]["words"])-1):
      if alphabets[key]["words"][i].word[-1] == alphabets[key]["words"][i+1].word[-1]:
        alphabets[key]["words"][i+1].score = 100
  for key in alphabets:
    alphabets[key]["words"].sort(key=lambda word: word.score)

def bfs(sc):
  q = queue.Queue()
  for word in alphabets[sc]["words"]:
    q.put([word.word])
  while not q.empty():
    shiritori = q.get()
    found_nothing = True
    lc = shiritori[-1][-1].lower()  # shiritoriで最後に追加されたものの最後の文字の小文字
    for i in range(min(len(alphabets[lc]["words"]),2)):
      if alphabets[lc]["words"][i].word in shiritori:
        continue
      found_nothing = False
      tmp = copy.copy(shiritori)
      tmp.append(alphabets[lc]["words"][i].word)
      q.put(tmp)
    if found_nothing:
      return shiritori
  return []

def solve(c):
  array = bfs(c)
  for key in alphabets:
    for word in alphabets[key]["words"]:
      word.have_seen = False
  return array

def main():
  init_dictionary(base)
  update_score()
  counter = 0
  for i in range(ord('a'), ord('z')+1):
    ans = solve(chr(i))
    print("{}: {}".format(chr(i), ans))
    counter += len(ans)
  print("counter: {}".format(counter))

if __name__ == "__main__":
  main()
