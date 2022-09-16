# **CE1103 Part 2 - C Programming**
--- 


## **Lab 2 – Functions and Pointers**

* ### Question 1:
    **(numDigits)** Write a function that counts the number of digits for a non‐negative integer. For example, 1234 has 4 digits. 
    The function **numDigits1()** returns the result.
    The function prototype is given below:
    int numDigits1(int num);


    Write another function **numDigits2()** that passes the result through the pointer parameter, result. 
    The function prototype is given below:
    void numDigits2(int num, int *result);


* ### Question 2:
    **(digitPos)** Write the function **digitPos1()** that returns the position of the first appearance of a specified digit in a positive number. 
    The position of the digit is counted from the right and starts from 1. If the required digit is not in the number, the function should
    return 0. 
    For example, digitPos1(12315, 1) returns 2 and digitPos1(12, 3) returns 0. 
    The function prototype is given below:
    int digitPos1(int num, int digit);


    Write another function **digitPos2()** that passes the result through the pointer parameter, result. 
    For example, if num = 12315 and digit = 1, then *result = 2 and if num=12 and digit = 3, then *result = 0. 
    The function prototype is given below:
    void digitPos2(int num, int digit, int *result);


* ### Question 3:
    **(square)** Write a function **square1()** that returns the square of a positive integer number num, by computing the sum of odd integers starting with 1 
    as shown in the example below. 
    The result is returned to the calling function. 
    For example, if num = 4, then 42 = 1 + 3 + 5 + 7 = 16 is returned; if num = 5, then 52 = 1 + 3 + 5 + 7 + 9 = 25 is returned. 
    The function prototype is: int square1(int num);


    Write another function **square2()** that passes the result through the pointer parameter, result. 
    For example, if num = 4, then *result = 42 = 1 + 3 + 5 + 7 = 16; if num = 5, then *result = 52 = 1 + 3 + 5 + 7 + 9 = 25. 
    The function prototype is:
    void square2(int num, int *result);