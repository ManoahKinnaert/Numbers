#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char* decToBin(int n) {
  char* bin = malloc(33 * sizeof(char));
  int index = 32;
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

unsigned int binToDec(char* bin) {
  size_t length = strlen(bin);
  unsigned int result = 0;
  for (int i=(int) length - 1; i >= 0; i--) {
    result += (int) (bin[i] - '0') * pow(2, (int) length - 1 - i);
  }
  return result;
}

int main() {
  int n = 12;
  char* bin = decToBin(n);
  printf("%s\n", bin);
  int result = binToDec(bin);
  printf("%d\n", result);
  // Please note that there is a memory leak here technically, but we leave it in on puprose because the program will terminate anyway.
  return 0;
}
