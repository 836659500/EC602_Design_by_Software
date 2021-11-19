#include <string>
#include <vector>
#include "bigint.h"
using std::vector;
using std::string;
using std::to_string;
typedef string BigInt;

BigInt multiply_int(const BigInt &a, const BigInt &b) {
  vector<int> x;
  vector<int> y;

  for (auto i = a.begin(); i != a.end(); i++)
    x.push_back(*i - '0');  // convert char in string to int by -'0'
  for (auto i = b.begin(); i != b.end(); i++)
    y.push_back(*i - '0');  // convert char in string to int by -'0'

  int m = x.size();  // most significant bit of x
  int n = y.size();  // most significant bit of y
  int msb = m + n - 2;  // most significant bit of the product
  vector<int> c(msb + 1);  // storage of every coefficient of bit

  for (int i = m; i <= msb; i++)
    x.push_back(0);  // zero fill for calculation in every bit
  for (int i = n; i <= msb; i++)
    y.push_back(0);
  for (int i = 0; i <= msb; i++) {
    c.at(i) = 0;
    for (int j = 0; j <= i; j++)
      c.at(i) += (x.at(j) * y.at(i - j));
  }

  vector<int> solution;
  int temp = 0;
  int carry = 0;
  int current = 0;

  for (int i = c.size() - 1; i >= 0; i--) {  // from last digit to first
    temp = c.at(i) + carry;
    current = temp % 10;  // current digit
    solution.insert(solution.begin(), current);
    carry = temp / 10;  // carry bit add to next digit
    if (i == 0 && carry != 0)   // carry out at first bit
      solution.insert(solution.begin(), carry);
  }

  BigInt product = "";
  for (auto i = solution.begin(); i != solution.end(); i++) {
    product += to_string(*i);
    if (product == "0") break;  // avoid output too many 0 if answer is 0
  }

  return product;
}

