# **loooooong - 20 pts**

```
I heard you have some "delusions of grandeur" about your typing speed. How fast can you go at shell2017.picoctf.com:41123?
```
A lot of this challenge involves past things we've done.


### **Step 1 - nc into port**
```
nc shell2017.picoctf.com:41123
```
You'll be met by a prompt telling you to print x amount of characters in the next 30 seconds. Obviously you can't type those out efficiently... so how can you do it?

### **Step 2 - open another terminal and use Python to generate string**
```
python -c "print 'A'*676 + '8'"
```
is an example of how to print 676 A's followed by an 8. Once the output goes into the other terminal, copy and paste into the one connected to picoctf.


flag{with_some_recognition_and_training_delusions_become_glimpses_040b5dbaa85682f120e15e7d1224f09c}
