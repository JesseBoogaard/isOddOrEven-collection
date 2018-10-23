#Jesse Boogaard 2018

isOddOrEven <- function(x){
    if(x == 0){
        y <- "is even"
        print(y)
    }else if(x == 1){
        y <- "is not even"
        print(y)
    }else{
        m <- isOddOrEven(x - 2)
    }
}