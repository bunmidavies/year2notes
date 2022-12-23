[[COMP22111]]

==superscalar extensions are able to increase stream throughput== 
refer to the definition of throughput within [[clock period]]

by breaking up 32 bit registers into vectors, as specified by certain instructions, you can increase throughput by performing multiple operations within a singular clock cycle, which increases performance overall

==superscalar schedules operations at runtime== this differs to [[VLIW]], which is its own type of ISA aimed at providing parallelism and increasing throughput as well 