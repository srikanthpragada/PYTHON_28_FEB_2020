from datetime import *

f = open(r"c:\classroom\feb28\players.txt")
players = {}

for line in f:
    parts = line.strip().split("-")
    if len(parts) < 2:
        continue

    name = parts[0].strip()
    try:
        dob = datetime.strptime(parts[1].strip(), "%d%m%Y")
        td = datetime.now() - dob  # Get timedelta
        age = td.days // 365  # Age in years
        players[name] = age
    except:
        pass

for name, age in sorted(players.items(), key=lambda t: t[1]):
    print(f"{name:10} {age:3}")
