
# draw_line(10,'*')

def draw_line(len=10, char='-'):
    for i in range(len):
        print(char, end='')


draw_line(10, '*')
print(type(10), type(draw_line))
