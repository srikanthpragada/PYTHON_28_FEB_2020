def prime(start, end):
    for n in range(start, end + 1):
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                break
        else:
            yield n


for n in prime(100, 200):
    print(n)
