# Print odd elements in a list
n=int(input())
lst=list(map(int,input().split()))[:n]
for i in lst:
    if i%2 != 0:
        print(i, end =' ')

print()
for i in range(0,n):
    if(lst[i]%2 != 0):
        print(lst[i],end=' ')

print()
# Print elements in odd index
for i in range(0,n):
    if i%2 != 0:
        print(lst[i],end=' ')
