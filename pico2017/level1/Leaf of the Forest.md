# **Leaf of the Forest - 30 pts**
```

We found an even bigger directory tree hiding a flag starting at /problems/db39b5c002d8445dc6d2bbf49a8ccc37. It would be impossible to find the file named flag manually...

```

We definitely can find it manually! WE just have to pipe 'find' into another command...

# Solution
```
find | grep flag
```
Since they gave us the name of the file 'flag', we can use grep to search through the output of 'find'. Check.




flag{c99501b0fe95402ed1c9191102fe1b68}
