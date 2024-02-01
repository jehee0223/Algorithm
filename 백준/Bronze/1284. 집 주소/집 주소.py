while(1):
    num = input()
    if(num=="0"):
        break
    blank = len(num) + 1

    num_check = list(map(int, str(num)))

    for i in num_check:
        if (i == 0):
            blank += 4
        elif (i == 1):
            blank += 2
        else:
            blank += 3
    print(blank)