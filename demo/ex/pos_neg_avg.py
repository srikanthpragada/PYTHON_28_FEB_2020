# Take numbers from user until 0 is given and display avg of positive and negative numbers

pos_sum = neg_sum = 0
pos_count = neg_count = 0
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
     break  # Terminate loop

    if num > 0:
        pos_sum += num
        pos_count += 1
    else:
        neg_sum += num
        neg_count += 1

print("Positive Avg : ", pos_sum / pos_count)
print("Negative Avg : ", neg_sum / neg_count)
