// Logan Daw 2018

#include <iostream>

void isOddOrEven (int n) {
    int x;
	if(n<0) {
		x = -n;
	} else {
		x = n;
	}
	while (x > 1) {
		for (int i = 0; i < 2; i++) {
			x--;
		}
	}
	switch (x) {
    	case 0: std::cout << n << " is even" << std::endl;
        	break;
    	case 1: std::cout << n << " is odd" << std::endl;
        	break;
    	default: std::cout << n << " is something else" << std::endl;
        	break;
	}
}


int main()
{
    isOddOrEven(100);
    isOddOrEven(9);
    isOddOrEven(-500);
    isOddOrEven(0);
    isOddOrEven(129485247);

    return 0;
}
