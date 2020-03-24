f = open(r"c:\classroom\feb28\students.txt", "rt")

students = {}

for line in f.readlines():
    parts = line.strip().split(",")
    total = sum(map(int, parts[1:]))  # get total for marks
    students[parts[0]] = total  # add name and total

f.close()

for n, t in sorted(students.items()):
    print(f"{n:10}  {t}")

for n, t in sorted(students.items(), key=lambda t: t[1]):
    print(f"{n:10}  {t}")
