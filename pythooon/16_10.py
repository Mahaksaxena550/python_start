while(True):
    print("1. addition \n 2. substraction \n 3. multiply \n 4. divide \n 5. off")
    n=int(input("please entre any of one option:"))

    if n in (1,2,3,4,5):
        if n in (1,2,3,4):
            if n==1:
                sum,l=0,[]
                n=int(input("entre how many no. you want to add"))
                for i in range(1,n+1):
                    value = int(input(f'enter {i} value:'))
                    l.append(value)
                    sum=sum+value
                print(f'sum of given value {l} is {sum}')

            elif n==2:
                sub,l=0,[]
                n=int(input("entre how many no. you want to subtract"))
                for i in range(1,n+1):
                    value=int(input(f'entre {i} value:'))
                    if i==1:
                        sub=value
                        l.append(value)
                    else:
                        sub=sub-value
                        l.append(value)       
                print(f'sub of given value {l} is {sub}')
            
            elif n==3:
                mul,l=1,[]
                n=int(input("enter how many no. you want to multiply"))
                for i in range (1,n+1):
                    value=int(input (f'entre {i} value:'))
                    mul=mul*value
                    l.append(value)
                print(f'sub of given value {l} is {mul}')

            elif n==4:
                div,l=1,[]
                n=int(input("enter how many no. you want to multiply"))
                for i in range (1,n+1):
                    value=int(input (f'entre {i} value:'))
                    if i==1:
                        div=value
                        l.append(value)
                    else:
                        div=div//value
                        l.append(value)

                    
                print(f'sub of given value {l} is {div}')




        else:
            break
    else:
        print("please select any vslid option")
