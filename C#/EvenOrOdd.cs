//Mustafa Ali Akbar 2018
using System;
using System.Collections.Generic;

class EvenOrOdd{
    static void Main(string[] args){
        isEvenOrOdd(-32);
        isEvenOrOdd(5999999);
        isEvenOrOdd(2928);
        isEvenOrOdd(-4);
    }
    //Creates a list based on input, fills it, and then compares the elements in it with the number
    static void isEvenOrOdd(int num)
    {
        if(num < 0)
        {
            num = num * (-1);
        }
        int listSize = (num + 2) / 2;
        List<int> evenNumbers = new List<int>(listSize);
        int currentEvenNum = 0;
        if(num > 0)
        {
            for(int i = 0; i < listSize; i++)
            {
                evenNumbers.Add(currentEvenNum);
                currentEvenNum += 2;
            }
        }
        else
        {
            Console.WriteLine("The number is even");
            return;
        }
        foreach (int n in evenNumbers)
        {
            if(n == num)
            {
                Console.WriteLine("The number is even");
                return;
            }
        }
        Console.WriteLine("The number is odd");
    }
}