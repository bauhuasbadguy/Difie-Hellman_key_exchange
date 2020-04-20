# Diffie Hellman Exchange

#Sources:-
#https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

#Set the public keys as a prime field, p, and its primitive root, g
p = 23
g = 5


#starting random numbers for alice and bob
a = 6
b = 15

#Alice's value to exchange
#A = (g^a) % p
A = pow(g, a, p)

#Bob's value to exhange
#B = (g^b) % p
B = pow(g, b, p)

#Now both sides have to calculate the private key they both agree on

#Alice calculates s = (B^a) % p
Sa = pow(B, a, p)

#Bob calculates s = (A^b) % p
Sb = pow(A, b, p)


#Check they get the same value
print(Sa)
print(Sb)


#Alice and bob have now established a private key
