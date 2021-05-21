
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:11:03 2021

@author: surim

An RSA encrypting and decrypting software 


User input and save the plain text into a file!!
"""


#      => Take in user input

ptextOrg= input("Please type in your message to be encrypted: \n")
ptextCapped = ptextOrg.upper()          # to use the lower range of ascii char 

#      => save plain capitalized text it to a file 
f = open("Message_to_be_converted.txt", "w") 
f.write(ptextCapped)
f.close()

#      => Remove white spaces
teweeded = ptextCapped.replace(" ", "") # removes the space 


#     =>  save ascii format
h = open("asciied.txt", "w")
for c in teweeded:    
    Asciied = ord(c)    
    h.writelines(str(Asciied))
h.close()

     # =>  Read the length of the string 
Number_of_chars = len(teweeded)


#    => Compels the user for some input
if Number_of_chars <= 0:
    print("Please add a message")
else:
    Number_of_chars = len(teweeded)
    
# the length of the string
block = len(teweeded)

lengthOfTweeted = len(teweeded)

def padding():    
    for c in Asciied:
        if block < 4:
            c = c + 'x'
        print(c)
     
# #padding the text
# if (block < 4 ):
#      print("needs padding")
# else:
#     print ("good to go")
    

teweeded = ptextCapped.replace(" ", "") # removes the space     
Number_of_chars = len(teweeded)
  
blockLen = 4

if ((Number_of_chars % blockLen) > 0):
    padding = blockLen - (Number_of_chars % blockLen)
else:
    padding = 0
    
difference = Number_of_chars % blockLen


        
def textpadding(inputtext):
        msg=inputtext
        message = msg
        message = msg.replace(" ", "") # removes the space 
        Number_of_chars = len(message)       
        blockLen = 4
        if ((Number_of_chars % blockLen) > 0):
            padding = blockLen - (Number_of_chars % blockLen)
        else:
            padding = 0
            
        char = "X"
        paddingInit =  ""
        padFile = open("outputtext.txt" , "w")        
        padFile.write(message)
        padFile = open("outputtext.txt", "a")        
        for i in range(padding):
            paddingInit += char
            padFile.write(paddingInit + "    ")            
        padFile.close()
            
            

textpadding(ptextCapped)


