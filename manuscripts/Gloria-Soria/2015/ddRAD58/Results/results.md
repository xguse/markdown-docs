---
title: Gloria-Soria (ddRAD58)
author: Gus Dunn
date: 2014-12-29
documentclass: scrartcl
classoption: letterpaper
geometry: margin=1in
toc: 1
graphics: 1
tags: [manuscript, methods, ddRAD58]
bibliography: methods.bib
csl: ../plos.csl
read: "+simple_tables+table_captions+footnotes+inline_notes+fenced_code_blocks+fenced_code_attributes+fancy_lists+definition_lists+superscript+subscript+tex_math_dollars"
header-includes: 
- \usepackage{fontspec}
- \setmainfont{Linux Libertine O}
...


# Functional Annotations #

## Argot2 Analysis ##

### Dataframe for results ###

__GENE__
- genename
- snp_contig
- snp_bp
- 


# Linkage Analysis #

## Linkage measurements ##


## LD-based filtering of SNP-pairs ##



### Scaling of binned $r^2$ distributions ###



### Bayesian parameter estimation using the binned $r^2$ distributions ###

In order to use the CDF of the Beta distribution to assign significances to each observed SNP-pair in a bin, it is necessary to learn the distribution parameters ($\alpha$ and $\beta$) for each bin given the specific data in each bin.
For this we used custom python code that made heavy use of the following third-party data analysis modules: Pandas [@mckinney-proc-scipy-2010], NumPy [@VanDerWalt2011], SciPy [@Jones2001scipy], pyMC [@Patil2010pymc],  and StatsModels  [@statsmodels].

We used pyMC to build the model of the Beta distribution and use it to exploit the bin-specific data to estimate the bin-specific values for the $\alpha$ and $\beta$ parameters of the model [Figure fig_betamod].
The values of $\alpha$ and $\beta$ were modeled with separate Uniform prior distributions from 0.01 to 10.
This model topology was used to create pyMC "model" objects and initialized with the $r^2$ data from each bin.
The parameters of each Beta distribution were then estimated by _maximum a posteriori_ (MAP) and used to calculate the $1-\mathrm{CDF}$ for each SNP-pair in each bin [@Jones2001scipy;@VanDerWalt2011].
The $1-\mathrm{CDF}$ values were then BH corrected by bin and filtered with a threshold of $(1-CDF)_{BH} \le 0.01$ using statsmodels [@Benjamini1995].


<div id="fig_betamod">
![__[fig_betamod]Network representation of the LD Beta model:__ Ovals represent modeled probability distributions. Circles represent learned parameters. Grey shading indicates use of observed data. \label{fig_betamod}](../figures/bin_MAP_model.png)

</div>

<!-- ################################################################## -->
\newpage
<!-- ################################################################## -->

# Bibliography #