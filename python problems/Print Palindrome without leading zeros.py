
N=input()   #we can take as a string
p=N[::-1]   # reverse it using[::-1]

print(int(p)) #as we working with integers so using int() function will delete leading zeros 2500 => 52
if N==p:
    print("YES")
else:
    print("NO")

