import pickle
import os.path
import re
import sys

import numpy as np

import Utility as U
import NumpyUtility as NU
import wordle


def getString(i, length, cl, chars="abcdefghijklmnopqrstuvwxyz"):
  print(i, length, cl)
  q = i
  string = ""
  for _ in range(length):
    q, r = divmod(q, cl)
    string += chars[r]
  return string


def ff(arr, length, chars, cl, ml):
  # print(i)
  for i in arr:
    print(f"\r {i:>{ml}}/{length**cl}({i/length**cl*100:>7.2%})", end="")
    getString(i, length, chars, cl)


def getAllStringTest(length, chars="abcdefghijklmnopqrstuvwxyz"):
  cl = len(chars)
  ml = len(str(length**cl))
  arr = np.fromfunction(lambda arr: ff(arr, length, chars, cl, ml), (length**cl,), dtype=object)
  print("")
  return arr


def getAllString(length, chars):
  cl = len(chars)
  ml = len(str(length**cl))
  # print(f"\r {i:>{ml}}/{length**cl}({i/length**cl*100:>7.2%})", end="")
  return [getString(i, length, cl, chars) for i in range(length**cl)]


if __name__ == "__main__":

  # if os.path.exists("randomWords.dat"):
  #   with open("randomWords.dat", "rb") as fp:
  #     words = pickle.load(fp)
  # else:
  #   words = getAllString(5, chars)
  #   with open("randomWords.dat", "wb") as fp:
  #     pickle.dump(words, fp)
  # U.printList(words)
  # words = list(filter(lambda x: wordle.filterExclude(x, "eyuiashcb"), words))
  # print(len(words))

  data = getAllStringTest(2)
  NU.npInfo(data, printContent=False)

  # chars = "abcdefghijklmnopqrstuvwxyz"
  # chars = re.sub("[abusechiy]", "", chars)
  # print(chars)
  # words = getAllString(3, chars)
  # words = list(filter(lambda x: wordle.filterSame(x, "l", 1, 2), words))
  # print(len(words))
  # U.printList(words)
