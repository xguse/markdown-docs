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
...


# Functional Annotations #

## Sequences Used ##

### _Glossina fuscipes fuscipes_ ###

All putative peptides annotated for _G. f. fuscipes_ in the GfusI1.1 gene-build were obtained from [VectorBase](link_address) __{{CITE_ME}}__.

### Other ###

The sequences used to compare the _G. f. fuscipes_ peptides against well known/annotated sequences were obtained from UNIPROT __{{CITE_ME}}__ (`blastp`) and PFAM __{{CITE_ME}}__ (`hmmscan`) as required by [ARGOT2](link_address) __{{CITE_ME}}__.


## Argot2 ##

The `blastp` and `hmmscan` results submitted to ARGOT2 were obtained by performing local searches on the _G. f. fuscipes_ peptides against the UNIPROT peptide database (obtained on 2014-09-08) and a protein-domain database consisting of the hidden Markov models (HMM)combined from the Pfam-A and Pfam-B model databases (obtained on 2014-09-08), respectively.
Settings used were as dictated by the ARGOT2 site and summarized here.

For `blastp`: 

~~~~~~~~ {.bash}

blastp -outfmt "6 qseqid sseqid evalue " -query GFUSI1_1_PEPTIDES -db UNIPROT_PEPTIDES -out OUTPUT_FILE

~~~~~~~~~~~~~~~~~~~

For `hmmscan`

~~~~~~~~ {.bash}

hmmscan --tblout OUTPUT_FILE  $your_sequences

~~~~~~~~~~~~~~~~~~~

# Linkage Analysis #


# Bib #


