
import sys

if len(sys.argv) < 2:
    print("Missing number!")
    exit(0)     # stop program

num = int(sys.argv[1])

for i in range(1,11):
    print(f"{num:3} * {i:2} = {num * i:4}")


