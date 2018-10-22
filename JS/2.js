//Jesse Boogaard 2018

function isOddOrEven(x){
    if(x == 0){
        console.log(true)
    }else if(x == 1){
        console.log(false)
    }else{
        isOddOrEven(x - 2)
    }
}