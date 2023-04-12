[[COMP22111]]

**a clock domain** is a specific area of a system which uses one clock signal. Complex systems can be made up of multiple clock domains, as different devices e.g. CPU and RAM may need different clock frequencies

When crossing clock domains, **resynchronisation** is required in order to resolve **metastability** - if metastability is not resolved, signals entering a flip flop from a different clock domain will put the flip flop into an **unknown state**