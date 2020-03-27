import threading
from threading import Thread


def print_numbers():
    for i in range(1, 11):
        print(i)


ct = threading.current_thread()
print(ct)

t1 = Thread(target=print_numbers)
t1.start()


print("Count : ", threading.active_count())

for t in threading.enumerate():
    print(t)

t1.join()     # Wait until t1 is terminated
print("The End")
