#include <stdio.h>
int main()
{
    int row, col, height;
    int num = 0;
    printf("Enter the height: \n");
    scanf("%d", &height);
    
    for (row = 0; row < height; row++)
    {
        for (col = 0; col < row+1; col++) // print numbers
        printf("%d",num+1);
        num = (num + 1) % 3; // print up to number 3
        printf("\n");
    }
    
    return 0;
}
