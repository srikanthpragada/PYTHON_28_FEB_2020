
sum = count = 0
while True:
    try:
        num = int(input("Enter a number [0 to stop] :"))
        if num == 0:
            break
        sum += num
        count += 1
    except Exception as ex:
        print("Invalid Number")

print(f"Average = {sum/count}")

