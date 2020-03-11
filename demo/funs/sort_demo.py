nums = [1, 10, 4, -5, -6, 5, 6, 7, 8, -10, 9]

for n in sorted(nums, key=abs):
    print(n)

names = ['Java', 'C#', 'Python', 'Ruby', 'JavaScript', 'C']

for n in sorted(names, key=len):
    print(n)

names = ['  Java ', 'c#', 'Python  ', 'Ruby', ' JavaScript', '  C']

# Ignore case and strip spaces
print(sorted(names, key=lambda s: s.strip().lower()))
