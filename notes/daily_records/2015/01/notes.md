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





------------------------------------------

# 2015-01-02 (Friday) #

## Writing Methods ##

- `[x]` Functional Annotations
    - done-ish at 2015-01-02 08:58
- `[ ]` Linkage
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
- `[ ]` _try running a `--blocks` PLINK analysis for haplotype blocks to see if its useful?_

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
- `[ ]` write code to plot 

## TODO for Gisella ##

- `[ ]` re-read grant bit about bioinformatics and think about how to use Hongyu Zhao.



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

- `[ ]` write code to plot

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

### PLINK - rerun ###

~~~~~~~~ {.bash}
plink --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf \
--allow-extra-chr \
--r gz with-freqs dprime \
--out plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r_none_freqs_dprime
~~~~~~~~~~~~~~~~~~~




## Recover dead positives ##

### Dissections ###

- Prepped for dissections and pre-filled the worksheets
- but we are out of the 1.5 ml tubes that I bought for this and I will have to go get some more tomorrow morning.



------------------------------------------

# 2015-01-06 (Tuesday) #

## Linkage Analysis ##

- emailed Dan about looking over the results.
- Should probably run them by Jeff if he has time too.

### PLINK `--make-bed` ###

~~~~~~~~ 
wd238 at compute-1-4 in ~GENOMES/glossina_fuscipes/annotations/SNPs (py278) 
$ plink --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf \
> --allow-extra-chr \
> --maf 0.05 \
> --make-bed \
> --out tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.plink

PLINK v1.90b2o 64-bit (25 Nov 2014)        https://www.cog-genomics.org/plink2
(C) 2005-2014 Shaun Purcell, Christopher Chang   GNU General Public License v3
Logging to tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.plink.log.
48251 MB RAM detected; reserving 24125 MB for main workspace.
--vcf: 73k variants complete.
tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.plink-temporary.bed
+
tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.plink-temporary.bim
+
tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.plink-temporary.fam
written.
73297 variants loaded from .bim file.
53 people (0 males, 0 females, 53 ambiguous) loaded from .fam.
Ambiguous sex IDs written to
tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.plink.nosex .
Using 1 thread (no multithreaded calculations invoked).
Before main variant filters, 53 founders and 0 nonfounders present.
Calculating allele frequencies... done.
Total genotyping rate is 0.965098.
0 variants removed due to MAF threshold(s) (--maf/--max-maf).
73297 variants and 53 people pass filters and QC.
Note: No phenotypes present.
--make-bed to
tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.plink.bed +
tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.plink.bim +
tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.plink.fam ...
done.

~~~~~~~~~~~~~~~~~~~

### PLINK `--blocks` ###

- running with `--blocks` option to look at estimated haplotype blocks

~~~~~~~~ 
wd238 at compute-1-4 in ~GENOMES/glossina_fuscipes/annotations/SNPs (py278) 
$ plink --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf \
> --allow-extra-chr \
> --blocks no-pheno-req no-small-max-span \
> --out plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf\
    /ld/blocks_nophenoreq_nosmallmaxspan

PLINK v1.90b2o 64-bit (25 Nov 2014)        https://www.cog-genomics.org/plink2
(C) 2005-2014 Shaun Purcell, Christopher Chang   GNU General Public License v3
Logging to plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf\
    /ld/blocks_nophenoreq_nosmallmaxspan.log.
48251 MB RAM detected; reserving 24125 MB for main workspace.
--vcf: 73k variants complete.

...

73297 variants loaded from .bim file.
53 people (0 males, 0 females, 53 ambiguous) loaded from .fam.
Ambiguous sex IDs written to
plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf\ 
    /ld/blocks_nophenoreq_nosmallmaxspan.nosex
.
Using 1 thread (no multithreaded calculations invoked).
Before main variant filters, 53 founders and 0 nonfounders present.
Calculating allele frequencies... done.
Total genotyping rate is 0.965098.
73297 variants and 53 people pass filters and QC.
Note: No phenotypes present.
--blocks: 8040 haploblocks written to
plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf\
    /ld/blocks_nophenoreq_nosmallmaxspan.blocks
.
Extra block details written to
plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf\
    /ld/blocks_nophenoreq_nosmallmaxspan.blocks.det
.
Longest span: 199.985kb.

~~~~~~~~~~~~~~~~~~~


### Plot PLINK results ###

- cleaned up a few things
- added residual plots following the regplots

## Recover dead positives ##

- need to meet with Kirsten (emailed her to schedule a time)
    - subject: "_Short meeting to talk about the dead positives screen?_"

### Dissections ###

- getting more:
    - tubes
    - PBS
    - Pens

- need to get receipt(s) from Kirsten regarding the dissection dish order
    - emailed with subject: "_did you ever send me the receipt(s) for the stuff you ordered for the dissections over the internet?_"

## Bonizzoni _et al_: Insecticide Resistance ##

- I am SUPER late on this!


------------------------------------------

# 2015-01-07 (Wednesday) #


## Bonizzoni _et al_: Insecticide Resistance ##

__Status:__ COMPLETE

- finished reviewing the main text
- emailed it to her
- will not be going over the legends or figs 


## Meeting with Serap Aksoy ##

__Time:__ 10:00 AM to 11:30AM

### Discussed ###

- how to log Iowa tsetse samples
- student to do much f the logging after a spreadsheet is devised
- location of the other RNA midguts
    - she said she thought they didnt get any but then thought she remembered that Brian tried extracting RNA from at least a few infected midguts with no success.
    - \*\*She said she needs the carcasses of the infected flies too which I did not remember (__I need to bring this up with Gisella bc this is a major reduction of our expected infected material...__).
        - _this doesn't really make sense anyway since i dont think we preserved the bodies for RNA._
- having me send an ad or two for a postdoc position for her lab to my friends

### Action items ###

__Status:__ IN PROGRESS

- `[x]` create simple excel sheet to track Iowa samples
    - `[x]` email sheet to Brian and Serap 
        - subject: _Spreadsheet to record Iowa sample materials_
    - __NOTE:__ sheet is a google sheet named [Iowa_tsetse_material_inventory](https://docs.google.com/spreadsheets/d/1SeoKnRQ0djB1xjyVGQy-NikNFTzQ-wL-hXCwUZAoNqw/edit?usp=sharing)
- `[x]` locate extra RNA midguts in our freezers
    - `[x]` email Aksoy, Brian, Michelle to schedule pickup
        - subject: _Many more midguts and heads for RNA_
- `[ ]` send feelers and ads to friends about postdoc position in her lab
- `[ ]` contact Gisella about Serap wanting the carcasses...



## Meeting with Andrea ##


### Discussed ###

- problem re-running the figure generation R script
- couldn't open the PNG writer bc no X11 on the cluster and `ssh -Y` wasn't working even though it did last time...
- I added some code to the R script to specify `png(type="cairo")
- waiting to hear the outcome
    - _program ran but output was not what was expected: many more graphs than last time_
    - I expect user error


## Recover dead positives ##

- Meeting with Kirstin tomorrow at 1 or 2 PM