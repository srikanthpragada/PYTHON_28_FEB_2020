def iseven(n):
    """
    Checks whether the given number is even

    :param n: number to be checked for even
    :return: true for even number and false for odd number
    """
    return n % 2 == 0


def isodd(n):
    return n % 2 == 1


# Testing - run when module is executed a script
if __name__ == '__main__':
    print(iseven(10), isodd(11))
else:
    print("Importing ", __name__)
