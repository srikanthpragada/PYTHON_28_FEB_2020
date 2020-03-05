# Count no. of uppercase letters in the given string
count = 0
s = input("Enter a string :")
for c in s:
    if c.isupper():
        count +=1

print("Count = ", count)
