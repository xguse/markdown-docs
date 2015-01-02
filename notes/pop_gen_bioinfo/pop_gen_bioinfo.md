---
title: Notes on Bioinformatics for Population Genetics
author: Gus Dunn
date: 2014-12-30
documentclass: scrartcl
classoption: letterpaper
geometry: margin=1in
toc: 1
graphics: 1
tags: [bioinformatics, popgen, notes]
fontfamily: fourier
read: "+simple_tables+table_captions+footnotes+inline_notes+fenced_code_blocks+fenced_code_attributes+fancy_lists+definition_lists+superscript+subscript+tex_math_dollars"
...


# Imputation #

- Nature Reviews Genetics 11, 499-511 (July 2010): [Box 1 | How genotype imputation works](http://www.nature.com/nrg/journal/v11/n7/box/nrg2796_BX1.html)



# VCF phased vs non-phased #

```tags
tags = [VCF, phased, ]
```

## Web snippets ##

- as far as I know, the main reason to use allele phasing information is to increase the correctness of the haplotypes and haplotype blocks inferred from them [\[source\]](https://www.biostars.org/p/5298/).

- Phased data are ordered along one chromosome and so from these data you know the haplotype. Unphased data are simply the genotypes without regard to which one of the pair of chromosomes holds that allele. [\[source\]](https://www.biostars.org/p/7846/)

- The ability to distinguish which alleles belong to which chromosome is important when considering how genes are inherited. Generally, a parent passes one of the two copies of each chromosome on to their offspring. While the two chromosomes might both contribute genetic information via a process called recombination, the genes received by a child are typically “linked” and inherited together since they are located on the same chromosome.

    To determine which genes of yours are linked together (and therefore likely to be inherited together by your child), it is first necessary to figure out which alleles (indicated by the variant SNPs) exist together on the same chromosome. This process has been termed “phasing” in the bioinformatics world. [\[source\]](link_addresshttp://www.chromosomechronicles.com/2009/09/08/phasing-determining-which-snps-are-inherited-together/)

- [http://blogs.discovermagazine.com/gnxp/2007/01/basic-concepts-linkage-disequilibrium/#.VKK7BAMAQ](http://blogs.discovermagazine.com/gnxp/2007/01/basic-concepts-linkage-disequilibrium/#.VKK7BAMAQ)

# Glossary #

imputation

~   in genetics, imputation refers to the statistical inference of unobserved genotypes. _It is achieved by using known haplotypes in a population_, for instance from the HapMap or the 1000 Genomes Project in humans, thereby allowing to test initially-untyped genetic variants for association with a trait of interest. Genotype imputation hence helps tremendously in narrowing-down the location of probably causal variants in genome-wide association studies. [Wikipedia](http://en.wikipedia.org/wiki/Imputation_(genetics))   


haplotype

~   a collection of specific alleles (particular DNA sequences) in a cluster of tightly-linked genes on a chromosome that are likely to be inherited together. _Put in simple words, haplotype is the group of genes that a progeny inherits from one parent._ [Wikipedia](link_addresshttp://en.wikipedia.org/wiki/Haplotype)

~   A second meaning of the term is a set of single-nucleotide polymorphisms (SNPs) on a single chromatid of a chromosome pair that are associated statistically. It is thought that these associations, and the identification of a few alleles of a haplotype sequence, can unambiguously identify all other polymorphic sites in its region. [Wikipedia](link_addresshttp://en.wikipedia.org/wiki/Haplotype)

~   haplotype is a contraction for haploid genotypes. [Wikipedia](link_addresshttp://en.wikipedia.org/wiki/Haplotype)

linkage disequilibrium

~   the occurrence of some combinations of alleles or genetic markers in a population more often or less often than would be expected from a random formation of haplotypes from alleles based on their frequencies. It is a second order phenomenon derived from linkage, which is the presence of two or more loci on a chromosome with limited recombination between them. The amount of linkage disequilibrium depends on the difference between observed allelic frequencies and those expected from a homogenous, randomly distributed model. Populations where combinations of alleles or genotypes can be found in the expected proportions are said to be in linkage equilibrium. [Wikipedia](http://en.wikipedia.org/wiki/Linkage_disequilibrium)



