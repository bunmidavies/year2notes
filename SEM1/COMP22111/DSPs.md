[[COMP22111]]

DSPs (digital signal processors) take real world signals (e.g. voice, video, temperature) that have already been digitised, and perform mathematical operations on them

![](https://i.imgur.com/g6ePwzM.png)


in this example, the DSP is performing MP3 encoding, and saves the file to memory

today, general purpose processors have become more powerful, and come closer to taking over all the responsibility of devices like the DSP. Instructions + hardware have been added to general purpose processor ISAs / hardware to give support in areas like DSP

e.g. SIMD instruction extensions (Single Instruction Multiple Data) - SIMD instructions are combined with superscalar in order to perform multiple instructions in a singular clock cycle

more info within [[superscalar extensions]]