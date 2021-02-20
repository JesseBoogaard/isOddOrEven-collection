package main

import "fmt"

func main(){
	fmt.Println(oddoreven(5))
}

func oddoreven(n int) string {
	if (n % 2 == 0){
		return "Is even"
	} else {
		return "Is odd"
	}
}