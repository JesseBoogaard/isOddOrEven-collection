#include <stdio.h>

// isOddOrEven: O(1)
// isOdd: O(1)

int isOddOrEven( const int i_n )
{
    if ( i_n & 1 )
		printf( "%d is Odd\n", i_n );
    else
		printf( "%d is Even\n", i_n );
}

int isOdd( const long long i_n )
{
    int n = i_n;
    for( int i = 6; i; i-- )
	{
        n *= n;
    }
    return !!n;
}

void printOddEven( const int i_n )
{
	printf( isOdd( i_n ) ? "%d is Odd\n" :  "%d is Even\n", i_n );
}


int main()
{
    isOddOrEven( 13 );
    isOddOrEven( 48 );
	
	printOddEven( 13 );
	printOddEven( 48 );

    return 0;
}
