# **Hex2Raw - 20 pts**

```
This program requires some unprintable characters as input... But how do you
print unprintable characters? CLI yourself to
/problems/9bbf83df34f9c5239f329f977f4a66c1 and turn that Hex2Raw!
```
So, a lot of what's going on is: *how do we represent data in the command line?*


### **Step 1: go into /problems/9bbf83df34f9c5239f329f977f4a66c1**
This can be done via simple CLI commands
```
cd /problems/9bbf83df34f9c5239f329f977f4a66c1
```


### **Step 2: Run ./hex2raw and get your bearings**
The executable will output some text:
```
Give me this in raw form (0x41 ->'A'):                                               
99d9835d83647dcf4cb202a51e1c29bc
You gave me:

```
So, the program wants you to input this hex **99d9835d83647dcf4cb202a51e1c29bc**
in *raw* form. An easy way to do this is to use python.



### **Step 3: input raw form of hex**
Using python is an easy way:
```
shreder613@shell-web:/problems/9bbf83df34f9c5239f329f977f4a66c1$ python -c "print('99d9835d83647dcf4cb202a51e1c29bc'.decode('hex'))" | ./hex2raw
```
This will satisfy the codemonkeys of ./hex2raw, and they will output the next flag....



Flag: 84b0a5a216620b05b1cae86508dad925
