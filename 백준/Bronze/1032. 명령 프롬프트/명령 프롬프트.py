cnt = input()
word = input()
for i in range(1, int(cnt)):
    next = input()
    for j in range(len(word)):
        if next[j] != word[j]:
            word=word[:j]+'?'+word[j+1:]
print(word)