#include <stdio.h>
int main()
{
    int i, d = 1; // d = denominator
    float x, result = 1.0, n = 1.0; // n = numerator
    printf("Enter x: \n");
    scanf("%f", &x);

    for (i = 1; i <= 10; i++)
    {
        d *= i;
        n *= x;
        result += n/d;
    }

    printf("Result = %.2f\n", result);
    return 0;
    }