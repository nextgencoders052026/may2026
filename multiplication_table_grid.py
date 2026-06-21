table=[]
n=int(input())
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