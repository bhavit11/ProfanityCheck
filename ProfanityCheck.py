import webbrowser
import time
import urllib
import os

def read_word():
    filename = raw_input('Enter a file path: ')
    list1 = []
    with open(filename) as f:
        for line in f:
            for word in line.split():
                a = check_profanity(word)
                c=a[14]
                if c == "t":
                    list1.append(word)
#                    filename = raw_input('Do you want to delete the profanity words from the document? : Y/N')
#                    if filename == "Y":
#                        pass

    if not list1:
        print("\nYour document has no profanity words. You may continue with your document. \n")

    else:
        print (""'\n'.join(list1))

            
                
def check_profanity(check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+check)
    output = connection.read()
    return output
    connection.close()

read_word()

