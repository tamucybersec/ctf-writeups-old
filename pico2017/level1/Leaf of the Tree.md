# **Leaf of the Tree - 20 pts**

```
We found this annoyingly named directory tree starting at /problems/a47d10dd80018fc6e7e1c5094c1ca323. It would be pretty lame to type out all of those directory names but maybe there is something in there worth finding? And maybe we dont need to type out all those names...? Follow the trunk, using cat and ls!
```

Just like the last challenge, we just need to get more comfortable with the commmand line to approach these simple problems.


### **Solution**
A great way to map out a directory is to use the 'find' command.

Travel to the directory in /problems, and simply use 'find'. The output should be something like

```
shreder613@shell-web:/problems/a47d10dd80018fc6e7e1c5094c1ca323$ find                 
.                                                                                     
./trunk                                                                               
./trunk/trunkbe9c                                                                     
./trunk/trunkbe9c/trunk8ec3                                                           
./trunk/trunkbe9c/trunk8ec3/branch4118                                                
./trunk/trunkbe9c/trunk8ec3/branch4118/leaf33d8                                       
./trunk/trunkbe9c/trunk8ec3/trunk708d                                                 
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c                                       
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/branchcd3c                            
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/branchcd3c/leaf29a9                   
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/branchcd3c/leaf280d                   
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b                             
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/branch8979                  
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/branch8979/leaf184f         
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/branch8979/leaf52a9         
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c                   
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/trunkc000         
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/trunkc000/flag    
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/trunkc000/branch82
11                                                                                    
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/trunkc000/branch82
11/leaffbf3                                                                           
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/branch67f2        
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/branch67f2/leaf5dd
4                                                                                     
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/branch67f2/leaf781
3                                                                                     
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/branch3c2e        
./trunk/trunkbe9c/trunk8ec3/trunk708d/trunk664c/trunk430b/trunk122c/branch3c2e/leaff81
e
```

Obviously, to avoid this clutter in the future, pipe it to grep. `find | grep flag` is better, especially when the directory you're looking through is much bigger than this one.




flag{5e3d48f32a6d6e17a8102d3cbae36283}
