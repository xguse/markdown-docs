---
title: Daily Records
subtitle: Caccone PostDoc
date: January, 2015
author: Gus Dunn
documentclass: scrartcl
classoption: letterpaper
toc: 1
graphics: 1
tags: daily notes, ddRAD, argot2, 
header-includes: 
 - \usepackage{bbding}
 - \usepackage[T1]{fontenc}
 - \usepackage{lxfonts}
read: "+simple_tables+table_captions+footnotes+inline_notes+fenced_code_blocks+fenced_code_attributes+fancy_lists+definition_lists+superscript+subscript+tex_math_dollars"
...



<!-- 

------------------------------------------


# 2014-12-26 (Friday) #

## T: Functional Annotations of genes near SNPs of interest ##

- `[_]` write code to create table of functional annotation info, given gene-names and annotation database.
    - `[_]` draft in ipython notebook
    - `[_]` copy to `spartan`
- `[_]` write methods for the functional annotation paper section -->


------------------------------------------

# 2015-01-02 (Friday) #

## Writing Methods ##

- `[x]` Functional Annotations
    - done-ish at 2015-01-02 08:58
- `[_]` Linkage
    - __STILL NEED TO DO THIS ANALYSIS...__

## Linkage Analysis ##

- Still not understanding how you can calculate LD without phased data but it __seems__ like many programs claim to...

### PLINK ###

- [v1.90 user manual: LD section ](https://www.cog-genomics.org/plink2/ld)
- `[x]` create the files needed from the master VCF file (tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.vcf)
    - looks like `plink` now reads VCF (`v1.90`): will try this first.
- `[x]` split data into smaller pieces to parallelize the `plink` analysis.
    - looks like the `--parallel` flag will allow `plink` to take care of this.
- `[x]` start run(s) on `louise`.
- `[_]` _try running a `--blocks` PLINK analysis for haplotype blocks to see if its useful?_

__plink commands run and kept:__

~~~~~~~~ {.bash}
plink --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.vcf --allow-extra-chr \
    --r gz with-freqs  \
    --out plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.vcf\
    /ld/r_none_freqs

plink --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.vcf --allow-extra-chr \
    --r gz in-phase with-freqs  \
    --out plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.vcf\
    /ld/r_none_phase_freqs

plink --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.vcf --allow-extra-chr \
    --r triangle gz  \
    --out plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.vcf\
    /ld/r_tri
~~~~~~~~~~~~~~~~~~~ 

### Plot PLINK results ###

- `[x]` create `ipython` notebook file
    - [YALE/ddrad58/2015-01-02_Plot_PLINK_results.ipynb](http://localhost:8888/jupiter/notebooks/YALE/ddrad58/2015-01-02_Plot_PLINK_results.ipynb)
- `[_]` write code to plot 

## TODO for Gisella ##

- `[_]` re-read grant bit about bioinformatics and think about how to use Hongyu Zhao.



------------------------------------------

# 2015-01-03 (Saturday) #

## Linkage Analysis ##

### Plot PLINK results ###

- `[x]`  __WHAT__ should be plotted?
    - `[x]`  what _exactly is_ the $r$ value telling us?
        - `[x]`  does it already take into account the distance?
            - according to [Wikipedia ](http://en.wikipedia.org/wiki/Linkage_disequilibrium#Definition), $r$ is simply the correlation coefficient between pairs of loci:
            $$r=\frac{D}{\sqrt{p_1p_2q_1q_2}}$$
    - It seems like plotting $\frac{r}{l_{a} - l_{b}}$ ($r$ divided by distance) __is__ warranted where:
        - $l_{a}$ is location of SNP$_{a}$
        - $l_{b}$ is location of SNP$_{b}$

- `[_]` write code to plot

#### Questions for Andrea ####

- Some MAFs are zero which causes the LD ($r$) to fail. [link](http://localhost:8888/jupiter/notebooks/YALE/ddrad58/2015-01-02_Plot_PLINK_results.ipynb#LD-as-r-for-Scaffold0:)



------------------------------------------

# 2015-01-05 (Monday) #

## Linkage Analysis ##

### Plot PLINK results ###

- met with Andrea after showing her what I had and specifically the MAF = 0 for about half the `scaffold0` comparisons.
    - __(see meeting notes for more details)__


### Re-Filter original VCF ###

- the incorrect (`--min-allele`/`--max-allele`) filter was used to generate: `tsetseFINAL_14Oct2014_f2_53.recode.vcf`
- the correct filter is `--maf`.
- I am doing it myself with MAF = 0.05 (see below).
- __retained only 47.7% sites__
- __I will be re-running my PLINK LD analysis just in case.__

~~~~~~~~ {.bash}
wd238 at compute-1-4 in ~GENOMES/glossina_fuscipes/annotations/SNPs (py278) 
$ vcftools \
    --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.vcf \
    --maf 0.05 \
    --out tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05 \
    --recode

VCFtools - v0.1.12b
(C) Adam Auton and Anthony Marcketta 2009

Parameters as interpreted:
    --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.vcf
    --maf 0.05
    --out tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05
    --recode

After filtering, kept 53 out of 53 Individuals
Outputting VCF file...
After filtering, kept 73297 out of a possible 153650 Sites
Run Time = 21.00 seconds

~~~~~~~~~~~~~~~~~~~

## Recover dead positives ##

### Dissections ###

- Prepped for dissections and pre-filled the worksheets
- but we are out of the 1.5 ml tubes that I bought for this and I will have to go get some more tomorrow morning.
