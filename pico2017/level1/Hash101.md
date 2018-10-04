# **Hash101 - 50 pts**

This challenge is designed to introduce you into more cryptography beyond basic ciphers, as well as familiarize yourself with how information is stored and represented within computers.


## **Solution**
Firstly, they require you to access a service on a certain port. Netcat:
```
nc [website] [port]
```
will do the trick easily.

Once there, you will be put through a series of questions testing your knowledge on binary, hexadecimal, decimal, and ascii. These are various methods in which data, through a computer, are stored.


### **Levels 1-2**
The first two levels will just test your basic knowledge and wits to convert from hex to ascii (ascii being a common way to represent text), binary to hex, hex to decimal, etc. Tip: understand the concepts, then use online resources to do the legwork for you.


### **Level 3**
The level explains how hashing functions work. Try to find a string that will meet the specifications of the level. My level told me to get a *remainder* of 2 after dividing by 16 (modulus 16). 2 in ascii is 50 in decimal, so the remainder after dividing 50 by 16 is 2.


### **Level 4**
Here, they give you a MD5 hash. Like they explain, brute forcing a MD5 hash would take a very long time, given that the password is a good one. However, most of the time, people don't have good passwords... a good resource for trying to crack MD5 hashes is [here](https://hashkiller.co.uk/md5-decrypter.aspx)
Mine came back as "lymph" and I received the flag.



Flag: 605911fee24de43af8ebe50ec7d210ec
