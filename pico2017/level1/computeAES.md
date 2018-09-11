# **computeAES - 50 pts**

You found something laying about... find out what it says?


```
Encrypted with AES in ECB mode. All values base64 encoded
ciphertext = V3Vqirostg6qW26sle5mnyrwEYSrteN6oHkilO50e9dFkN+0JhC3yu0LcQNw/hXU
key = r7y1dhmTvjQrcra7A1UQFw==
```

### Step 1: decode base64 and represent in hexadecimal
This can be done with online resources, or a python script. We need to convert the data to hex so we can decrypt it.


### Step 2: decrypt ciphertext using key
There are lots of websites which can do this for you. AES w/ ECB. I used [this](http://extranet.cryptomathic.com/aescalc/index) one.


### Step 3: convert output to ascii
And you shall get the flag!



Flag: do_not_let_machines_win_6a68a292
