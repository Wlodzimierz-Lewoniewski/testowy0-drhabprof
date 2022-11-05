words = input().split()
sentences_count=int(intput())
sentences=[]
for x in range(sentences_count):
    a=input()
    sentences.append(a)

for word in words:
    result=[]
    for num,sentence in enumerate(sentences):
        tokens=sencence.split()
        result.append(tokens.count(word))
    print (result)
