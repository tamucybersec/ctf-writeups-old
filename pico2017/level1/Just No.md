# **Just No - 40 pts**

```
A program at /problems/579fe8ee083cd54f55718c1324687c74 has access to a flag
 but refuses to share it. Can you convince it otherwise?
```

A lot of this challenge is looking beyond the surface of a program. If you're struggling,
it helps to look at the *hint*:

```
Check out the difference between relative and absolute
paths and see if you can figure out how to use them to
solve this challenge. Could you possibly spoof another
auth file it looks at instead...?
```

... and that's precisely what we'll do.


### **Step 1: analyze 'justno.c' using xxd or hexdump**
![justNO1](../.picopics/justNO1.png)

command I used here: `hexdump -C justno.c | less`

As you can see, this program accesses the file 'auth', however it uses the *relative*
path of ../../problems/579fe8ee083cd54f55718c1324687c74. How could that be an
issue, and more importantly, how can we exploit that?


### **Step 2: create a 'fake' relative path**
We have no write-permissions on the 'auth' file in this directory, so we have to trick
the program into reading a file 'auth' with something other than 'no'.
To do this, we will have to create a new directory /problems/579fe8ee083cd54f55718c1324687c74 somewhere in the filesystem. I chose to create in /tmp.
```
mkdir -p /tmp/yoyo123/problems/579fe8ee083cd54f55718c1324687c74
```


### **Step 3: create 'auth' in new directory and run justno**
So, now we need to make a 'auth' file with something other than 'no', and then run the program 'justno'
```
cd /tmp/yoyo123/problems/579fe8ee083cd54f55718c1324687c74
echo yespls > auth
/problems/579fe8ee083cd54f55718c1324687c74/justno
```
![justNO2](../.picopics/justNO2.png)

Awesome, flag acquired.





flag{37df41ffe2da397584c43eabf8a50ee3}
