#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

int get_difference(std::string row){
  std::stringstream ss;
  std::string number;
  int num = 0;
  int largest = -1000000;
  int smallest = 1000000;
  int difference = 0;

  ss << row;
  while (getline(ss, number, '\t')){   // split based on '\t' substring
    num = atoi(number.c_str());
    if (num > largest){
      largest = num;
    }
    if (num < smallest){
      smallest = num;
    }
  }
  ss.clear ();
  difference = largest - smallest;
  return difference;
}

int calc_checksum(std::string filename){
  int checksum = 0;
  std::ifstream readfile;
  std::string linetxt;
  int diff = 0;
  
  readfile.open("input.txt"); // open input file
  if (readfile.is_open()){
    while (getline(readfile, linetxt)){
      //      std::cout << linetxt << "\n";
      diff = get_difference(linetxt);
      //      std::cout << diff << "\n";
      checksum += diff;
    }
  }
  readfile.close();
  
  return checksum;
}

int main(){
  int result;
  std::string filename = "input.txt";
  for (int i = 0; i < 1000; i++){
    result = calc_checksum(filename);
  }
  std::cout << result << "\n";
  return 1;
}
