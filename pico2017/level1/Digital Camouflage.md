# **Digital Camouflage - 50 pts**

So, we want access to "some routers," and we're given a .pcap file. We must analyze the traffic
for any credentials.


Files:
data.pcap



## *Solution*
The easiest way to analyze packets is through wireshark.

We could look through each packet individually, but it'd be smarter to focus on the protocols which
pose the most weakness. Let's check for http (unencrypted) web traffic. A good way to look at the
entirety of the communications is to follow the streams using wireshark.

Looking through the streams, we find something:

We can see "userid=grassers" and a password that looks kind of like gibberish. Glancing at the
'%3D' on the end, we can reasonably infer that this password in url encoded on top of base64
encoding. Decrypting it will render us the answer.


Flag: 'prvqBZNqYw'
