color_num = [[0, 1], [1, 10], [2, 100], [3, 1000], [4, 10000], [5, 100000], [6, 1000000], [7, 10000000], [8, 100000000], [9, 1000000000]]
color={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}

first=input()
second=input()
third=input()

add=color[first]*10+color[second]
result=add*color_num[color[third]][1]

print(result)