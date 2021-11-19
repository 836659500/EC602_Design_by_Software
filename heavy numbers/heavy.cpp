#include <string>
#include <vector>
using std::vector;

int power(int A, int exp) {
  int product = 1;
  for (int i = 0; i < exp; i++) {
    product = product * A;
  }
  return product;
}

int main(int argc, char **argv) {
  int y = atoi(*(argv + 1));
  int N = atoi(*(argv + 2));
  vector<int> num;
  int amount = 0;
  while (true) {
    int m;  // m is the most significant bit of y
    int i = 0;
    while (y >= power(N, i)) {
      m = i;
      i++;
    }
    int square_sum = 0;
    while (m >= 0) {                   // calculate the squared sum
      int temp = y / power(N, m);
      y -= temp * power(N, m);
      square_sum += temp * temp;
      m -= 1;
    }


    if (square_sum == 1) return 1;    // convergence to 1


    for (int n = 0; n < amount; n++) {
      if (square_sum == num.at(n))
        return 0;                // repetition of some previous squared sum
    }
    num.push_back(square_sum);
    amount += 1;
    y = square_sum;
  }
}

