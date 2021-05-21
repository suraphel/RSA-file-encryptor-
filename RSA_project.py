# all function in on 
    #Main program file - running the RSA encryption code
import random



a = gcd((9-1), 15)
b = gcd((7), 15)
c = gcd((17-1), 15)
d = gcd(15, 49)
e = gcd(15, 327)

bob_plain_text = "b_msg.txt"
bob_pad_text = "b_pad_msg.txt"
bob_convert_to_num_text = "b_converted_num_file.txt"
bob_cipher_text = "b_cipher_text.txt"
alice_decrypt_convert_to_num_text = "a_decrypt_converted_num_file.txt"
alice_decrypt_pad_text = "a_d_pad_msg.txt"
alice_decrypted_plain_text = "a_d_message.txt"

alice_plain_text = "a_msg.txt"
alice_pad_text = "a_pad_msg.txt"
alice_convert_to_num_text = "a_converted_num_file.txt"
alice_cipher_text = "a_cipher_text.txt"
bob_decrypt_convert_to_num_text = "b_decrypt_converted_num_file.txt"
bob_decrypt_pad_text = "b_d_pad_msg.txt"
bob_decrypted_plain_text = "b_d_message.txt"


bob_p = gen_prime(90000, 91000)
bob_q = gen_prime(90000, 91000)
bob_n = gen_modulus(bob_p, bob_q)
bob_e = gen_public(bob_p, bob_q)
bob_d = gen_secret(bob_p, bob_q, bob_e)

alice_p = gen_prime(90000, 91000)
alice_q = gen_prime(90000, 91000)
alice_n = gen_modulus(alice_p, alice_q)
alice_e = gen_public(alice_p, alice_q)
alice_d = gen_secret(alice_p, alice_q, alice_e)

########## Bob sends message to Alice
message = "Alice, I am trying with another text, does it still work?"
print("Bob to Alice: ",message)
plain_txt = open (bob_plain_text, "w")
plain_txt.write(message)
plain_txt.close()

pad_txt(bob_plain_text, bob_pad_text) # Bob pads the plain message
convert_to_num(bob_pad_text, bob_convert_to_num_text, bob_n) # Bob converts the padded plain message to numbers
encrypt(alice_e, alice_n, bob_convert_to_num_text, bob_cipher_text, 4) # Bob encrypts the numbers to block ciphers


## Alice decrypts Bobs message
decrypt(alice_d, alice_n, bob_cipher_text, bob_decrypt_convert_to_num_text, 4)
convert_to_char(bob_decrypt_pad_text, bob_decrypt_convert_to_num_text)
unpad_txt(bob_decrypted_plain_text, bob_decrypt_pad_text)


########## Alice replies to Bob
plain_txt = open (bob_decrypted_plain_text, "r")
message = plain_txt.read()
print("Alice receives from Bob: ", message)
if message == "Alice, I am trying with another text, does it still work?":
    message = "yes Bob, the RSA algorithm works as a crypto algorithm"
else:
    message = "You sent some jewbrish Bob, can you send it again?"
plain_txt = open (alice_plain_text, "w")
print("Alice sends to Bob: ", message)
plain_txt.write(message)
plain_txt.close()

pad_txt(alice_plain_text, alice_pad_text) # Alice pads the plain message
convert_to_num(alice_pad_text, alice_convert_to_num_text, alice_n) # Alice converts the padded plain message to numbers
encrypt(bob_e, bob_n, alice_convert_to_num_text, alice_cipher_text, 4) # Alice encrypts the numbers to block ciphers

## Bob decrypts Alice message
decrypt(bob_d, bob_n, alice_cipher_text, alice_decrypt_convert_to_num_text, 4)
convert_to_char(alice_decrypt_pad_text, alice_decrypt_convert_to_num_text)
unpad_txt(alice_decrypted_plain_text, alice_decrypt_pad_text)
plain_txt = open (alice_decrypted_plain_text, "r")
message = plain_txt.read()
print("Bob receives from Alice: ", message)

# -*- coding: utf-8 -*-
"""
RSA implementation
"""
import random

def gcd(a, b): # for a, b => 0 # greatest common divisor
    c = a #make copy to not modify original
    d = b # make copy to not modify original
    while (d != 0):
        r = c % d
        c = d
        d = r
    return c


def if_even_make_odd(p): # 2. check if p number is even
    if (p % 2) == 0:
        p = p + 1
    return p
    
        
def is_p_bigger_pmax(p, p_min, p_max): # 3. check if p > p_max
    if p > p_max:
        p = p_min + p % (p_max + 1)
        return True
    else:
        return False
        
        
def check_if_prime(p):# 4.  primality test - fermats test 
    a = random.randint(2, (p - 2)) # generate int between values
    if ((a**(p-1) % p) == 1):
        return True
    else:
        return False
    

def gen_prime(start, end): # cryptography in c & c++ p.329
    # start, end => 1
    a = 1
    if (a == 1):
            p = random.randint(start, end) # generate int between values    
            a = 2
    while(a != 5):
        if (a == 2):
            p = if_even_make_odd(p)
            a = 3
        elif (a == 3):
            b = is_p_bigger_pmax(p, start, end)
            if (b == True):
                a = 2
            else:
                a = 4
        elif (a == 4):
            f = random.randint(start, end) 
            f = if_even_make_odd(f) # f needs to be an odd positive integer
            if (gcd(p - 1, f) == 1) and check_if_prime(p):
                a = 5
            else:
                p = p + 2
                a = 3
    return p

       
## key generation
#1.1 Generate the modulus, n --> n = pq, where p and q are to random primes
def gen_modulus(p, q): # p and q are primes
    n = p*q
    return n


#1.2 derive the public key component, e --> relative prime to phi(n) and e < phi(n)
def gen_public(p, q):
    phi_n = (p - 1)*(q - 1)
    while True:
        e = random.randint(2, (phi_n - 1))
        if (gcd(e, phi_n) == 1): # run loop until gcd(e, phi_n) = 1 and e < phi_n
            return e    
            break

#1.3 derive the secret key component, d --> modular inverse of e
def xtnd_gcd(a, b): # a = phi_n > b = e, from Crypto C/C++ p.176
    # gcd(a, b) = u*a + v*b, where v = secret component (the inverse of e)
    v_1 = -1
    v_3 = -1
    q = -1
    t_3 = -1
    t_1 = -1
    v = -1
    u = 1
    d = a
    if(b == 0):
        v = 0
        return v
    else:
        v_1 = 0
        v_3 = b
    while (v_3 != 0):
        t_3 = d % v_3
        q = int((d - t_3) / v_3)
        t_1 = int(u - q * v_1)
        u = v_1
        d = v_3
        v_1 = t_1
        v_3 = t_3
    
    v = int((d - u*a)/b)
    v = v % a
    return v

def gen_secret(prime_1, prime_2, public_key):
    phi_n = (prime_1 - 1)*(prime_2 - 1)
    private_key = xtnd_gcd(phi_n, public_key)
    #private_key = private_key % phi_n #get private key as a positive integer
    return private_key

#p = gen_prime(10, 100)
#q = gen_prime(10, 100)
#n = gen_modulus(p, q)
#e = gen_public(p, q)
d = gen_secret(7, 11, 7)



## message encryption
c = (5**7) % 77
m = 47**43 % 77

#2.1 transform to two digit numbers

#2.2 divide into equal size of chunks

#2.3 encrypt

#2.4 send the ciphertext

## message decryption
#3.1 decrypt the ciphertext

#3.2 put the text together again, to one unit

#3.3 translate the two digit to the corresponding character

#3.4 write text to file



 # 1. pad original message
def pad_txt(p_text, output_padded_text):
    msg_file = open(p_text, "r")
    message = msg_file.read()
    message = message.rstrip("\n") #enf
    num_of_char = len(message)
    msg_file.close()
    
    # find length of padding
    len_blocks = 8 # plain text padding length
    if((num_of_char % len_blocks) > 0): # only pad if there is a remainder in one block
        len_padding = len_blocks - (num_of_char % len_blocks)
    else: # no remainder put lenngth of padding to zero
        len_padding = 0
    
    # pad file:
    char = "X"      # char used for padding
    pad_chars = "" 
    pad_file = open(output_padded_text, "w")
    pad_file.write(message) # original message text
    
    pad_file = open(output_padded_text, "a") #start padding
    for i in range (len_padding):      
       pad_chars+= char
        
    pad_file.write(pad_chars) # write all the padding to the padding file
    pad_file.close

# 2. convert blocks of chars into nums (2 digit per char)
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
        char_to_num = ord(char) - 28 # minus 28, to get all nums to become two digit - cons: eliminate some ascii characters
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
    num = ""
    
    while True:
        counter += 1
        char = convert_from.read(1) # read one char at the time
        if not char: # end of file --> break loop
            break
        elif char == whitespace: # reduce counter to correct counts ascii chars - remember whitespace is a char
            counter -= 1
        else:
            num += char #store num before converting to ascii
            
        if (counter % plain_txt_chars_per_block == 0 and (num != "" or num != '') ): # write to file - you have a num correspodning to a ascii char
            num = num.lstrip('0')
            num = int(num)
            num = num + 28 # convert back to ascii --> therefore + 28
            num = chr(num)
            convert_to.write(num)
            num = ""
    
    convert_to.close()
    convert_from.close()
    
# 4. unpadding chars 
def unpad_txt(p_text, input_padded_text):
    plain_txt = open(p_text, "w")
    padded_txt = open(input_padded_text, "r")
    pad_msg = padded_txt.read()
    plain_msg = pad_msg.rstrip("X")
    plain_txt.write(plain_msg)