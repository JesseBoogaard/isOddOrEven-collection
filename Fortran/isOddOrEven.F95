program isOddOrEven

! This tells you if a number is odd or even
    implicit none

! Type declarations
    Integer :: input, mod, result
    Logical :: isOdd


! Executable statements
    input = 1233455243
    mod = 2
    result = modulo(input, mod)
    IF (result == 0) THEN
        print *, "is even"
    ELSE IF (result == 1) THEN
        print *, "is odd"
    END IF
end program isOddOrEven
