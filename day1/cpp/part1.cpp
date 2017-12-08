#include <iostream>
#include <string>
#include <fstream>

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

int part1(){
  std::ifstream readfile;
  std::string filetext;
  std::string stringnumber;
  int* numarray = NULL; // initialise pointer to int, initialise to NULL pointer
  int length = 0; // initialise length of array to 0
  
  readfile.open("input.txt"); // open input file
  if (readfile.is_open()){
    getline(readfile, filetext);
    //    std::cout << filetext << "\n";
  }
  readfile.close();
  length = filetext.length();
  numarray = new int[length]; // allocate memory to store n ints
  for (int i = 0; i < length; i++){
    stringnumber = filetext.at(i); // get character (as a length 1 string) at position i
    numarray[i] = atoi(stringnumber.c_str()); // convert length 1 string to char and convert char to int and store in array
  }
  int result = 0;
    
  result = captcha_sum(numarray, length);
  //  std::cout << result << "\n";

  delete [] numarray; // frees memory
  numarray = NULL; // set numarray to NULL pointer again to avoid invalid memory access
  return result;
}

int main(){
  int i, result;
  for (i = 0; i<1000; i++){
    result = part1();
  }
  std::cout << result << "\n";
  return 0;
}
