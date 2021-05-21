#Text padding script

 # 1. pad original p_msg
def pad_txt(p_text, output_padded_text):
    msg_file = open(p_text, "r")
    p_msg = msg_file.read()
    p_msg = p_msg.rstrip("\n") #strip away the new line in end of file --> correct padding of padding char 
    num_of_char = len(p_msg)
    msg_file.close()
    
    # padding
    len_blocks = 8 # plain text padding length
    if((num_of_char % len_blocks) > 0): # only pad if there is a remainder in one block
        len_padding = len_blocks - (num_of_char % len_blocks)
    else: # no remainder put lenngth of padding to zero
        len_padding = 0
    
    # pad file:
    char = "X"      # char used for padding
    pad_chars = "" 
    p_f = open(output_padded_text, "w")
    p_f.write(p_msg) # original p_msg text
    
    pad_file = open(output_padded_text, "a") #start padding
    for i in range (len_padding):      
       pad_chars+= char
        
    pad_file.write(pad_chars) # write all the padding to the padding file
    pad_file.close

# 2. convert blocks of chars into numbers (2 digit per char)
def convert_to_num(char_padded_file, converted_num_file, modulus): #convert chars to digits 
    pad_file = open(char_padded_file, "r")
    convert_file = open(converted_num_file, "a")
    convert_file.truncate(0)     # clear write to file
    plain_txt_chars_per_block = 2 
    whitespace = 0
    
    while True:
        whitespace += 1
        char = pad_file.read(1) # read one char at the time
        if not char: # end of file --> break loop
            break
        char_to_num = ord(char) - 28 # minus 28, to get all numbers to become two digit - cons: eliminate some ascii characters
        num_to_string = str(char_to_num)
        if char_to_num <= 9 and char_to_num >= 0:
            num_to_string = "0" + num_to_string 
        convert_file.write(num_to_string)    
        if (whitespace % plain_txt_chars_per_block == 0):
            convert_file.write(" ")
    pad_file.close()
    convert_file.close()
        
# 3. convert blocks of digits to padded text
def convert_to_char(convert_char_file, decrypted_num_file): 
    convert_to = open(convert_char_file, "w")
    convert_from = open(decrypted_num_file, "r")
    
    plain_txt_chars_per_block = 2 
    whitespace = " "
    counter = 0
    number = ""
    
    while True:
        counter += 1
        char = convert_from.read(1) # read one char at the time
        if not char: # end of file --> break loop
            break
        elif char == whitespace: # reduce counter to correct counts ascii chars - remember whitespace is a char
            counter -= 1
        else:
            number += char #store number before converting to ascii
            
        if (counter % plain_txt_chars_per_block == 0 and (number != "" or number != '') ): # write to file - you have a number correspodning to a ascii char
            number = number.lstrip('0')
            number = int(number)
            number = number + 28 # convert back to ascii --> therefore + 28
            number = chr(number)
            convert_to.write(number)
            number = ""
    
    convert_to.close()
    convert_from.close()
    
# 4. unpadding chars 
def unpad_txt(p_text, input_padded_text):
    plain_txt = open(p_text, "w")
    padded_txt = open(input_padded_text, "r")
    pad_msg = padded_txt.read()
    plain_msg = pad_msg.rstrip("X")
    plain_txt.write(plain_msg)