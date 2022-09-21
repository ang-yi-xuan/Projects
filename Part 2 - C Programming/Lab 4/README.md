# **CE1103 Part 2 - C Programming**
--- 


## **Lab 4 - Character Strings**

* ### Question 1:
    `(sweepSpace)` Write two versions of a C function that remove all the blank spaces in a string.
    The first version sweepSpace1() will use array notation for processing the string, while the
    other version sweepSpace2() will use pointer notation. The function prototypes are given
    below:

```
    char *sweepSpace1(char *str);
    char *sweepSpace2(char *str);
```


&nbsp;

* ### Question 2:

    `(findTarget)` Write a C program that reads and searches character strings. In the program, it
    contains the function findTarget() that searches whether a target name string has been
    stored in the array of strings. 
    
    The function prototype is:

    ```
    int findTarget(char *target, char nameptr[][80], int size);
    ```

    where **nameptr** is the array of strings, **size** is the number of names stored in the array and
    **target** is the target string. 

    If the target string is found, the function will return its index location, or ‐1 if otherwise. In addition, the program also contains the functions readNames() and printNames(). 
    
    The function readNames() reads a number of names from the user. 
    The function prototype is:

    ```
    void readNames(char nameptr[][80], int *size);
    ```

    where **nameptr** is the array of strings to store the input names, and **size** is a pointer
    parameter which passes the number of names to the caller. 
    
    The function prototype of printNames() which prints the names is:

    ```
    void printNames(char nameptr[][80], int size);
    ```


&nbsp;

* ### Question 3:

    `(palindrome)` Write a function palindrome() that reads a character string and determines
    whether or not it is a palindrome. A palindrome is a sequence of characters that reads the
    same forwards and backwards. For example, "abba" and "abcba" are palindromes, but
    "abcd" is not. The function returns 1 if it is palindrome, or 0 if otherwise. The function
    prototype is given as follows:

    ```
    int palindrome(char *str);
    ```