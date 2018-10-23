! Jesse Boogaard 2018
! This tells you if a number is odd or even
RECURSIVE INTEGER FUNCTION isOddOrEven(x) RESULT(y)
    INTEGER :: x
    IF(x == 0) THEN
        print *, 'is even.'
    ELSE IF(x == 1) THEN
        print *, 'is odd.'
    ELSE
        y = isOddOrEven(x - 2)
    END IF
END FUNCTION isOddOrEven

PROGRAM main
    INTEGER :: input, result
    print *, 'Enter a number below 86844'
    read *, input
    print *, 'You requested', input
    result = isOddOrEven(input)
END PROGRAM main
