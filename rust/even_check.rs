// Script for determing if an integer is even or odd
// It attempts to split the integer into two piles
// If the piles are the same size, the integer is even
// Runtime appears to be O(n!)
// Don't use on numbers beyond 29 or so in absolute value

use std::io;
use std::cmp::Ordering;

fn main() {
    println!("What is your number?");

    let mut number = String::new();
    io::stdin().read_line(&mut number)
        .expect("Failed to read line");

    let number: i32 = number.trim().parse()
        .expect("Can't interpret that number");

    let result = is_even(number);

    let evenorodd = match result {
        true => "even",
        false => "odd"
    };

    println!("Your number is {}.", evenorodd);
}

fn is_even(n: i32) -> bool {

    let abs_n: i32 = match n.cmp(&0) {
        Ordering::Less => n - n - n,
        Ordering::Greater => n,
        Ordering::Equal => 0
    };

    let mut counter = 0;
    let mut pile1 = 0;
    let mut pile2 = 0;

    let result: bool = loop {
        counter += 1;

        if abs_n == 0 {
            break true
        }
        else if abs_n == 1 {
            break false
        }

        if is_even(counter - 1) {
            pile1 += 1;
        }
        else {
            pile2 += 1;
        }

        if counter == abs_n {
            break pile1 == pile2
        }
    };

    result
}
