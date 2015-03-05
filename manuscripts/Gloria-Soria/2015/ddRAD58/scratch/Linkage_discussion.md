# Introduction: #

## Linkage disequilibrium ##

Briefly, linkage disequilibrium is the co-occurrence of pairs of alleles within chromosomes in a population at frequencies more elevated or depressed than would be expected if given the overall frequencies of each allele in the population assuming completely random assortment between alleles.  However, alleles are __not__ able to assort in a completely random fashion. In reality, the distance between loci is _inversely proportional_ to the rate of recombination ("mixing") between chromosomal loci. So LD values can not be directly compared between arbitrary groups of allele-pairs.  One must either know the species-specific recombination rate or restrict comparisons to pairs with similar distances and thereby roughly fix the rates of recombination being compared.

## _Glossina fuscipes fuscipes_ ##


We do not know the recombination rate of _G. f. fuscipes_.  Therefore the methods that I have employed below have focused on controlling the effect of variable recombination rates by constructing bins of SNP-pairs that are located on contiguous chromosomal contigs (__not__ considering phasing or diploid/haploid membership) and have similar distances.  For example all SNP-pairs separated by the interval on a supercontig of $[i,j)$ where $|i-j| \sim 100$.


----

# First thoughts and notes about first thoughts:

Where these data approximatly normal-looking one might use a z-score or modified z-score (_median absolute devation_ instead of std-dev) to set a semi-principled threshold for a value being considered "interesting".  But these are __not__ even a little "Normal" looking.

I then thought about using an Exponential distribution to model them but it can not accommodate the types of data we observe in the shorter distances which have concentrations at the high-end of the $r^2$ spectrum as well.  This may not be a big deal in practice, however,  as that pattern is not common in most distance-bins.  The fact that the support for the Exponential distribution is $[0,\inf)$ while our data __can only__ occur over $[0,1]$ does bother me a bit though.

This has led me to the Beta distribution, which in its 2 parameter formulation ($\mathrm{Beta}(\alpha, \beta)$) only supports values over $(0,1)$.  However in a four parameter formulation ($\mathrm{Beta}(\alpha, \beta, a, c)$) accommodates values along $[a,c]$ by scaling linearly $[a,c]$ to within the Beta's normal support interval.

Below, I will go through what I have done to explore these distributions with our data.


## Exponential model of distance bin's $r^2$ for MCMC learning:

For `pyMC` we must build model components separately and add them to the model proper. First we must model the Exponential's parameter $\lambda$. I have selected a Gamma distribution for this. Then we will initialize the values of the Gamma distribution using the observed bin data. This model of the $\lambda$ parameter will be added to the Exponential distribution model and the Exponential model will be assigned the observed data to use.  Finally, we will execute both maximum a posteriori (MAP) and Markov Chain Monte Carlo (MCMC)-based learning to arrive at estimations of the $\lambda$ parameter value based on the observed data and compare results.