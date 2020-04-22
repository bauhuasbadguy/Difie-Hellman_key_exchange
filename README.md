## README ##

In this script I wrote an example of the Diffie-Hellman key exchange for my own understanding. 

Put very simply the algoritm involves taking turns moving round a circle by an amount only you know. Then you all end up in the same place.

The Diffie-Hellman key exchange is designed so that two actors, Alice and Bob can create a shared encryption key without a third party (Eve) being able to discover the key by evesdropping on their messages. This is what is meant by public/private key encryption. Alice and Bob will decide two shared public keys, the first of which is the modulus which is the circumfrence of our circle and should be a prime number. The second is the base g which is a primitive root modulo of p, i.e. its powers can be any value under p by taking g to the required power (this is confusing and badly explained here so see the sources). This means that the largest possible secret key generated using this method is p.

Alice and Bob will then take the values of g and p and use them to calculate m = g<sup>k</sub>%p, where k is their private keys, taking them some number of rotations around the circle. They then share their messages publicly and then repeat with g being substituted for each others messages. They will then both get the same value which can be used as the shared encryption key. 


This process can be repeated within an arbitrarily large group as required.

### IMPORTANT NOTE ###

I am just some guy in a room. If you are trying to understand the algorithm I hope you will find this useful but if you're using this IRL use a version made by someone actually qualified.

### Sources ###

* https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
* https://math.stackexchange.com/questions/795414/what-are-primitive-roots-modulo-n