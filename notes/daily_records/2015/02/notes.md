---
title: Daily Records
subtitle: Caccone PostDoc
date: February, 2015
author: Gus Dunn
documentclass: scrartcl
classoption: letterpaper
toc: 1
graphics: 1
blockquote: 1
tags: daily notes
header-includes: 
 - \usepackage{bbding}
 - \usepackage[T1]{fontenc}
 - \usepackage{lxfonts}
read: "+simple_tables+table_captions+footnotes+inline_notes+fenced_code_blocks+fenced_code_attributes+fancy_lists+definition_lists+superscript+subscript+tex_math_dollars"
...




------------------------------------------

# 2015-02-01 (Sunday) #

## Updating maps: current trap locations ##

### `spartan` dev: GPS stuff ###

- writing autovivification version of `GPSCoordTree._grow_branch`.



------------------------------------------

# 2015-02-02 (Monday) #

## Updating maps: current trap locations ##

### `spartan` dev: GPS stuff ###

- testing ([test_utils_maps_gps.py](file:///home/gus/Dropbox/repos/git/spartan/src/spartan/tests/test_utils_maps_gps.py)):
    - `[x]` `GPSCoordTree._grow_branch`
    - `[x]` `GPSCoordTree._get_subtree`
    - `[x]` `GPSCoordTree.mean`

## Creating Uganda Data Repo ##

- __local location:__ 

    [/home/gus/Dropbox/uganda_data/data_repos/field_data](file:///home/gus/Dropbox/uganda_data/data_repos/field_data)
- __github address:__ [https://github.com/CacconeLabYale/field_data.git](https://github.com/CacconeLabYale/field_data.git)





------------------------------------------

# 2015-02-03 (Tuesday) #

## Updating maps: current trap locations ##

- established comprehensive lists of village-ID-map and trap GPS locations for Uganda:
    - __village-ID-map:__
        
        [field_data/locations/names/uganda_village_id_map.csv](file:///home/gus/Dropbox/uganda_data/data_repos/field_data/locations/names/uganda_village_id_map.csv)
    - __trap GPS coords:__

        [field_data/locations/gps/traps/uganda_traps_gps.csv](file:///home/gus/Dropbox/uganda_data/data_repos/field_data/locations/gps/traps/uganda_traps_gps.csv)


------------------------------------------

# 2015-02-04 (Wednesday) #

## General ToDo ##

- `[x]` email to confirm HR got my letter
- `[x]` meet with Gisella and Andrea [1130]
    - `[X]` write up notes from meeting: [gisella_andrea_2015-02-04.pdf](file:///home/gus/Dropbox/repos/git/markdown-docs/notes/meetings/gisella_andrea_2015-02-04/gisella_andrea_2015-02-04.pdf)
- `[x]` Talk to Ben E about the MAD idea.
- `[x]` create git repo for this paper
- `[ ]` begin development of the MAD idea
- `[X]` install LDna and R-studio
- `[X]` Located space to move the EPH _G. pallidipes_ samples here to ESC with Rob




## ddRAD stuff ##

### LD: detect 'outlier' SNP-pairs ###

- __I propose this method:__
    1. for each distance group: collect $r^2$ from $\pm \sim5$ bp distance window
        a. across genome
        b. across scaffold
    2. calculate modified z-score (based on _median absolute deviation_ rather than standard deviation: __MAD is more robust than SD for HTS-type data__)
    3. flag any SNP-pair with $z \geq 3.5$
    4. _possibly randomize data and calculate FDR to evaluate performance._
        a. perhaps vary the window from step 1 to use FDR to chose window that minimizes FDR.
- __Ben E's thoughts:__
    - basically: this is probably a waste of time and energy
        - other more sophisticated methods have already been applied to this data with not much significance detected
        - why do we expect this work to yield better/more results?
- __Gisella's thoughts:__
    - still should do it bc we will need it when we have more data

### Install LDna ###

- github page: [github.com/petrikemppainen/LDna](https://github.com/petrikemppainen/LDna)
- paper reference: [http://onlinelibrary.wiley.com/doi/10.1111/1755-0998.12369/abstract](http://onlinelibrary.wiley.com/doi/10.1111/1755-0998.12369/abstract)
- installed `devtools` with `RStudio` gui: __[successful]__
- installed `LDna` with `devtools`:  __[successful]__

    ~~~~~~~~ {.R}
    devtools::install_github("petrikemppainen/LDna")
    ~~~~~~~~~~~~~~~~~~~
    - documentation: [LDna/html/00Index.html](file:///home/gus/R/x86_64-unknown-linux-gnu-library/3.1/LDna/html/00Index.html)

### LDna notes ###

- operates on:  
    
    >Lower diagonal matrix of pairwise LD values, $r^2$ is strongly recommended
- the code below should generate what I want (__I think__):
    
~~~~~~~~ {.bash}
plink --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf \
--allow-extra-chr \
--r2 bin  \
--out plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r2_bin
~~~~~~~~~~~~~~~~~~~


### PLINK run for LDna ###

- ran the command below:

~~~~~~~~ 
wd238 at compute-23-2 in ~GENOMES/glossina_fuscipes/annotations/SNPs (py278)
$ plink --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf \
> --allow-extra-chr \
> --r2 bin  \
> --out plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r2_bin

~~~~~~~~~~~~~~~~~~~

- waiting for it to finish: __[failed]__

### Louise Scratch Request Email ###

>__netid:__ wd238
>__group:__ caccone
>__anticipated usage:__ 
>
>- ~ 100G
>- < 100 files 
>__purpose of usage:__ 
>
>- running `plink` _all_v_all_ linkage disequilibrium calculations on ~40K SNPs
>- current attempt (documented below) gave a write failure which I think may be bc of some rather large tmp files generated during the process?
>- Does bumping up against our space quota have hard/immediate consequences like that?
>
>
>__error log:__
>
>```
>wd238 at compute-23-2 in ~GENOMES/glossina_fuscipes/annotations/SNPs (py278)
>$ plink --vcf tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf \
>> --allow-extra-chr \
>> --r2 bin  \
>> --out plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r2_bin
>PLINK v1.90b2o 64-bit (25 Nov 2014)        https://www.cog-genomics.org/plink2
>(C) 2005-2014 Shaun Purcell, Christopher Chang   GNU General Public License v3
>Logging to plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r2_bin.log.
>516842 MB RAM detected; reserving 258421 MB for main workspace.
>--vcf: 73k variants complete.
>plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r2_bin-temporary.bed
>+
>plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r2_bin-temporary.bim
>+
>plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r2_bin-temporary.fam
>written.
>73297 variants loaded from .bim file.
>53 people (0 males, 0 females, 53 ambiguous) loaded from .fam.
>Ambiguous sex IDs written to
>plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r2_bin.nosex
>.
>Using up to 63 threads (change this with --threads).
>Before main variant filters, 53 founders and 0 nonfounders present.
>Calculating allele frequencies... done.
>Total genotyping rate is 0.965098.
>73297 variants and 53 people pass filters and QC.
>Note: No phenotypes present.
>--r2 square bin to
>plink_out/tsetseFINAL_14Oct2014_f2_53.recode.renamed_scaffolds.maf0_05.vcf/ld/r2_bin.ld.bin
>... done.
>
>Error: File write failure.
>
>```



### Github repo for this paper ###

- github page:  
    [https://github.com/CacconeLabYale/gloria_soria_ddRAD_2015.git](https://github.com/CacconeLabYale/gloria_soria_ddRAD_2015.git)





------------------------------------------

# 2015-02-05 (Thursday) #

## Mariangela `blacktie` install ##


- turns out i did NOT send Mariangela install instructions for the development branch
- wrote quick install script for her to use and sent it

## MAD idea ##

1. for each group of SNPs $x$ bp apart: collect $r^2$ from $\pm \sim5$ bp distance window around $x$:  
    a. across genome
    b. across scaffold
2. calculate modified z-score (based on _median absolute deviation_ rather than standard deviation: __MAD is more robust than SD for HTS-type data__)
3. flag any SNP-pair with $z \geq 3.5$
4. possibly randomize data and calculate FDR to evaluate performance.
    a. perhaps vary the window-size from step 1 to use FDR to chose window-size that minimizes FDR.

### Development ###

- ipython notebook: [ddrad58/2015-02-05_MAD_idea.ipynb](file:///home/gus/Dropbox/common/ipy_notebooks/YALE/ddrad58/2015-02-05_MAD_idea.ipynb)

## _G. pallidipes_ ##

- Rob brought most to ESC this morning
- doesn't expect to need my truck for the rest



------------------------------------------

# 2015-02-06 (Friday) #

## MAD idea ##

### Development ###

- LOTS of progress at ipython notebook: [ddrad58/2015-02-05_MAD_idea.ipynb](file:///home/gus/Dropbox/common/ipy_notebooks/YALE/ddrad58/2015-02-05_MAD_idea.ipynb)

- See notes about plotting median and MAD with bootstrapped CIs near the bottom of above (commit dd7fe5da5733406edeaab6ce3c25b523b94552f2)



# Carl Zimmer Workshop 






