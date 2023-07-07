#Slicing

s = input().strip()
# Reversing a string
new_s = s[::-1]
print(new_s)

# Print the last k values of a string
s = input().strip()
k = int(input())
new_s = s[::-1]
# abc ==> cba | k = 2 ==> cb
print(new_s[:k])

# Print the last k values of a string - Simplified
s = input().strip()
k = int(input())
print((s[::-1])[:k])

# Skip last k values of a string and print the rest
s = input().strip()
k = int(input())
new_s = s[::-1]
print(new_s[k:])

# Print first k values of a string
s=input().strip()
k=int(input())
print(s[:k])

# Skip first k values of a string and print the rest
s=input().strip()
k=int(input())
print(s[k:])
