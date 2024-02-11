count = int(input())
word=list()
for i in range(count):
    word.append(input())

# set 함수로 중복 없애기
word=list(set(word))
# 단어순서로 정렬
word.sort()
# key를 사용해 문자 길이대로 정렬
word.sort(key=len)

for i in word:
    print(i)