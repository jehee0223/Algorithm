import queue
import sys

cards=queue.Queue()
N=int(sys.stdin.readline())
for i in range(1,N+1):
    cards.put(i)

while True:
    if cards.qsize()>1:
        cards.get()
        cards.put(cards.get())
    else:
        print(cards.get())
        break