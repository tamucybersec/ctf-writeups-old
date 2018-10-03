# **A Thing Called the Stack - 60 pts**

```
A friend was stacking dinner plates, and handed you this, saying something about a "stack". Can you find the difference between the value of esp at the end of the code, and the location of the saved return address? Assume a 32 bit system. Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df
```

Here they give us assembly code. If you are unfamiliar with assembly and how it works, I highly recommend watching [this](https://www.youtube.com/watch?v=75gBFiFtAb8) video for a very basic introduction to assembly and how it works. A quick note: the video goes over x86 assembly, but not AT&T syntax, which is used here.

### **Inspect assembly.s**

```
foo:
  1.  pushl %ebp
  2.  mov %esp, %ebp
  3.  pushl %edi
  4.  pushl %esi
  5.  pushl %ebx
  6.  sub $0xc0, %esp
  7.  movl $0x1, (%esp)
  8.  movl $0x2, 0x4(%esp)
  9. movl $0x3, 0x8(%esp)
  10.  movl $0x4, 0xc(%esp)
```

I've numbered each line, so let's go, number by number, on what's going on here.

1: %ebp *base pointer* is pushed onto the stack. This denotes the bottom bound of a function on the stack.
2: We are moving %esp *stack pointer* at the same location as %ebp to create the new frame.
3, 4, 5: we are pushing registers %edi, %esi, %ebx into the stack, however, they are not placed within the frame or stack pointer, so they *are* not counted!
6: Adding $0xc0==12x16=192 bytes to the stack pointer. This is done to store local variables.
7: Stores variable $0x1=1 to address ($esp) 192+4=196
8: Stores $0x2=2 to 0x4($esp) 196+4=200
9. Stores $0x3=3 to 0x8($esp) 200+4=204
10. Stores $0x4=4 to 0xc($esp) 208+4=212

The stack pointer is at 208, so let's convert 208 to hex ==0xd0


flag{0xd0}
