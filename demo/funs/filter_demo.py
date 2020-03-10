def iseven(n):
    print("Checking ", n)
    return n % 2 == 0


nums = [1, 10, 4, 5, 6, 7, 8, 9]
even_nums = filter(iseven, nums)
nums.append(20)

print("About to print!")
for n in even_nums:
    print(n)

#for c in filter(str.isupper, "This IS fine"):
#    print(c)
