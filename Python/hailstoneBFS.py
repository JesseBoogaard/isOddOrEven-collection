from heapq import heappush, heappop

def oddable(x):
    if x < 4:
        return False
    else:
        val = int((x - 1) / 3)
        if (3 * val + 1 == x):
            # shhh
            return val % 2 == 1
        else:
            return False

def odd(x):
    if x == 1:
        return True

    visited = {}

    h = []

    heappush(h, 1)

    while True:
        val = heappop(h)

        visited[val] = None

        even = val * 2;

        if x == even:
            return False
        elif even not in visited:
            heappush(h, even)

        if oddable(val):
            o = int((val - 1) / 3)

            if x == o:
                return True
            elif o not in visited:
                heappush(h, o)


if __name__ == '__main__':
    for x in range(1, 100):
        if odd(x) != x % 2 == 1:
            print(x)

    while True:
        number = int(input("Enter a number: "))
        if odd(number):
            print("{} is odd".format(number))
        else:
            print("{} is even".format(number))

