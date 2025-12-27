n=int(input('entre any value'))
i,sum=1,0
# while(i<=n):
#     print(i,end=',')
#     i=i+1

while(i<=n):
    sum=sum*i
    if i<=(n-1):
        print(i,end='*')
    else:
        print(i,end='=')
    i=i+1
print(sum)
   
   