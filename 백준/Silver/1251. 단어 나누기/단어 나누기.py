word = input().strip()
n = len(word)
res=[]

smallest_word = word
for i in range(1, n - 1):
    for j in range(i + 1, n):

        part1 = word[:i][::-1]
        part2 = word[i:j][::-1]
        part3 = word[j:][::-1]
        # 새로운 단어 생성
        new_word = part1 + part2 + part3

        res.append("".join(new_word))

print(min(res))