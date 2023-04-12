[[COMP22111]]
exists to continue on from [[simulation]], as part of [[verification vs testing]]

*software simulation*
- slow (faster on cluster machines)
- very controllable (as you can insert breakpoints etc)
- offers good observability of all signals (i.e. 'hidden' signals in a chip for debugging)
- can show unknown nodes (X)
- <span style="color:red">timing is approximate, or in some cases some software may have no timing</span>
- affordable

*hardware emulation*
- faster, as you are running the actual hardware
- less controllable, the hardware will just run like its the real thing
- limited observability (logic analysers may be required)
- cannot show unknown nodes
- timing model - it may not be applicable for the actual product to be deployed
- expensive
