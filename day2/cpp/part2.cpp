#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

int get_equal_dividers(std::string row){
  std::stringstream ss;
  std::string number;
  int read_number = 0;
  std::vector <int> row_vector;
  
  ss << row;
  while (getline(ss, number, '\t')){   // split based on '\t' substring
    read_number = atoi(number.c_str());
    row_vector.push_back(read_number);
  }
  ss.clear ();
  for (int num : row_vector){
    for (int den : row_vector){
      if (num % den == 0 and num != den){
	return num/den;
      }
    }
  }
  return -1;
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
      diff = get_equal_dividers(linetxt);
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
