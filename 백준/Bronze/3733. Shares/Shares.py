while True:
    try:
        N,S= map(int, input().split())

        num=S//(N+1)
        print(num)
    except:
        break