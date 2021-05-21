# This is the padding and the division part of the code 

# taking the user input
def padding ( read, calculate, padd):
    read.read()
    return len(read)    
    

def odd(x):
    if x % 2 == 0:
        return("odd")
    else:
        return ("even")
   
    
p_text = input ("what would like to send\n")


p_to_file = open("p_txt_container","a")

#p_to_file.write(" this is a trail")

p_to_file.write(p_text)

p_to_file.close()


#This is the reading part +++++++++++++++++++++++++

read_file = open("p_txt_container" , "r")
containent = read_file.read()
read_file.close

# here we will do some division and padding if needed!==================

print ("this is some thing and we are not sure what will happen\n")
print (containent)
quantity = len (containent)

    
if quantity > 0:
    for quantity is odd:
        else:
            even 
    
#open("p_txt_container","a")
#p_to_file.write("x")
#p_to_file.close()
    
    
print(quantity)

