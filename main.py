words_count = int(input())
words=[]
for x in range(words_count):
  a=input()
  words.append(a.strip())

for word in words:
  if len(word)>2: print (word,len(word))
