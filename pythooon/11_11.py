# #  //// to count digits of a number///

# n=int(input("entre to count digit  "))
# orignal_no = n
# tg=0

# # tg is total number

# while n>0:
#     tg=tg+1
#     n=n//10
# print(f'given number {orignal_no} digit is {tg}')


n = int(input("entre a no.  to find amrstrom"))
orignal_no =p=q= n
sum=tg=0
while n>0:
    tg=tg+1
    n=n//10
while p>0:
    last_digit=p%10
    sum=sum+last_digit**tg
    p=p//10
if q==sum:
    print("armstrong")
else:
    print("not armstrong")


