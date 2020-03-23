f = open(r"c:\classroom\feb28\names.txt", "r")

names = []

for line in f.readlines():
    # split line by ,
    parts = line.strip().split(",")
    # print(len(parts))
    for name in parts:
        name = name.strip()
        if len(name) > 0:
            names.append(name)

f.close()

for name in sorted(names):
    print(name)
