s=input()                    # input = 351 as string
sum=0 
for i in s:
    if i.isdigit():
        sum = sum + int(i)
print(sum)                   # output = 9 (3+5+1)
