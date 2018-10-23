import itertools

def isOdd(n, oddNumbers=[]):
    
    if oddNumbers == []:
        for x in list(itertools.chain(range(100000))):
            if str(x)[-1] == '1':
                oddNumbers.append(str(x)[-1])

            if str(x)[-1] == '2':
                pass
            
            if str(x)[-1] == '3':
                oddNumbers.append(str(x)[-1])

            if str(x)[-1] == '4':
                pass

            if str(x)[-1] == '5':
                oddNumbers.append(str(x)[-1])

            if str(x)[-1] == '6':
                pass

            if str(x)[-1] == '7':
                oddNumbers.append(str(x)[-1])

            if str(x)[-1] == '8':
                pass

            if str(x)[-1] == '9':
                oddNumbers.append(str(x)[-1])

    oddNumbers = sorted(list(set(oddNumbers)))
    maxOddNumber = int(oddNumbers[-1])

    m = str(n)
    s = m[0]

    if s == '-':
        return isOdd(int(m[1:]), oddNumbers)

    if n > maxOddNumber:
        return isOdd(int(m[1:]))

    for number in oddNumbers:
        if m == number:
            # Double-check just in case
            return int(m) % 2 != 0

    return False


if __name__ == '__main__':
    while True:
        number = int(input("Enter a number: "))
        if isOdd(number):
            print("{} is odd".format(number))
        else:
            print("{} is even".format(number))
    
    
    
