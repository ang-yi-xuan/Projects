# **CE1103 Part 2 - C Programming**
--- 


## **Lab 5 - Structures**

### Phonebook Management System:
    
    Write a C program that implements the phoebook management system with the following three functions:


1. The function readin() reads a number of persons’ names and their corresponding
    telephone numbers, passes the data to the caller via the parameter p, and returns the
    number of names that have entered. The character '#' is used to indicate the end of
    user input.

&nbsp;

2. The function printPB() prints the phonebook information on the display. It will print the
message “Empty phonebook“ if the phonebook list is empty.


&nbsp;

3. The function search() finds the telephone number of an input name target, and then
prints the name and telephone number on the screen. If the input name cannot be
found, then it will print an appropriate error message. 


    The prototypes of the three functions are:
    ```
    void printPB(PhoneBk *pb, int size);
    int readin(PhoneBk *pb);
    void search(PhoneBk *pb, int size, char *target);
    ```


    The structure definition for PhoneBk is: 
    ```
    typedef struct {
    char name[20]; // a string
    int telno; // an integer with 5 digits
    } PhoneBk;
    ```
