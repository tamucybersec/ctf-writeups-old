# **What is Web - 20 pts**

```
Someone told me that some guy came up with the "World Wide Web", using "HTML" and
"stuff". Can you help me figure out what that is? Website.
```

In this challenge, you will learn how to gain information on websites and how
the front end of a website works.

### **Step 1: go to [Website.](http://shell2017.picoctf.com:58191/) and "View Page Source"**

This can be done through virtually any browser. Notice at the bottom of the page...

```
<!-- Cool! Look at me! This is an HTML file. It describes what each page contains in a format your browser can understand. -->
<!-- The first part of the flag (there are 3 parts) is 4eabea7c5b1 -->
<!-- What other types of files are there in a webpage? -->
```

So, we have to look for the other two files that are linked onto this page. Hint:
there's a .css file and a .js file that may or may not contain the other parts of
the flag.


flag{4eabea7c5b1e8e0c84cc612a79d2dc833}
