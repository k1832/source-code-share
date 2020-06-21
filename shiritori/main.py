# -*- coding: utf-8 -*-
import os, copy, string
from collections import defaultdict

base = os.path.join(os.getcwd(), "files")
words = {}

counter = 0
word_counter = {}

class Word():
  def __init__(self, word, have_seen, occur = 0):
    self.word = word
    self.have_seen = False
    self.occur = occur

def init_dictionary(current_dir):
  for name in os.listdir(current_dir):
    if os.path.isfile(os.path.join(current_dir, name)):
      first_letter = name[0].lower()
      if not first_letter in words:
        words[first_letter] = []
      words[first_letter].append(Word(name, False))
    else:
      init_dictionary(os.path.join(current_dir, name))

def dfs(sc, shiritori=[]):
  # if check(sc):
  #   return shiritori
  if word_counter[sc] == 0:
    return shiritori
  shortest = []
  for i in range(min(len(words[sc]), 2)):
    if words[sc][i].have_seen:
      continue
    words[sc][i].have_seen = True
    word_counter[sc] -= 1
    tmp = copy.copy(shiritori)
    tmp.append(words[sc][i].word)
    tmp = dfs(words[sc][i].word[-1].lower(), tmp)
    words[sc][i].have_seen = False
    word_counter[sc] += 1
    if len(tmp) == 0:
      continue
    if len(shortest) == 0 or len(shortest) > len(tmp):
      shortest = tmp
  if len(shortest) == 0:
    return []
  return shortest

# その文字から始まる文字列を全部使った時
def check(sc):
  for word in words[sc]:
    if not word.have_seen:
      return False
  return True

def solve(c):
  array = dfs(c)
  global counter
  counter += len(array)
  print("{}: {}".format(c, array))
  for first_letter in words:
    for word in words[first_letter]:
      word.have_seen = False

def main():
  init_dictionary(base)
  for first_letter in words:
    for word in words[first_letter]:
      last_letter = word.word[-1].lower()
      word.occur = len(words[last_letter])
  for first_letter in words:
    words[first_letter].sort(key=lambda word: word.occur)
  for first_letter in words:
    for word in words[first_letter]:
      last_letter = word.word[-1].lower()
      next_best = words[last_letter][0].occur
      word.occur = min([len(words[last_letter]), next_best+1])
  for first_letter in words:
    words[first_letter].sort(key=lambda word: word.occur)
    word_counter[first_letter] = len(words[first_letter])
  
  
  for i in range(ord('a'), ord('z')+1):
    solve(chr(i))
  print("counter: {}".format(counter))

if __name__ == "__main__":
  main()