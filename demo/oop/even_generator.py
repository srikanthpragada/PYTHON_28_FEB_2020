def even_numbers(num):
    for i in range(2, num + 1, 2):
        yield i


print(type(even_numbers(20)))

en = even_numbers(10)
print(next(en))
print("Next value")
print(next(en))

# for n in even_numbers(20):
#     print(n, end=' ')
