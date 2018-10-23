import math

def isEven(number):
    # handeling negative numbers
    try:
        result = math.sqrt(number)
    except:
        number *= -1

    number = str(number)
    number = list(number)


    # getting the last number 
    for i in range(len(number)):
        lastNum = number[i]

    loopGoingCondition = "True"
    while loopGoingCondition == "True" and loopGoingCondition == "False":
        if(lastNum != "1" and lastNum != "0"):
            lastNum = str(int(lastNum)-2)
        else:
            loopGoingCondition = "False"
    try:
        result = 1/(1-int(lastNum))
        return True
    except:
        pass
    return False
    


print(isEven(-1664656))
print(isEven(1))

    
    
