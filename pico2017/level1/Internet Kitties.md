# **Internet Kitties - 10 pts**

```
I was told there was something at IP shell2017.picoctf.com with port 42354. How do I get there? Do I need a ship for the port?
```

Interestingly, you do not need a ship, you just need a terminal!

### Solution

For this challenge you need to access this IP on a specific port. A good command is netcat:
```
nc shell2017.picoctf.com 42354
```

And boom, that easy, you get the flag below.

flag{74d4fd0abc13a085d6d60489db227dfd}
