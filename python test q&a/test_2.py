#  ......question 1......
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5


# n=int(input("entre any no. to print pattern"))
# for i in range(n):
#     for j in range(1,n+1):
#         print(j,end=" ")


#     print()

# ..... Question 2 ............


# n=int(input("entre any no. to print pattern"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")

#     print()


# ...... question 3 .......

# n=int(input("entre any no. to print pattern"))
# number=1
# for i in range(1,n):
#     for j in range(1,i+1):
#         print(number,end=" ")
#         number=number+1
#     print()



# ...... question 4 .......

# n=int(input("entre any no. to print pattern"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j*2,end=" ")
        
#     print()


    # ...... question 5 .......

# n=int(input("entre any no. to print pattern"))
# number=2
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(number,end=" ")
#         number=number+2
#     print()


    

# ....... question 6......
# n=int(input("entre any no. to print pattern"))

# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
        
#     print()


# ...... question 7.....

# n=int(input("entre any no. to print pattern"))

# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(j*2,end=" ")
        
#     print()


# ...... question 8........

# n=int(input("entre any no. to print pattern"))

# for i in range(n):
#     ch='A'
#     for j in range(1,n+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)


#     print()


# ...... question 9.........

# n=int(input("entre any no. to print pattern"))

# for i in range(1,n+1):
#     ch='A'
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)

#     print()



# ...... question 10 .......

# n=int(input("entre any no. to print pattern"))
# number=1
# ch='A'
# for i in range(1,n+1):
    
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#     print()



# ...... question 11.........

# n=int(input("entre any no. to print pattern"))

# for i in range(1,n+1):
#     ch='A'
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+2)

#     print()



# ........Question 12........

# n=int(input("entre any no. to print pattern"))

# for i in range(1,n+1):
#     ch='A'
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
       
#     print()




# ........Question 13.........

# n=int(input("entre any no. to print pattern"))
# ch='A'
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
       
#     print()




# ........Question 14.........

# n=int(input("entre any no. to print pattern"))
# for i in range(1,n+1):
#     ch='A'
#     print(" "*(n-i),end="")
#     for j in range(1,i+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+2)
       
#     print()


# ..... Question 15 ............


# n=int(input("entre any no. to print pattern"))
# for i in range(1,n+1):
#     print('* '*i)


#......Question 16


# n=int(input("entre any no. to print pattern"))
# for i in range(1,n+1):
#     print(" "*(n-i)+'*'*i)
   


# ......Question 17......


# n=int(input("entre any no. to print pattern"))
# for i in range(1,n+1):
#     print(" "*(n-i)+'* '*i)


# ..... Question 18 ............


# n=int(input("entre any no. to print pattern"))
# for i in range(1,n+1):
#     print('* '*((n+1)-i)+" "*i)



# ..... Question 19 ............


n=int(input("entre any no. to print pattern"))
for i in range(1,n+1):
    print(' '*i+ '*'*((n+1)-i))



# .....Question20......
# n=int(input("entre any number"))
# for i in range(1,n+1):
#     print(' '*i+'* '*((n+1)-i))


# .....Question 21....
# n=int(input("entre any number"))
# for i in range(1,n+1):
#     print('* '*i)
# for i in range(1,n+1):
#     print('* '*(n-i)+" "*i)


# .....Question 22.....
# n=int(input("entre any no. to print pattern"))
# i=1
# while i<=n: 
#     print(' '*(n-i)+'*'*i)
#     i=i+1
# i=i-2 
# while i>=1:
#     print(' '*(n-i)+'*'*i)
#     i=i-1


# ......Question 23......


# n=int(input("entre any no. to print pattern"))
# for i in range(1,n+1):
#     print(" "*(n-i)+'* '*i)
# for j in range(1,n+1):
#     print(' '*j+'* '*(n-i))



#......Question 24......
# n=int(input("enter number value:"))
# for i in range(0,n):
#     print(' '*i+'*'*(n-i))
# for i in range(2,n+1):
#     print(' '*(n-i)+'*'*i)





#......Question 25....

# n=int(input("entre any no. to print pattern"))
# for i in range(2,n+1):
#     print('* '*((n+2)-i)+" "*i)
# for i in range(1,n+1):
#     print('* '*i)
