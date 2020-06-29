# -*- coding: utf-8 -*-
import os, copy, string
import queue
base = os.path.join(os.getcwd(), "files")

MAX_NUM_TO_SEARCH = 2

# words_beginning_with = {"a":[WordWithScore], "b": [WordWithScore], ..., "z": [WordWithScore]}
words_beginning_with = {}

class WordWithScore():
  def __init__(self, word, score=0):
    self.word = word
    self.score = score

def map_dir(current_dir):
  for name in os.listdir(current_dir):
    if os.path.isfile(os.path.join(current_dir, name)):
      first_letter = name[0].lower()
      if not first_letter in words_beginning_with:
        words_beginning_with[first_letter] = []
      words_beginning_with[first_letter].append(WordWithScore(name))
    else:
      map_dir(os.path.join(current_dir, name))

def update_score():
  # 最後の文字で始まる単語数をscoreとして持つ
  # 例："abd"について、"d"から始まる単語数が"abd"のscoreになる
  for first_letter in words_beginning_with:
    for word in words_beginning_with[first_letter]:
      last_letter = word.word[-1].lower()
      word.score = len(words_beginning_with[last_letter])
  # 最初の文字ごとにscoreでソート
  for first_letter in words_beginning_with:
    words_beginning_with[first_letter].sort(key=lambda word: word.score)
  
  # 最後の文字で始まる単語のなかで最もスコアのいいものと自分のスコアを比較
  # 例："abd"について、「"abd"のスコア」と、「"d"で始まる単語の中で最もスコアのいいもの+1」を比較して良い方をscoreとして更新
  for first_letter in words_beginning_with:
    for word in words_beginning_with[first_letter]:
      last_letter = word.word[-1].lower()
      next_best_score = words_beginning_with[last_letter][0].score
      word.score = min([word.score, next_best_score+1])

  # 同じ文字で終わる単語が複数ある場合は、一つに絞る
  for first_letter in words_beginning_with:
    for i in range(len(words_beginning_with[first_letter])-1):
      if words_beginning_with[first_letter][i].word[-1] == words_beginning_with[first_letter][i+1].word[-1]:
        words_beginning_with[first_letter][i+1].score = 100
  
  # 最終的なスコアでソート
  for first_letter in words_beginning_with:
    words_beginning_with[first_letter].sort(key=lambda word: word.score)

def bfs(first_letter):
  q = queue.Queue()
  for word in words_beginning_with[first_letter]:
    q.put([word.word])
  while not q.empty():
    shiritori = q.get()
    nothing_found = True
    last_word = shiritori[-1]
    last_letter = last_word[-1].lower()  # shiritoriで最後に追加されたものの最後の文字の小文字

    # スコアによってソートされたものを、上から最大{MAX_NUM_TO_SEARCH}個試す
    for i in range(min(len(words_beginning_with[last_letter]),MAX_NUM_TO_SEARCH+1)):
      if words_beginning_with[last_letter][i].word in shiritori:
        continue
      nothing_found = False
      tmp = copy.copy(shiritori)
      tmp.append(words_beginning_with[last_letter][i].word)
      q.put(tmp)
    if nothing_found:
      # 本当に次に続く単語がないか探索
      # ある場合は空の配列を返す
      for word in words_beginning_with[last_letter]:
        if not word.word in shiritori:
          return []
      return shiritori
  return []

def main():
  map_dir(base)
  update_score()
  counter = 0
  for i in range(ord('a'), ord('z')+1):
    ans = bfs(chr(i))
    print("{}: {}".format(chr(i), ans))
    counter += len(ans)
  print("counter: {}".format(counter))

if __name__ == "__main__":
  main()
