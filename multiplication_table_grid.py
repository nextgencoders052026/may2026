<<<<<<< HEAD
while True:
    print('Enter number for multiplication grid')
    table=[]
    n=int(input())
    if n>10:
        print('Column width is getting too large. Enter a smaller number')
    else:
        for row in range(1,n+1):
            list_of_row=[]
            for column in range(1,n+1):
                mul=row*column
                list_of_row.append(mul)
            table.append(list_of_row)
    for list_of_row in table:
        string_row=[]
        for num in list_of_row:
            string_row.append(str(num).ljust(n))
        print("".join(string_row))
    print('Do you want to continue?')
    while True:
        answer=input()
        if answer=='no':
            print('Done!')
            continue
        elif answer=='yes':
            print('Alright lets go again')
            break
=======
print('welcome to the multiplication table grid generator!')
while True:
    print('please enter a number to get the multiplication table grid:')
    num=int(input())
    for i in range(1,num+1):
        tablerow=[]
        for j in range(1,num+1):
            a=i*j
            tablerow.append(str(a))
        result=' '.join(tablerow)
        print(result)
    print('do you want to continue? (y/n)')
    choice=input()  
    if choice.lower()=='n':
        print('thank you for using the multiplication table grid generator!')
        break
   
>>>>>>> e0a3dae804321468c3600f5ed7d34c220e35923c
