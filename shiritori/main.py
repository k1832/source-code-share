# -*- coding: utf-8 -*-
import os, copy, string
from collections import defaultdict

base = os.path.join(os.getcwd(), "files")
words = {}

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
  if check(sc):
    return shiritori
  shortest = []
  for i in range(min(len(words[sc]), 2)):
    if words[sc][i].have_seen:
      continue
    words[sc][i].have_seen = True
    tmp = copy.copy(shiritori)
    tmp.append(words[sc][i].word)
    new_array = dfs(words[sc][i].word[-1].lower(), copy.copy(tmp))
    words[sc][i].have_seen = False
    if len(new_array) == 0:
      continue
    if len(shortest) == 0 or len(shortest) > len(new_array):
      shortest = copy.copy(new_array)
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
  print("{}: {}".format(c, dfs(c)))
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
      last_letter_best = words[last_letter][0].occur
      word.occur = min(len(words[last_letter]), last_letter_best)
  for first_letter in words:
    words[first_letter].sort(key=lambda word: word.occur)
  for i in range(ord('a'), ord('z')+1):
    solve(chr(i))

if __name__ == "__main__":
  main()
