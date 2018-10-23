void isOddOrEven (int n) {
	int x = n;
	while (x > 1) {
		for (i = 0; i < 2; i++) {
			x--;
		}
	}
	switch (x) {
    	case 0: std::cout << n << " is even" << std::endl;
        	break;
    	case 0: std::cout << n << " is odd" << std::endl;
        	break;
    	default: std::cout << n << " is something else" << std::endl;
        	break;
	}
}
