/* Question 1*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int studentNumber = 0, mark;

    printf("Enter Student ID: \n");
    scanf("%d",&studentNumber);
    while (studentNumber!= -1)
    {
    scanf("%d", &mark);
    switch ((mark+5) / 10) {
    case 10:
    case 9:
    case 8: printf("Grade = %c\n", 'A');
    break;
    case 7: printf("Grade = %c\n", 'B');
    break;
    case 6: printf("Grade = %c\n", 'C');
    break;
    case 5: printf("Grade = %c\n", 'D');
    break;
    default: printf("Grade = %c\n", 'F');
    }
    printf("Enter Student ID: ");
    scanf("%d",&studentNumber);
    }
    return 0;
}
