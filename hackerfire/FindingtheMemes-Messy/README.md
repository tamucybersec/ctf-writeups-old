# Finding the Memes - 200pts

In this challenge, you'll need to find the name of the table that the challenge is currently using. This is a common tactic used in SQL Injection to enable hackers to extract data from other portions of the database.  

http://104.236.124.19:8002  

## Solution

In the previous two web challenges I was able to get away with the classic sql injection `' OR 1=1; -- a`. 
It looks like I won't be able to get away with that this time around.  
The hint is that the flag is the name of the table. I knew that one way to get a table name in MySQL is with the query:  
`SELECT table_name FROM information_schema.tables`  
  
So I planned on try structuring my SQL injectoin around that query.  
To do this I also made use of the SQL `UNION` operator. What `UNION` does is simply takes the results from two different
`SELECT` statements and combine them to make one result. My first attempted SQL injection was to simply do:  
`a' UNION SELECT table_name from information_schema.tables; -- a`.  
  
However I got the error: `The used SELECT statements have a different number of columns`.  
After some googling around I figured out in SQL statements you can repeat results by simply repeating the what is selected in the statement.
For example `UNION SELECT table_name, table_name from information_schema.tables` will return two columns containing the same result. 
Because I saw that two only the two columns name and link are displayed on the page I first tried the injection: `a' UNION SELECT table_name, table_name from information_schema.tables; -- a`  
  
However I got the same error:  
`The used SELECT statements have a different number of columns`.  
So I simply decided to brute force the number of columns. Luckily for me the number of columns was only three so the following injection worked:  
`a' UNION SELECT table_name, table_name, table_name from information_schema.tables; -- a`  
  
The output contained all of the standard SQL tables and at the very bottom of the page was:  
`flag{w3lc0me_t0_th3_m3m3side}                  flag{w3lc0me_t0_th3_m3m3side}`
