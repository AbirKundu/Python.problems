t=int(input())
for i in range(t):
    n=input()
    r=n[::-1]
    print(*r)  ### here this star(*) sign before the result prints the number of r with a space 
               ### if r = 123456 and 
               ###output = * r
               ###output = 1 2 3 4 5 6
