#include <stdio.h>

int main() {

    int a, b, r;

    printf("CALCULATOR OF GREATEST COMMON DIVISOR\n");
    printf("Enter two numbers\n");

    printf("The first one:\t");
    scanf("%d", &a);

    printf("The second:\t");
    scanf("%d", &b);

    if (a == 0 && b == 0) {
        printf("GCD is undefined for 0 and 0");
    }
    else {
        while (b != 0) {
            r = a % b;
            a = b;
            b = r;
        }

        printf("GCD IS %d", a);
    }

    return 0;
}