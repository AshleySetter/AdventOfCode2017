#include <iostream>
#include <string>
#include <fstream>

#define MAXFILELEN 1000

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
  std::ifstream readfile;
  std::string input;
  int testarray[8] = {9, 1, 2, 1, 2, 1, 2, 9};
  int* numarray = NULL; // initialise pointer to int, initialise to NULL pointer
  int length = 8; // get length of array
  char filetext[MAXFILELEN];
  
  readfile.open("input.txt"); // open input file
  if (readfile.is_open()){
    while (!readfile.eof()){
      readfile >> filetext;
      std::cout << filetext << "\n";
    }
  }
  readfile.close();
  numarray = new int[length]; // allocate memory to store n ints
  for (int i = 0; i < length; i++){
    numarray[i] = testarray[i]; // initialise all elements of array
  }
  int result = 0;
  
  input = "test";
  std::cout << input << "\n";
  
  result = captcha_sum(numarray, length);
  std::cout << result << "\n";

  delete [] numarray; // frees memory
  numarray = NULL; // set numarray to NULL pointer again to avoid invalid memory access
  
  return 0;
}
