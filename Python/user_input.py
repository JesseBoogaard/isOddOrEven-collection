# the check itself runs at O(1) efficiency. You can't beat this algo. 

def is_odd_or_even(num=False):
    is_even = False
    if not num:
        number = input("Enter your number: ")
        print("your number is " + str(number))

        odd_or_even = input("Is your number odd or even?: ")
        done = False

        while not done:
            if odd_or_even == ("odd" or "Odd" or "ODD"):
                print(str(number) + " is odd")
                done = True
            elif odd_or_even == ("even" or "Even" or "EVEN"):
                print(str(number) + " is even")
                done = True
            else:
                odd_or_even = input("What? Is your number odd or even?: ")
    else:
        number = num
        print("your number is " + str(number))

        odd_or_even = input("Is your number odd or even?: ")
        done = False

        while not done:
            if odd_or_even == ("odd" or "Odd" or "ODD"):
                print(str(number) + " is odd")
                is_even = False
                done = True
            elif odd_or_even == ("even" or "Even" or "EVEN"):
                print(str(number) + " is even")
                done = True
                is_even = True
            else:
                odd_or_even = input("What? Is your number odd or even?: ")
    if is_even == True:
        return "even"
    else:
        return "false"

is_odd_or_even()
is_odd_or_even(8)
print(is_odd_or_even())
