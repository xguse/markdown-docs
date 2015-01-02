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


# 2015-01-02 (Friday) #

## Writing Methods ##

- `[X]` Functional Annotations
    - done-ish at 2015-01-02 08:58
- `[_]` Linkage
    - __STILL NEED TO DO THIS ANALYSIS...__

## Linkage Analysis ##

- Still not understanding how you can calculate LD without phased data but it __seems__ like many programs claim to...

### PLINK ###

- [v1.90 user manual: LD section ](https://www.cog-genomics.org/plink2/ld)
- `[X]` create the files needed from the master VCF file (tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.vcf)
    - looks like `plink` now reads VCF (`v1.90`): will try this first.
- `[X]` split data into smaller pieces to parallelize the `plink` analysis.
    - looks like the `--parallel` flag will allow `plink` to take care of this.
- `[X]` start run(s) on `louise`.
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

- `[X]` create `ipython` notebook file
    - [YALE/ddrad58/2015-01-02_Plot_PLINK_results.ipynb](http://localhost:8888/jupiter/notebooks/YALE/ddrad58/2015-01-02_Plot_PLINK_results.ipynb)
- `[_]` write code to plot 

## TODO for Gisella ##

- `[_]` re-read grant bit about bioinformatics and think about how to use Hongyu Zhao.