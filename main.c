#include <stdio.h>

int MULADD(int a, int b, int c, int d) {
    return (a * b) + (c * d);
}

int main() {
    int a, b, c, d;

    printf("Enter values for a, b, c, d:\n");
    scanf("%d %d %d %d", &a, &b, &c, &d);

    int result = MULADD(a, b, c, d);

    printf("Result of MULADD(a, b, c, d) = (a * b) + (c * d) = %d\n", result);

    return 0;
}
