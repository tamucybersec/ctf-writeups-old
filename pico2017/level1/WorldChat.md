# **WorldChat - 30 pts**

```
We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:7911. Remember to use Ctrl-C to cut the connection if it overwhelms you!
```
This challenge hints on the need to filter a lot of information out through the command line.

### **Step 1 - nc into port and check it out**
You should know how to do this by now. And, there's WAY too much information going on to see any flags.

### **Step 2 - use 'grep' to filter out fluff**
```
nc shell2017.picoctf.com 7911 | grep flag
```
is a decent choice, however, since some of the users contain 'flag' in their username, it is better to be smart and include a space and a hyphen, as the eighths of the flag contain that format, so:
```
nc shell2017.picoctf.com 7911 | grep 'flag -'
```

the flag should come to you by eighths, and then you just have to piece them together...


flag{08bc0aa64ab97621e512d2e46d8bdab3}
