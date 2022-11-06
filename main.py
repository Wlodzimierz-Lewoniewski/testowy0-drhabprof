sentences=[]
sentences_count=int(input())
for x in range(sentences_count):
    a=input()
    sentences.append(a.strip())
words_count = int(input())
words=[]
for x in range(words_count):
    a=input()
    words.append(a.strip())

for word in words:
    result={}
    for num,sentence in enumerate(sentences):
        tokens=sentence.split()
        if word in tokens:
            result[num]=tokens.count(word)
    #print (result)
    print ([x for x in sorted(result, key=result.get, reverse=True)])
