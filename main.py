import string
def wordCount():
  s = input("Input sentence: ")
  return len(s.split())

def prepare(s):
  return "".join(filter(lambda k: k in string.ascii_uppercase, s.upper() ))

wordIndices = []

def getAllWords(lst, n, dictionary):
  validWords = []
  # All rows
  for i in range((len(lst))):
    for j in range((len(lst[0])) - n + 1):
      w = "".join(lst[i][j : j + n])
      if w in dictionary or w[::-1] in dictionary:
        validWords.append((w, (i,j)))
        wordIndices.append([(i, j + m) for m in range(n)])
  # All columns
  for j in range((len(lst[0]))):
    for i in range((len(lst)) - n + 1):
      w = ""
      for ind in range(i, i+n):
        w += lst[ind][j]
      if w in dictionary or w[::-1] in dictionary:
        validWords.append((w, (i,j)))
        wordIndices.append([(i + m, j) for m in range(n)])
  return validWords

def readGrid():
  f = open("wordsearch.txt", "r")
  l = f.readlines()
  return [a.strip().split() for a in l]

def readWordsList():
  f = open("wordList.txt", "r")
  l = f.readlines()
  return [prepare(a) for a in l]

grid = readGrid()
wordList = readWordsList()

minLen = min([len(a) for a in wordList])
maxLen = max([len(a) for a in wordList])

for l in range(minLen, maxLen + 1):
  print(getAllWords(grid, l, wordList))

wordIndices = [item for sublist in wordIndices for item in sublist]

for i in range(len(grid)):
  s = ""
  for j in range(len(grid[0])):
    s += ("#" if (i,j) in wordIndices else " ")
  print(s)