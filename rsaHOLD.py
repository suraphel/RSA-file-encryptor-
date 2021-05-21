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
