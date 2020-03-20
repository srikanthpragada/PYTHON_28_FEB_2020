
sum = 0
while True:
    try:
        num = int(input("Enter a number [0 to stop] :"))
        if num == 0:
            break
        sum += num
    except Exception as ex:
        print(type(ex))
        print(ex)
        print("Invalid Number")

print(sum)

