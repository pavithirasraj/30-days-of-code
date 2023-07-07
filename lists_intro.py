# Original method
lst = []
n = int(input())
for i in range(0,n):
    ele = int(input())
    lst.append(ele)
print(lst)

# List comprehension - Efficient method
n = int(input())
lst = list(map(int,input().split()))[:n]
print(lst)

for i in lst:
    print(i,end=' ')
    
print()   
print(*lst)

print(sum(lst))
