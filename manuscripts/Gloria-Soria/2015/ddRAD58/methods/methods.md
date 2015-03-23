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
fontfamily: fourier
bibliography: ../manuscript.bib
csl: ../nature.csl
read: "+simple_tables+table_captions+footnotes+inline_notes+fenced_code_blocks+fenced_code_attributes+fancy_lists+definition_lists+superscript+subscript+tex_math_dollars"
header-includes: 
 - \usepackage{arev}
 - \usepackage[T1]{fontenc}
...


# Functional Annotations #

## Sequences Used ##

___Glossina fuscipes fuscipes:___
All putative peptides annotated for _G. f. fuscipes_ in the GfusI1.1 gene-build were obtained from [VectorBase](link_address) [@Giraldo-Calderon2014]

___Other:___
The sequences used to compare the _G. f. fuscipes_ peptides against well known/annotated sequences were obtained from UNIPROT/SwissProt [@Boeckmann2005]\ (`blastp`) and PFAM [@Finn2014]\ (`hmmscan`) as required by [ARGOT2](link_address) [@Radivojac2013;@Falda2012;@Gillis2013].


## Argot2 Analysis ##

The `blastp` and `hmmscan` results submitted to ARGOT2 were obtained by performing local searches on the _G. f. fuscipes_ peptides against the UNIPROT peptide database (obtained on 2014-09-08) and the hidden Markov models (HMM) of the combined protein-domain sets om the Pfam databases (Pfam-A and Pfam-B: obtained on 2014-09-08), respectively.
Settings used were as dictated by the ARGOT2 site and summarized here.

For `blastp`: 

~~~~~~~~ {.bash}
blastp -outfmt "6 qseqid sseqid evalue " -query GFUSI1_1_PEPTIDES \
    -db UNIPROT_PEPTIDES -out OUTPUT_FILE
~~~~~~~~~~~~~~~~~~~

For `hmmscan`:

~~~~~~~~ {.bash}
hmmscan --tblout OUTPUT_FILE PFAMA_AND_PFAMB_DOMAINS GFUSI1_1_PEPTIDES
~~~~~~~~~~~~~~~~~~~

The `blastp` and `hmmscan` results were split into 10 groups (roughly 2330 peptides per group) and uploaded to ARGOT2 servers for analysis.
The functional annotations were then downloaded and joined back together.

# Linkage Analysis #

## Source of SNPs ##

SNPs were obtained as described earlier in this manuscript.

## Linkage measurements ##
~~~~~~~~ {.bash}
plink --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf \
--allow-extra-chr \
--r gz with-freqs dprime \
--out plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r_none_freqs_dprime
~~~~~~~~~~~~~~~~~~~

Plink version 1.9 [@Chang2015] was used to calculate pairwise linkage disequilibrium (LD) as $r$ for all SNP-pairs located on common supercontigs.
The `--allow-extra-chr` option was required to handle the number of supercontigs.
Unless stated otherwise, all subsequent analysis pertaining to LD used $r^2$.

## LD-based filtering of SNP-pairs ##

The LD values of SNP-pairs were compared after binning SNP-pairs by base pair separation to control for unknown rates of recombination in _G. f. fuscipes_.
Bins length was set at 50 bp with the lower bound inclusive and higher bound exclusive. 
In other words the bins were defined as $[i, i + 49)$ where $i \in \{1,1(50),2(50),3(50) ... n(50)\}$ and $n$ is a positive integer $1 + 3$.

2015-03-23


# Bib #


