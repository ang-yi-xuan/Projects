# **CE1103 Part 2 - C Programming**
--- 


## **Lab 3 ‐ Arrays**

* ### Question 1:
    * `(findAr1D)` Write a function `findAr1D()` that returns the subscript of the **first appearance** of a target number in an array. 
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
    You may assume that the input matrix is a 3x3 matrix, i.e. SIZE = 3.