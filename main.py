    #Main program file - running the RSA encryption code
import text_padding
import rsa
import plainText


a = rsa.gcd((9-1), 15)
b = rsa.gcd((7), 15)
c = rsa.gcd((17-1), 15)
d = rsa.gcd(15, 49)
e = rsa.gcd(15, 327)

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



bob_p = rsa.gen_prime(90000, 91000)
bob_q = rsa.gen_prime(90000, 91000)
bob_n = rsa.gen_modulus(bob_p, bob_q)
bob_e = rsa.gen_public(bob_p, bob_q)
bob_d = rsa.gen_secret(bob_p, bob_q, bob_e)

alice_p = rsa.gen_prime(90000, 91000)
alice_q = rsa.gen_prime(90000, 91000)
alice_n = rsa.gen_modulus(alice_p, alice_q)
alice_e = rsa.gen_public(alice_p, alice_q)
alice_d = rsa.gen_secret(alice_p, alice_q, alice_e)

########## Bob sends message to Alice
print(plainText.ptextOrg)
message = plainText.ptextOrg
print("Bob to Alice: ",message)
plain_txt = open (bob_plain_text, "w")
plain_txt.write(message)
plain_txt.close()
text_padding.pad_txt(bob_plain_text, bob_pad_text) # Bob pads the plain message
text_padding.convert_to_num(bob_pad_text, bob_convert_to_num_text, bob_n) # Bob converts the padded plain message to numbers
rsa.encrypt(alice_e, alice_n, bob_convert_to_num_text, bob_cipher_text, 4) # Bob encrypts the numbers to block ciphers


## Alice decrypts Bobs message
rsa.decrypt(alice_d, alice_n, bob_cipher_text, bob_decrypt_convert_to_num_text, 4)
text_padding.convert_to_char(bob_decrypt_pad_text, bob_decrypt_convert_to_num_text)
text_padding.unpad_txt(bob_decrypted_plain_text, bob_decrypt_pad_text)


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

text_padding.pad_txt(alice_plain_text, alice_pad_text) # Alice pads the plain message
text_padding.convert_to_num(alice_pad_text, alice_convert_to_num_text, alice_n) # Alice converts the padded plain message to numbers
rsa.encrypt(bob_e, bob_n, alice_convert_to_num_text, alice_cipher_text, 4) # Alice encrypts the numbers to block ciphers

## Bob decrypts Alice message
rsa.decrypt(bob_d, bob_n, alice_cipher_text, alice_decrypt_convert_to_num_text, 4)
text_padding.convert_to_char(alice_decrypt_pad_text, alice_decrypt_convert_to_num_text)
text_padding.unpad_txt(alice_decrypted_plain_text, alice_decrypt_pad_text)
plain_txt = open (alice_decrypted_plain_text, "r")
message = plain_txt.read()
print("Bob receives from Alice: ", message)

