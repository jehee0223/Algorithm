N=int(input())
F=int(input())

N_s=str(N)[:-2]
N_i=int(N_s)*100
for i in range(F):
    if((N_i+i)%F==0):
        N_i=N_i+i
        N_i%=100
        break
if(N_i//10==0):
    print("0"+str(N_i))
else:
    print(str(N_i))