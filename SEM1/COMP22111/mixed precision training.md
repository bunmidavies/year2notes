[[COMP22111]]

as was being discussed within [[Google TPU]], ML research has found that despite lowering the precision of some calculations, you can still end up with the same amount of accuracy

==mixed precision training== uses operations of lower precision (float16, bfloat16) in a model to:
- use less memory
- run faster

MSFP16 is an example of a floating point format which achieves 3x lower cost than bfloat16, while delivering comparable/same accuracy - the trick is through using a ==shared exponent== to achieve dynamic range