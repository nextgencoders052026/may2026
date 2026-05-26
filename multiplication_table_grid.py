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
   
