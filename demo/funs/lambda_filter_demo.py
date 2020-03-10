nums = [1, 10, 4, 5, 6, 7, 8, 9]
for n in filter(lambda n: n % 2 == 0, nums):
    print(n)

marks = [56, 80, 44, 95, 46, 37, 88, 79]
for n in filter(lambda n: n > 50, marks):
    print(n)

