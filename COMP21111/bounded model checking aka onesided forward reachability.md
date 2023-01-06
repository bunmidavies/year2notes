[[COMP21111]]

==procedure== FReach(I, T, F)
==input== = formulas(I,T,F)
==output== = "yes" or no output
**begin**
	i := 0;
	R := I($\bar{x}_0$);
	loop
		if $R\land F(\bar{x}_i)$ is satisfiable then return "yes";
		$R := R \land T(\bar{x}_i,\bar{x}_{i+1})$;
		i += 1;
	end loop
**end**