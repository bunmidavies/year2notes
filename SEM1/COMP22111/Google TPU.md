[[COMP22111]]

==case study as part of week 11==

The v1 of the TPU was launched in 2015, which was only capable of inference. The v2 of the TPU was launched in 2017, which is capable of inference and training.

Inference = classifying the data
Training = building the neural network so that it can be used for inference

==a **tensor** is a generalised matrix, that can map vectors, scalars, and other similar objects==
![](https://i.imgur.com/lVFXocR.png)


*Within neural networks, when given an image (i.e. a grid of pixels), you convert it to a vector - the ==neuron== that recognises the provided image takes the vector values and multiplies it by the parameter values, and sums all the values in the resulting vector. The neuron with the highest result is the ==best match== between the input data and the corresponding parameter*

Above explains that basically neural networks require ==massive amounts== of multiplication and addition. As explained above, ==inference== requires:
- Multiplying the input data with weights
- Adding the results to aggregate the neuron's state into 1 value
- Applying an activation function to module the neurons activity (?)

### CPU with neural network

the CPU is so flexible, and requires a memory access with every calculation due to its [[von neumann architecture]]

this is also known as the von neumann bottleneck - these huge number of neural network calculations are predictable, but the CPUs ALU will execute them individually, accessing memory everytime ==limiting throughput== and ==consuming significant energy==

### GPU with neural network

because [[GPUs]] have thousands of ALUs built within one processor, it means that thousands of calculations can be done simultaneously

this is why ==GPUs are one of the most popular architectures in deep learning==

however, the GPU is still a general purpose processor, designed to support millions of different applications and software, not ==just deep learning==

registers need to be accessed for every single calculation, therefore due to the huge number of ALUs more energy is spent accessing memory, and throughput is limited

### TPU with neural network

the TPU is ==domain specific== - the domain being **a matrix processor specialised for neural networks**

so the TPU cant run many applications like a GPU or CPU can, but can handle neural network calculations at a ==much higher speed== while consuming less power + a smaller physical footprint

TPUs have [[systolic array architecture]] - a physical matrix of multipliers and adders, connected together. This is called the ==MXU==

*The Cloud TPU v2 has two systolic arrays of 128x128, resulting in ==32,768 ALUs== for 16 bit floating point values*

the TPU loads parameters from memory into the matrix, and multiplication results are passed to the the next multiplier, while also performing summation

==no memory access is required during the whole process of calculation==

the TPU also has a ==unified buffer (UB)== and ==activation unit (AU)==

![](https://i.imgur.com/5dmNkD7.png)


note that the ==control unit is very minimal== - the TPU chip is half the size of the other chips, reducing chip cost by a factor of 8

### choosing floating point format

machine learning research has shown that many models can tolerate lower precision calculations ==without loss in accuracy==. [[mixed precision training]]