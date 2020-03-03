# Take numbers from user until 0 is given and display sum of numbers

sum = 0
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break  # Terminate loop

    sum += num

print("Sum = ", sum)
