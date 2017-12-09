#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

int get_difference(int *row, int length){
  int largest = -1000000;
  int smallest = 1000000;
  int difference = 0;
  
  for(int i = 0; i<length; i++){
    if (row[i] > largest){
      largest = row[i];
    }
    if (row[i] < smallest){
      smallest = row[i];
    }
  }
  difference = largest - smallest;
  return difference;
}

int calc_checksum(std::string filename){
  int checksum = 0;
  std::ifstream readfile;
  std::string linetxt;
  std::string number;
  std::istringstream iss;
  
  readfile.open("input.txt"); // open input file
  if (readfile.is_open()){
    while (getline(readfile, linetxt)){
      std::cout << linetxt << "\n";
      iss.str(linetxt);
      while (getline(iss, number, ' ')){
	// split based on ' ' substring
	std::cout << number << "\n";
      }
    }
  }
  readfile.close();
  
  return checksum;
}

int main(){
  std::string filename = "input.txt";
  for (int i = 0; i < 1; i++){
    calc_checksum(filename);
  }
  
  return 1;
}
