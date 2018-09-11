# **Master Challenge - 50 pts**
```
I really need to login to this website, but the developer hasn't implemented login yet. Can you help?
```
Congrats on getting this far! Just one more challenge to go...

### **Step 1 - go to the website and look around**
Inspecting the source we can see...

![yonder](/home/bryce/Pictures/jsThing.png)

that there's a .js script that has not implemented the authentication yet, and instead returns everything as false.

### **Step 2 - interact with Javascript directly**

To do this, I used BurpSuite, which you can configure through your browser as a proxy.

![burpsuite](/home/bryce/Pictures/burpsuite.png)

Go to the website, and enter any password, and submit. You should get a notification in the 'Intercept'

![burp1](/home/bryce/Pictures/burp1.png)

Looking now, we have intercepted the HTTP POST request to 'login'. Looks useful! And there's a parameter we can change... let's make it true...

![burp2](/home/bryce/Pictures/burp2.png)

and there ya have it, level 1 complete. Congrats.




flag{client_side_is_the_dark_sidebde1f567656f8c9b654a1ec24e1ff889}
