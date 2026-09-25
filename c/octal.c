#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

char* decToOct(int n) {
    char* oct = malloc(33 * sizeof(char));
    int index = 32;
    oct[index] = '\0';
    if (oct == 0) { oct[--index] = '0'; }
    while (n > 0) {
        int o = n % 8;
        oct[index--] = o + '0';
        n /= 8;
    }
    return &oct[index + 1];
}

unsigned int octToDec(char* oct) {
    size_t length = strlen(oct);
    unsigned int result = 0;
    for (int i=(int) length - 1; i >= 0; i--) {
        result += (int) (oct[i] - '0') * pow(8, (int) length - 1 - i);
    }
    return result;
}

int main() {
    int n = 32;
    char* oct = decToOct(n);
    printf("%s\n", oct);
    int result = octToDec(oct);
    printf("%d\n", result);
    return 0; // Please note that the memory leak in this program is intentional.
}