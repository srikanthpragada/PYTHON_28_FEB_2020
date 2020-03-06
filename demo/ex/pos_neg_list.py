# Insert positive number on the left and negative number on the right 
nums = []
pos = 0
while True:
    n = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break

    if n > 0:
        nums.insert(pos,n)
        pos += 1
    else:
        nums.append(n)


print(nums)