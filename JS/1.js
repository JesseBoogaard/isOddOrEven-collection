//Jesse Boogaard 2018

function isOddOrEven(x) {
    let numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    let arr = x.toString().split("")
    let res;
    y = arr.slice(-1)[0]
    
    for(let i = 0; i < numbers.length; i++){
        if(y === numbers[i]){
           res = numbers[i] 
        }
    }
    switch(res){
        case '0':
            console.log(`${ arr.join("") } is even`)
            break;

        case '2':
            console.log(`${ arr.join("") } is even`)
            break;

        case '4':
            console.log(`${ arr.join("") } is even`)
            break;

        case '6':
            console.log(`${ arr.join("") } is even`)
            break;

        case '8':
            console.log(`${ arr.join("") } is even`)
            break;

        case '1':
            console.log(`${ arr.join("") } is odd`)
            break;
        
        case '3':
            console.log(`${ arr.join("") } is odd`)
            break;
        
        case '5':
            console.log(`${ arr.join("") } is odd`)
            break;

        case '7':
            console.log(`${ arr.join("") } is odd`)
            break;

        case '9':
            console.log(`${ arr.join("") } is odd`)
            break;
    }
}