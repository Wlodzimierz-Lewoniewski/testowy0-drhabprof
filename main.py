words = input().split()
sentences_count=int(input())
sentences=[]
for x in range(sentences_count):
    a=input()
    sentences.append(a)

for word in words:
    result={}
    for num,sentence in enumerate(sentences):
        tokens=sentence.split()
        if word in tokens:
            result.append(tokens.count(word))
    print (result)
