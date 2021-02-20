String oddoreven(int n){
  if (n % 2 == 0){
    return "Is even";
  } else {
    return "Is odd";
  }
}

// Test
void main(){
  print(oddoreven(5));
}