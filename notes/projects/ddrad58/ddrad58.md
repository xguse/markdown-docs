---
title: ddrad phase 2 project
subtitle: Caccone PostDoc
date: April, 2015
author: Gus Dunn
documentclass: scrartcl
classoption: letterpaper
toc: 1
graphics: 1
blockquote: 1
tags: daily notes
read: "+simple_tables+table_captions+footnotes+inline_notes+fenced_code_blocks+fenced_code_attributes+fancy_lists+definition_lists+superscript+subscript+tex_math_dollars"
header-includes: 
- \usepackage{fontspec}
- \setmainfont{Linux Libertine O}
...


------------------------------------------

\newpage

# Tasks #

## BEAST ##

### --To DO-- ###

-



### --Completed-- ###

- `[wont do]` Convert BAMs to NEXSUS
    - waiting to hear back from admins about getting permissions to AndreaG's BAMs
- `[wont do]` BEAST configuration
- `[wont do]` attempt BEAST run
- `[2015-03-13]` meeting with GisellaC and Aris 2015-03-13 at 11
- `[2015-03-12]` conversation with Aris
- `[wont do]` write up conversation with Aris for GisellaC and get clearance to proceed.



## Linkage disequilibrium thresholds for SNP-pairs ##

### --To Do-- ###

- `[ ]` 

### --Completed-- ###

- `[2015-03-12]` set up and yield models
- `[2015-03-12]` take model and return parameters
- `[2015-03-12]` take parameters and df and set value for each SNP-pair's probability ($1-\mathrm{CDF}$)
- `[2015-03-12]` take df and set value for each SNP-pair's BH corrected probability


------------------------------------------

<!-- ################################################################## -->
\newpage
<!-- ################################################################## -->


# Contig proximity graph #

## 2015-03-10 (Tuesday) ##

- calculate LD only between __INTER-__ contig SNPS __[Conversation with JoshM]__

### Calculate interchromosomal LD with `vcftools` ###

#### Attempt 1 [FAILED: bug in v0.1.12b] ####


\ \
__- -INPUT- -__

```bash
SNP_DIR="/home2/wd238/data/genomes/glossina_fuscipes/annotations/SNPs"

VCF="${SNP_DIR}/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf"

OUT_PREFIX="${SNP_DIR}/vcftools_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf"

mkdir -p ${SNP_DIR}/vcftools_out/

vcftools --vcf $VCF  --out $OUT_PREFIX --interchrom-geno-r2
```

__- -OUTPUT- -__

```bash
VCFtools - v0.1.12b
(C) Adam Auton and Anthony Marcketta 2009

Parameters as interpreted:
        --vcf /home2/wd238/data/genomes/glossina_fuscipes/annotations/SNPs/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf
        --max-alleles 2
        --min-alleles 2
        --interchrom-geno-r2
        --out /home2/wd238/data/genomes/glossina_fuscipes/annotations/SNPs/vcftools_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf

After filtering, kept 53 out of 53 Individuals
Outputting Interchromosomal Pairwise Genotype LD (bi-allelic only)
Error: Require phased haplotypes for r^2 calculation (use --phased)

```

##### Email to vcftools-help #####

I have recently tried to run the following command

```bash
$ vcftools --vcf $VCF  --out $OUT_PREFIX --interchrom-geno-r2
```

and was answered with the following error/output

```bash
VCFtools - v0.1.12b
(C) Adam Auton and Anthony Marcketta 2009

Parameters as interpreted:

        --vcf /long/path/to/snps.vcf
        --max-alleles 2
        --min-alleles 2
        --interchrom-geno-r2
        --out /long/path/to/out/snps.vcf

After filtering, kept 53 out of 53 Individuals
Outputting Interchromosomal Pairwise Genotype LD (bi-allelic only)
Error: Require phased haplotypes for r^2 calculation (use --phased)

```

I was under the impression from the docs that these options (`--geno-r2` and `--interchrom-geno-r2`) only require phased data for `D` and `D'` metrics:

>`--geno-r2`
>
>Calculates the squared correlation coefficient between genotypes encoded as 0, 1 and 2 to represent the number of non-reference alleles in each individual. This is the same as the LD measure reported by PLINK. The D and D’ statistics are only available for phased genotypes. The output file has the suffix ".geno.ld".


Can anyone spot what is going wrong for me or am I confused?

Thanks,

Gus

##### [RESPONSE] Email to vcftools-help #####

- said its a bug and they will fix

#### Attempt 2 [FAILED: ran out of space] ####
\ \

I installed [vcftools_0.1.12a](file:///home/gus/remote_mounts/louise/scripts/installs/install_vcftools_0.1.12a.sh) and it began without complaint.

__- -INPUT- -__
```bash
SNP_DIR="/home2/wd238/data/genomes/glossina_fuscipes/annotations/SNPs"
VCF="${SNP_DIR}/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf"
OUT_PREFIX="${SNP_DIR}/vcftools_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf"

mkdir -p ${SNP_DIR}/vcftools_out/

module load vcftools/0.1.12a
vcftools --vcf $VCF  --out $OUT_PREFIX --interchrom-geno-r2
```

__- -OUTPUT- -__

- Ran out of disk space.


------------------------------------------


<!-- ################################################################## -->
\newpage
<!-- ################################################################## -->

## 2015-03-11 (Wednesday) ##

### Calculate interchromosomal LD with `vcftools` ###

#### Attempt 3 [?] ####

- attempting to use `fastscratch` to allow for extra space.

\ \
__- -INPUT- -__

```bash
FAST_SCRATCH=/fastscratch/wd238
SNP_DIR="/home2/wd238/data/genomes/glossina_fuscipes/annotations/SNPs"
VCF="${SNP_DIR}/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf"
OUT_PREFIX="${FAST_SCRATCH}/vcftools_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf"

mkdir -p ${FAST_SCRATCH}/vcftools_out/

module load vcftools/0.1.12a
vcftools --vcf $VCF  --out $OUT_PREFIX --interchrom-geno-r2 
```


------------------------------------------

<!-- ################################################################## -->
\newpage 
<!-- ####################################################################################### -->

# Linkage disequilibrium thresholds for SNP-pairs #

## General ##

### 2015-03-10 (Tuesday) [Status] ###


- Decided its best to use the Beta distribution on data binned by distance and scaled thusly:

$$((x_i-0.5) \cdot 0.999) + 0.5)$$

- So far the MAP estimation is coming out VERY close to the MCMC results, so I think I will simply use that since it is __MUCH__ faster.
- `[ ]` does multiple testing correction need to be done?
    - I am pretty sure it does
- p-values will be obtained for each $r^2$ as: $1 - \mathrm{CDF}(x_i)$ 
- see [2015-02-27_overview_of_LD_work_in_Gff.ipynb](http://nbviewer.ipython.org/github/xguse/ipy_notebooks/blob/master/YALE/ddrad58/2015-02-27_overview_of_LD_work_in_Gff.ipynb) for extra info.

## Thresholds by binning: notebook ##

- notebook file: [2015-03-12_LD_thresholds_via_binning.ipynb](file:///home/gus/Dropbox/repos/git/ipy_notebooks/YALE/ddrad58/2015-03-12_LD_thresholds_via_binning.ipynb)
- script version: [2015-03-12_LD_thresholds_via_binning.py](file:///home/gus/Dropbox/repos/git/ipy_notebooks/YALE/ddrad58/2015-03-12_LD_thresholds_via_binning.py)

### 2015-03-13 (Friday) ###

- got the whole data set to run
    - those bins which fail MAP go on to run MCMC
    - had to re-write a bit to get the model object to save the MCMC runner so that we can look at the traces to asses convergence
- running as script in IPython to view.
- SUCCESS.  Finally.
- saved resulting table in pickle: [ddrad58/ld_thresholds/post_MAP_calc.plk](file:///home/gus/Documents/YalePostDoc/project_stuff/g_f_fucipes_uganda/ddrad58/ld_thresholds/post_MAP_calc.plk)
- use above to avoid re calculating the MAPs that take HOURS.
- started new ipython notebook file for results analysis: [2015-03-13_LD_thresholds_via_binning_RESULTS.ipynb](file:///home/gus/Dropbox/repos/git/ipy_notebooks/YALE/ddrad58/2015-03-13_LD_thresholds_via_binning_RESULTS.ipynb)


------------------------------------------

<!-- ################################################################## -->
\newpage
<!-- ################################################################## -->



## Investigate LD bin-data pattern ##

![Distance vs $r^2$ overall ](/home/gus/Documents/YalePostDoc/project_stuff/g_f_fucipes_uganda/ddrad58/manuscript/figures/ld/distance_VS_r2_all.pdf)

### Bin-data membership quantity ###

__Is the reason for the bizarre data shape due to loss of signal to noise as shorter contigs are eliminated from data pool?__

![Distance vs avg $r^2$, contigs and $q$ for bins 150-10000 ](/home/gus/Documents/YalePostDoc/project_stuff/g_f_fucipes_uganda/ddrad58/manuscript/figures/ld/distance_VS_avgR2_spperbin_contigsperbin_q_b150-to-b10000.pdf)

![Distance vs avg $r^2$, contigs and $q$ for bins 150-20000 ](/home/gus/Documents/YalePostDoc/project_stuff/g_f_fucipes_uganda/ddrad58/manuscript/figures/ld/distance_VS_avgR2_spperbin_contigsperbin_q_b150-to-b20000.pdf)

### Bin-data pattern of individual populations  ###

__Is the reason for the bizarre data shape due to strange behavior in a specific population?__

#### 2015-04-15 (Wednesday) ####

- installing vcftools_0.1.12b on `jupiter` bc `louise` is down for work.

#### 2015-04-16 (Thursday) ####

__[VCF filtering]:__

```shell

IN_SNPS=/home/gus/remote_mounts/louise/data/genomes/glossina_fuscipes/annotations/SNPs/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf

vcftools --vcf  --keep $PROJECTSTUFF/g_f_fucipes_uganda/ddrad58/SNP_data/vcf/OT_indvs.txt --out $PROJECTSTUFF/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05._indiv --recode --recode-INFO-all 

```
#### 2015-04-22 (Wednesday) ####

__[VCF filtering]:__

```shell
\#!/bin/zsh 
\# /home2/wd238/data/projects/ddrad58/population_VCFs/split_pop_vcf.sh

INDIVS=$HOME/data/genomes/glossina_fuscipes/annotations/SNPs/vcftools_out/ddrad58_populations/individuals
GFFANNOTATIONS=$HOME/data/genomes/glossina_fuscipes/annotations

IN_SNPS=$GFFANNOTATIONS/SNPs/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf

OT_LIST=$INDIVS/OT_indvs.txt
MS_LIST=$INDIVS/MS_indvs.txt
NB_LIST=$INDIVS/NB_indvs.txt
KG_LIST=$INDIVS/KG_indvs.txt

OT_PREFIX=$INDIVS/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.OT_indiv
MS_PREFIX=$INDIVS/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.MS_indiv
NB_PREFIX=$INDIVS/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.NB_indiv
KG_PREFIX=$INDIVS/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.KG_indiv

vcftools --vcf $IN_SNPS --keep $INDIVS/OT_indvs.txt --out $OT_PREFIX --recode --recode-INFO-all
vcftools --vcf $IN_SNPS --keep $INDIVS/MS_indvs.txt --out $MS_PREFIX --recode --recode-INFO-all
vcftools --vcf $IN_SNPS --keep $INDIVS/NB_indvs.txt --out $NB_PREFIX --recode --recode-INFO-all
vcftools --vcf $IN_SNPS --keep $INDIVS/KG_indvs.txt --out $KG_PREFIX --recode --recode-INFO-all
```

__[VCFtools LD calculation]:__

```shell
qI8

md load parallel
md load vcftools/0.1.12a


parallel vcftools --vcf {} --out {.} --geno-r2 ::: $(cat vcf_manifest.txt)

```

- completed without error reported. (2015-04-23)

#### 2015-04-23 (Thursday) ####

- rewrote the processing and save to pickle code as [vcftools_table_to_pandas_pickle.process_my_ld](file:///home/gus/src/repos/git/gloria_soria_ddRAD_2015/src/gs_ddRAD2015/scripts/vcftools_table_to_pandas_pickle.py)
- still debugging

```shell
LD_PATH=$HOME/remote_mounts/louise/data/genomes/glossina_fuscipes/annotations/SNPs/vcftools_out/ddrad58_populations/individuals/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.KG_indiv.geno.ld
OUT_PATH=$HOME/remote_mounts/louise/data/genomes/glossina_fuscipes/annotations/SNPs/vcftools_out/ddrad58_populations/individuals/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.KG_indiv.geno.ld.pkl

process_my_ld --ld-prog vcftools --distance-bin 50 $LD_PATH $OUT_PATH
```


# Dating the North/South population split #

## Converting the BAMS to NEXSUS for BEAST ##

- using PGDSpider2 to convert to NEXUS
- BAM location: `/scratch/ag674/sample_mappedSC`
- SPID file: [bam_to_nex_for_BEAST.spid](file:///home/gus/remote_mounts/louise/data/projects/ddrad58/PGDSpider_files/bam_to_nex_for_BEAST/bam_to_nex_for_BEAST.spid)
- BAMS to use:
    - `find /scratch/ag674/sample_mappedSC -name \* | grep -P "\d\.sorted" > $HOME/data/projects/ddrad58/PGDSpider_files/bam_to_nex_for_BEAST/bam_to_nex_for_BEAST.bam_list.txt`
    - [bam_to_nex_for_BEAST.bam_list.txt](file:///home/gus/remote_mounts/louise/data/projects/ddrad58/PGDSpider_files/bam_to_nex_for_BEAST/bam_to_nex_for_BEAST.bam_list.txt)
- ref for bam: [Glossina-fuscipes-IAEA_SCAFFOLDS_GfusI1.fa](file:///home/gus/remote_mounts/louise/data/genomes/glossina_fuscipes/assemblies/GfusI1/Glossina-fuscipes-IAEA_SCAFFOLDS_GfusI1.fa)

### 2015-03-11 (Wednesday) ###

- stymied by permissions issues with the bams. 
- see tomorrow

### 2015-03-12 (Thursday) ###

#### Attempt 1 [FAILED: write permissions] ####

```bash
module load PGDSpider/2.0.8.0 samtools-bcftools-htslib/1.0

java -Xmx2048m -Xms512m -jar /home2/wd238/.local/easybuild/software/PGDSpider/2.0.8.0/PGDSpider2-cli.jar -inputfile /fastscratch/wd238/beast_run/BAMs/KG_10030.sorted.bam -inputformat BAM -outputfile /fastscratch/wd238/beast_run/KG_10030.sorted.bam.nex -outputformat NEXSUS -spid $HOME/data/projects/ddrad58/PGDSpider_files/bam_to_nex_for_BEAST/bam_to_nex_for_BEAST.spid

```

\ \

__NOTES:__

- `PGDSpider` seems to write a bunch of temporary files in the same dir as the inputfile.
- this breaks because I only have READ access to the data dir
- proceeding with copying the BAMs to a place I have write access to and trying again


#### Attempt 2 [FAILED: memory limit] ####

```bash
$ java -Xmx2048m -Xms512m -jar /home2/wd238/.local/easybuild/software/PGDSpider/2.0.8.0/PGDSpider2-cli.jar -inputfile /fastscratch/wd238/beast_run/BAMs/KG_10030.sorted.bam -inputformat BAM -outputfile /fastscratch/wd238/beast_run/KG_10030.sorted.bam.nex -outputformat NEXSUS -spid $HOME/data/projects/ddrad58/PGDSpider_files/bam_to_nex_for_BEAST/bam_to_nex_for_BEAST.spid

-[  output   ]-
INFO  16:27:47 - load PGDSpider configuration from: /home2/wd238/.local/easybuild/software/PGDSpider/2.0.8.0/spider.conf.xml
initialize convert process...
read input file...
INFO  16:28:04 - Run samtools/bcftools...
INFO  16:28:33 - [bam_sort_core] merging from 3 files...
ERROR 16:30:24 - not enough memory. To increase the allowed memory see help.
read input file done.
write output file...
write output file done.
```

\ \

__NOTES:__

- `PGDSpider` ran out of mem. 
- I am going to bump up the mem and try again.


#### Attempt 3 [FAILED: reference file issue] ####

```bash
$ java -Xmx16384m -Xms16000m -jar /home2/wd238/.local/easybuild/software/PGDSpider/2.0.8.0/PGDSpider2-cli.jar -inputfile /fastscratch/wd238/beast_run/BAMs/KG_10030.sorted.bam -inputformat BAM -outputfile /fastscratch/wd238/beast_run/KG_10030.sorted.bam.nex -outputformat NEXSUS -spid $HOME/data/projects/ddrad58/PGDSpider_files/bam_to_nex_for_BEAST/bam_to_nex_for_BEAST.spid

-[  output   ]-
INFO  17:23:52 - load PGDSpider configuration from: /home2/wd238/.local/easybuild/software/PGDSpider/2.0.8.0/spider.conf.xml
initialize convert process...
read input file...
INFO  17:24:16 - Run samtools/bcftools...
INFO  17:24:51 - [bam_sort_core] merging from 3 files...
INFO  17:26:38 - ...done
ERROR 17:29:37 - reference file does not contain *!
read input file done.
write output file...
write output file done.

```

\ \

__NOTES:__

- `PGDSpider` ran out of mem. 
- I am going to bump up the mem and try again.


### 2015-03-13 (Friday) ###

- ABANDONING THIS AND LETTING ARIS TRY TO START FROM SCRATCH via PYRAD.
- thank GAWD.


























# Meeting  #


- Introduce Joshua and suggest a meeting



