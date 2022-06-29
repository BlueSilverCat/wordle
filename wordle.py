import sys
from words import Words


def printList(lst):
  length = len(lst)
  maxLen = len(str(length))
  print(length)
  for i in range(length):
    print(f"{i:>{maxLen}}: {lst[i]}")


def uniqueFilter(lt):
  length = len(lt)
  return [lt[i] for i in range(length) if lt.index(lt[i]) == i]


def filterSame(x, chars, start, end):
  if x[start:end] == chars:
    return True
  return False


def filterNotSame(x, chars, start, end):
  if x[start:end] == chars:
    return False
  return True


def filterInclude(x, chars):
  count = 0
  for char in chars:
    if char in x:
      count += 1
  if count == len(chars):
    return True
  return False


def filterExclude(x, chars):
  for char in chars:
    if char in x:
      return False
  return True


def getData(data):
  return sorted(uniqueFilter([datum.lower() for datum in data]))


def filterChars(data, params):
  result = data
  if params[0] == "end":
    sys.exit(0)
  if params[0] == "i":
    result = list(filter(lambda x: filterInclude(x, params[1]), data))
  elif params[0] == "e":
    result = list(filter(lambda x: filterExclude(x, params[1]), data))
  elif params[0] == "s":
    start, end = params[2].split(":")
    result = list(filter(lambda x: filterSame(x, params[1], int(start), int(end)), data))
  elif params[0] == "n":
    start, end = params[2].split(":")
    result = list(filter(lambda x: filterNotSame(x, params[1], int(start), int(end)), data))
  return result


if __name__ == "__main__":
  data = getData(Words)
  text = ""
  printList(data)
  while len(data) > 0:
    text = input("[iesn] chars [n:m]: ")
    param = text.split(" ")
    data = filterChars(data, param)
    printList(data)
