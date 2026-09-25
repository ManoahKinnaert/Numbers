#include <stdio.h>
#include <stdlib.h>

char* decToBin(int n) {
  char* bin = malloc(32 * sizeof(char));
  int index = 31;
  bin[index] = '\0';
  if (n == 0) {
    bin[--index] = '0';
  }

  while (n > 0) {
    int bit = n % 2;
    bin[index--] = bit + '0';
    n /= 2;
  }
  return &bin[index + 1];
}

int main() {
  int n = 12;
  char* bin = decToBin(n);
  printf("%s\n", bin);
  return 0;
}
