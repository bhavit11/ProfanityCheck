# Most frequent

A very basic python program that parses all the email addresses in a text file by using the given condition that if the first word of a line has 'From' , the word next to it is the email address we want.

How it works:
1) It asks the user for the location of the text file to be read.
2) Opens the text file and pulls one line at a time and if the first word of the line is 'From' it pulls the second word and saves it into a list
3) The program creates a dictionary with the email address as the key and its frequency as the value.
4) Then it sorts the dictionary according to values in ascending order and then looks for the all the keys that have the value same as the last value in the sorted list of dictionary values




# Text file provided with the program is test.txt
