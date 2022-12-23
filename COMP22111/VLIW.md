[[COMP22111]]

Most CPU [[ISA]]s allow programs to specify singular instructions to be performed in sequence e.g. ADD then BRA then CMP

a VLIW ISA allows programs to specify muiltiple instructions to be executed in parallel. This can be achieved through having multiple ALUs for instance, but a singular PC

VLIW works well for linear algebra, and "zero-overhead" loops

==VLIW operations are scheduled with the compiler==. This differs to how [[superscalar extensions]] schedules operations