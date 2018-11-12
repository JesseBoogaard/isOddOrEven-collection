from heapq import heappush, heappop

def oddable(x):
    if x < 4:
        return False
    else:
        return 3 * int((x-1) / 3) + 1 == x

def odd(x):
    if x == 1:
        return True


    h = []
    heappush(h, (1, 1))

    visited = {}

    while True:
        val, isOdd = heappop(h)

        visited[val] = None

        even = val * 2;
        if x == even:
            return False
        elif even not in visited:
            heappush(h, (even, 0))

        if isOdd == 0 and oddable(val):
            o = int((val - 1) / 3)

            if x == o:
                return True
            elif o not in visited:
                heappush(h, (o, 1))


if __name__ == '__main__':
    for x in range(1, 1000):
        if odd(x) != x % 2 == 1:
            print(x)

    while True:
        number = int(input("Enter a number: "))
        if odd(number):
            print("{} is odd".format(number))
        else:
            print("{} is even".format(number))

