# **Programmers Assemble - 75 pts**

```
You found a text file with some really low level code.
Some value at the beginning has been X'ed out. Can you 
figure out what should be there, to make main return 
the value 0x1? Submit the answer as a hexidecimal number,
with no extraneous 0s. For example, the decimal number 2015
would be submitted as 0x7df, not 0x000007df
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
So what's going on here? We have to look backwards.

To have a return value of `0x1` we need to get to the *good* subroutine, and the only way there is through `fin`

At that point, `%ebx` must equal `0xdc98`. To get there, we look at `loop`, which calls `fin` when `%eax` is 0.

if `%eax` != 0,
#### %ebx += %ecx
#### %eax -= 1

So `%ecx` is being added to `%ebx` `%eax` times! And in `main`, `%ebx` and `%ecx` are `0x8`, so we can form a general equation:

#### `%ebx = 0x8 * %eax`

For us to return 1, `%ebx` is equal to `0xdc98`, so this simplifies to:

#### `0xdc98 = 0x8 * %eax`
and therefore,
`%eax` = **0x1B93**

Input above, and shabang.


flag{0x1B93}
