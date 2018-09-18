# **Meta Find Me - 70 pts**

```
Find the location of the flag in the image: image.jpg. Note: Latitude and longitude values are in degrees with no degree symbols,/direction letters, minutes, seconds, or periods. They should only be digits. The flag is not just a set of coordinates - if you think that, keep looking!
```

Welcome to level 2! Now, we are given just a single image file, and somewhere there is the flag...

### **Step 1: Download file and inspect**
*Steganography* is hiding something--a message, file, audio, etc--in another file.

By far the easiest thing to do here is find the coordinates. Just open the image, and inspect the tags. They are given plainly.

### **Step 2: check ALL of the file**
A good way to sort of get a glimpse into what's in a file is to use `strings /path/to/file`, and since we're looking for a flag, it'd probably be a good idea to pipe it into grep...

![metafindme](../.picopics/MetaFindMe.png)


... jackpot! Put those two together and you get the flag.


flag{flag_2_meta_4_me_7_100_1c84}
