# **Raw2Hex - 20 pts**

```
This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it! CLI yourself to /problems/608e5f8b55c005ae6bc4ff13393c9c23 and turn that Raw2Hex!
```
This is basically just like the previous challenge, Hex2Raw, but we are doing the
reverse this time.

### **Step 1: go into /problems/608e5f8b55c005ae6bc4ff13393c9c23**
Simple CLI command 'cd' will do the trick
```
cd /problems/608e5f8b55c005ae6bc4ff13393c9c23
```


### **Step 2: Assess the program ./raw2hex**
Convert the output of the program using `xxd`

```
./raw2hex | xxd -plain
```

This will output hex which will translate to "The flag is:=¬ÓC]Y¤+ø=|DÍ2".
We have the flag, but we need to remove the beginning part of the message.


### **Step 3: Find a way to reduce the output to the flag only**
You can look through the hex to find the colon, but it's also pretty easy to
use something like "cut"

```
./raw2hex | cut -d ':' -f 2 | xxd -plain
```

from there, you should get the output of only the flag, and proceed to the next
level.


Flag: 3dacd3435d59a4862b9ff83d7c44cd320a
