
class Marks_Iterator:
    def __init__(self,data):
        self.data = data
        self.pos = 0

    def __next__(self):
        if self.pos == len(self.data):
            raise StopIteration
        else:
            self.pos += 1
            return self.data[self.pos - 1]


class Marks:
    def __init__(self):
        self.marks = [20, 30, 40, 25, 66]

    def __iter__(self):
        return Marks_Iterator(self.marks)



m = Marks()
it1 = iter(m)
it2 = iter(m)
print(next(it1), next(it2))

# for v in m:
#     print(v)
