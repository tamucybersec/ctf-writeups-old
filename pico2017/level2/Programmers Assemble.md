# **Programmers Assemble - 75 pts**

```
You found a text file with some really low level code. Some value at the beginning has been X'ed out. Can you figure out what should be there, to make main return the value 0x1? Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df
```

We are given another piece of assembly code, but this time with multiple functions and using Intel syntax instead of AT&T. We are trying to find the value at the beginning, in the first line of main. Let's try to take the same, methodical approach as last time.

### **Inspect assembly.s**
```
.global main

main:
    mov $XXXXXXX, %eax
    mov $0, %ebx
    mov $0x8, %ecx
loop:
    test %eax, %eax
    jz fin
    add %ecx, %ebx
    dec %eax
    jmp loop
fin:
    cmp $0xdc98, %ebx
    je good
    mov $0, %eax
    jmp end
good:
    mov $1, %eax
end:
    ret
```
So what's going on here?

**main:**
  *assign %eax to value $XXXXXXX
  assign %ebx to value 0
  assign %ecx to value 8*
**loop:**
  *zf = bitwise AND of eax,eax
  if zf: goto fin
  %ecx = %ecx + %ebx
  %eax = %eax - 1
  goto loop*
**fin:**
  *val = %ebx == $0xdc98
  if val=1: goto good
  %eax = 0
  goto end*
**good:**
  *%eax = 1*
**end:**
  *return %eax*

So, let's anaylze this program from end to beginning. To end, zf=1, which means %eax=1 from
