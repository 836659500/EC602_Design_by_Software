#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::endl;
using std::string;

int power(int A, int B) {
  int product = 1;
  for (int i = 0; i < B; i++) {
    product = product * A;
  }
  return product;
}


int main(int argc, char **argv) {
  string zi = *(argv + 1);
  int a1 = atoi(*(argv + 2));
  int a2 = atoi(*(argv + 3));
  int a = 0;
  for (int i = 0; i < zi.size(); i++)
    a += (static_cast<int>(zi.at(i))
          - static_cast<int>('0')) * power(a1, (zi.size() - 1 - i));

  int i = 0;
  int m;
  while (a >= power(a2, i)) {
    m = i;
    i++;
  }
  string res = "";
  while (m >= 0) {
    int temp = a / power(a2, m);
    a -= temp * power(a2, m);
    res += static_cast<char>(temp + static_cast<int>('0'));
    m -= 1;
  }
  cout << res << endl;
  return 0;
}
