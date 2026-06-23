while True:
    print('Please enter a number to get the multiplication table grid:')
    num=int(input())
    for i in range(1,num+1):
        tablerow=[]
        for j in range(1,num+1):
            a=i*j
            tablerow.append(f"{a:4}")
        result=' '.join(tablerow)
        print(result)
    print('Do you want to continue? (y/n)')
    choice=input()  
    if choice.lower()=='n':
        print('Thank You for using the multiplication table grid generator!')
        break