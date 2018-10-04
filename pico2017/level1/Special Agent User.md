# **Special User Agent - 50 pts**


We need to figure out the user string to determine what browser the administrator is using for a
future exploit. We are given a traffic file.


Files:
data.pcap


## *Solution*
Firstly, to find the browser agent, we should filter out traffic unrelated to the internet and
monitor streams to find the user agent.

On TCP stream 3, we find the 'User-Agent:' string. Utilize an online resource, like www.useragentstring.com
and analyze.


Flag: 'Chrome 36.0.1985'
