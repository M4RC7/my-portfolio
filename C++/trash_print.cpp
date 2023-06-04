#include <iostream>
using namespace std;

int main() {
  int myNumbers[5] = {10, 20, 30, 40, 50};
  //int myNumbers[5];
  for (int i : myNumbers) {
    cout << i << "\n";
  }
  cout << myNumbers[6] << endl; //it prints trash
  return 0;
}
