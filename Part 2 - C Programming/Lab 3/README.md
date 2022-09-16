# **CE1103 Part 2 - C Programming**
--- 


# **Lab 3 ‐ Arrays**

* ### Question 1:
    `(findAr1D)` Write a function `findAr1D()` that returns the subscript of the **first appearance** of a target number in an array. 
    For example, if **ar = { 3,6,9,4,7,8 }**, then findAr1D(6,ar,3) will return 0 where 6 is the size of the array and 3 is the number to be found, and
    `findAr1D(6,ar,9)` will return 2. If the required number is not in the array, the function will return ‐1. The function prototype is given as follows:
    int findAr1D(int size, int ar[ ], int target);


&nbsp;

* ### Question 2:

    `(swap2RowsCols2D)` Write the code for the following matrix functions: 

```
    void swap2Rows(int ar[][SIZE], int r1, int r2);
    /* the function swaps the row r1 with the row r2 of a 2‐dimensional array ar */


    void swap2Cols(int ar[][SIZE], int c1, int c2);
    /* the function swaps the column c1 with the column c2 of a 2‐dimensional array ar*/

```


&nbsp;

* ### Question 3:

    * (reverseAr1D) Write a C function printReverse() that prints an array of integers in reverse order. 
    For example, if ar[5] = {1,2,3,4,5}, then the output 5,4,3,2,1 will be printed after applying the function printReverse(). 
    The function prototype is given as follows:

        ```
        void printReverse(int ar[], int size); // size indicates the size of the array
        ```


    * Write two versions of printReverse(). One version printReverse1() uses the index
    notation and the other version printReverse2() uses the pointer notation for accessing
    the element of each index location.

    * In addition, Write a C function reverseAr1D() that takes in an array of integers ar and an
    integer size as parameters. The parameter size indicates the size of the array to be
    processed. The function converts the content in the array in reverse order and passes
    the array to the calling function via call by reference.
    void reverseAr1D(int ar[ ], int size);