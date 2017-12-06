#include <iostream>
#include <string>

int captcha_sum(int *sequence, int length){
  /*
  calculates sum of all digits that match the next digit in the sequence.
  For last element, checks if last element equals first element.
  */
  int summation = 0;
  int i;
  
  for (i = 0; i < length-1; ++i){
    if (sequence[i] == sequence[i+1]){
      summation += sequence[i];
    }
  }
  if (sequence[length-1] == sequence[0]){
    summation += sequence[length-1];
  }
  
  return summation;
}

int main(){
  std::string input;
  int testarray[8] = {9, 1, 2, 1, 2, 1, 2, 9};
  int length = 8;
  int result = 0;
  
  input = "test";
  std::cout << input << "\n";
  
  result = captcha_sum(testarray, length);
  std::cout << result << "\n";
  
  return 0;
}
