//Just a simple reminder of why to not use goto.

#include <iostream>
using namespace std;

int main() {
  lbl:
  cout << "DO NOT USE GOTO ";
  goto lbl;
  return 0;
}
