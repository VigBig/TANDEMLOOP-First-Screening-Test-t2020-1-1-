# TANDEMLOOP-First-Screening-Test-t2020-1-1-
This repository contains python program files associated to the first screening test of TANDEMLOOP.

All the four programs have been uploaded here have written in Python 3 using Pycharm as the IDE.
All Programs have been labelled in the manner as instructed by the email.

## Comments:

1.Program-1.py 

  I taken 3 inputs from the user through 3 variables : "a","b","type_of_operation"
  where 'a' and 'b' are varaibles that take inputs of floating values.
  and "type_of_operation" takes inputs of string values.
  
  I have constructed an if-else ladder where if "type_of_operation" = +,-,*,/ 
   
  it would peform operations of addition, subtraction, multiplaction and division on the two numbers stored in 'a' and 'b' respectively.
  
  Any other string entered would print "Invalid operator".
  
2.Program-2.py 

  I have inputted the integer from the user to a variable 'a'.
  I have intialized an variable for while loop iteration 'i' where i=1.
  
  I first constructed a simple if-else statement where if a = 1, simply print i,
  followed by an else statement under which a while loop operates
  under the condtions that i < a. The loop statements are as follows:
  
  a. if i = 1, simply print i.
  b. print (i*2) + 1
  c. increment i through i=i+1
  
3.Program-3.py 

  Here, I have noted 2 observations from the pattern given in this question:
  a. if a = odd no. , then the number of elements to be displayed in the series is the same as a. If a is even, just subtract 1 to get the odd number to potray the same pattern.
  b. if a = odd no., the last term of the series is (a*2)-1. if a = even no. then ((a-1)*2)-1.
  

  I have inputted the integer from the user to a variable 'a'.
  I have intialized an variable for while loop iteration 'i' where i=1.
  
  I first constructed an if-else statement to manage two cases when a is even or odd.
  The if statement (if 'a' is odd) has a while loop where the loop condition is if i <= (a*2).
  The loop statements are simply :
  
  a. if i%2 !=0 (i.e. if i is odd), then simply print i.
  b. increment i through i=i+1
  
  The else statement (if 'a' is even) has a while loop where the loop condition is if i <= ((a-1)*2).
  The loop statements are simply :
  
  a. if i%2 !=0 (i.e. if i is odd), then simply print i.
  b. increment i through i=i+1
  
4.Program-4.py 

  I first initialized a list called num = [1,2,3,4,5,6,7,8,9]
  I initalized an empty input list called "ip". 
  I have intialized an integer variable called my_num = "0". (note "0" is a string value)
  
  I have constructed a while loop to input a list of numbers into ip.
  The condition to break the loop is if the user enters "".
  
  ip.remove('') is wriiten below the loop to remove the "" item at the end of the list.
  
  Since we need the list to have integers and the while loop opertaion inputted the numbers as strings,
  a for loop has been written to convert the string values to integers and stored in the same list, ip.
  
  Nine counter variables have been initialized to zero, the names of the variables are aptly,
  "one", "two", "three", "four","five","six", "seven", "eight" and "nine" which correspond
  to the numbers in the num list.
  
  A third for loop has been constructed where variable "i" scans through each item in list ip with 
  ladder of if statements underneath it.
  
  Each if statment checks if number in list ip is divisible by number in list num.
  If the the number is divisuble then the counter variables are incrememnted.
  
  Finally a dictionary called output is created where each item value from num list is associated with their respective counter values.
  
  Then the dictionary is finally printed.
  
