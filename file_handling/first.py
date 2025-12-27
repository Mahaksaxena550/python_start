# f=open('a1.txt','a')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.writable())
# print(f.readable())
# print(f.closed)


# ......... 08/11/2025...........

# f=open('a2.txt','a')
# data='''this is python class'''
# f.write(data)
# f.close()

# ...... or .......

# f=open('a2.txt','a')
# data='''this is 
#            python 
#                   class'''
# f.write(data)
# f.close()


# f=open('a2.txt','a')
# data=['python\n','java\n','php\n']
# f.write("hello\n")
# f.write("welcome")
# f.writelines(data)
# f.close()




# f=open('a2.txt','a')
# data="python"
# data1="this is python"
# data2='''this is
#               python
#                     class'''
# f.write(data)
# f.write(data1)
# f.write(data2)
# f.close()


# f=open('a3.txt','a')
# data='python\n'
# data1='this is python\n'
# data2='''this is
#               python 
#                    class\n'''
# f.writelines([data,data1,data2])
# f.close



# f=open('a2.txt')
# all_data=f.read(10)
# print(all_data)
# data=f.read()
# print(data)
# f.close()


# f=open('a2.txt')
# data=f.readlines()
# print(data)
# f.close()

# .....open with ......

# with open('a1.txt','a') as f:
#     data ="this is python class"
#     f.write(data)
#     print(f.closed)

# print(f.closed)



#.... cursor movement ....

with open ('a1.txt','rb') as f:
    print(f.tell())
    print(f.seek(5))
    data=f.read(10)
    print(data)
    print(f.tell())
    f.seek(-3,1)