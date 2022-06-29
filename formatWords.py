from words import Words
import wordle
import json

if __name__ == "__main__":
  data = wordle.uniqueFilter(Words)
  data = sorted(list(map(lambda x: x.lower(), data)))
  data = json.dumps(data, indent="  ")
  data = "Words = " + data
  with open("words.py", "w", newline="\n") as fp:
    fp.write(data)