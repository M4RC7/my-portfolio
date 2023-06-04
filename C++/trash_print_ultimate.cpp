#include <iostream>
#include <string>
using namespace std;

int main() {
  char greeting[25];
  greeting[3] = 'k';
  cout << greeting; //I think it printed trash
  return 0;
}
