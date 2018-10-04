# **Bash Loop - 40 pts**

```
We found a program that is hiding a flag but requires you to guess the number it is thinking of. Chances are Linux has an easy way to try all the numbers... Go to /problems/e3f1970eb419b3aa32788a43ec91ef08 and try it out!
```

This is placed inside the "binary exploitation" category, but it can easily be
solved with some CLI wizardry.


### **Step 1: go into directory and examine program**
Try out the program, think about how you could tell your computer to guess every
single possibility the program asks, from 0 to 4096...

### **Step 2: execute**
A for-loop works quite well in this situation:

```
for i in {0..4096}; do ./bashloop $i | grep 'flag'; done
```

The output should be pretty simple and out in front. Paste the flag into the
box to get 40 points...



flag{9960332950d7db392f97f29dee04f4ee}
