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



------------------------------------------

# 2015-02-09 (Monday) #

__Goals:__

- `[x]` Zimmer Workshop
- `[x]` Start Professional Development notebook
- `[x]` Find out how to process health reimbursement
    - `[ ]` Get them ready for mailing
        - `[x]` form
        - `[ ]` receipts
    - `[X]` Assemble list of information I need from Sarah and send it to her
- `[ ]` Progress on MAD idea
- `[ ]` Generate strategy for the week
- `[ ]` Sketch out abstract for Keystone? meeting
- `[ ]` find out if there is data available on tsetse control by area in Uganda
    - chemicals sold
    - etc


## Health reimbursement  ##

- [http://yalehealth.yale.edu/claims](http://yalehealth.yale.edu/claims)
- Supplemental Claim form: [http://yalehealth.yale.edu/sites/default/files/supplemental_claims_form.pdf](http://yalehealth.yale.edu/sites/default/files/supplemental_claims_form.pdf)
- pharmacy claim form: [http://yalehealth.yale.edu/sites/default/files/pharmacy_claim_form_restat_catamaran.pdf](http://yalehealth.yale.edu/sites/default/files/pharmacy_claim_form_restat_catamaran.pdf)

### Instructions for pharmacy process ###

- from website above

>Include copies of prescription receipts showing the following information:
>
>- Pharmacy Name, Address & Phone Number 
>- Patient Name 
>- Prescription Number 
>- Prescription Fill Date 
>- Drug Name, Strength and NDC Code
>- Drug Quantity & Days supply 
>- Drug Cost 
>- Amount Paid 
>
>Please mail the Prescription Drug Claim Form and receipts to:
>
>Restat  
>Patient Reimbursement  
>11900 W. Lake Park Drive  
>Milwaukee, WI 53224  
>
>Claims are honored for one year from the date of service. If you haven't received a response to a claim within 60 days of filing, contact the Claims Department. You may call sooner to inquire if the claim has been received and is in process.



------------------------------------------

# 2015-02-10 (Tuesday) #

__Goals:__


- `[ ]` Get pharm claim ready for mailing
    - `[x]` form
    - `[ ]` receipts
- `[ ]` Progress on MAD idea
- `[ ]` Generate strategy for the week
- `[ ]` Sketch out abstract for Keystone? meeting
- `[ ]` find out if there is data available on tsetse control by area in Uganda
    - chemicals sold
    - etc
- `[ ]` figure out how to download zimmer files


## Health reimbursement  ##

- printed form

## Met with Postdoc applicant (Christina) ##

- had lunch 

------------------------------------------

# 2015-02-12 (Thursday) #

## Health reimbursement  ##

- Need Catherine's member ID

## MAD idea ##

### Development ###

- _yesterday:_
    - bootstrap confidence intervals are functional
    - modified z-score is functional
    - used ggplot to provide nice figure showing rough progression of z-scored $r^2$ through distance between snps


------------------------------------------

# 2015-02-13 (Friday) #

## _G. pallidipes_ Sample catalog ##


### Summary table ###

- data types:
    - location
    - symbols when present (_I assume you mean location symbol?_)
    - number of individuals
    - date range
    - is tissue?
    - is extraction?
    - analysis status
- will be done in `python` for increased flexibility by __[Gus]__

- notebook file: [2015-02-12_sample_catalog_summary.ipynb](file:///home/gus/Dropbox/common/ipy_notebooks/YALE/pallidipes_kenya/2015-02-12_sample_catalog_summary.ipynb)

- Showed output to Gisella and she signed off on it after asking whether I could accommodate GEO COORDS when we get them.

- __STATUS:__ __[completed]__

### Primers etc ###

- RobH reports that he and KirstinD found many primers etc that were either designed for _G. pallidipes_ or shown to work with it in the past.
- testing on the primers will begin next week.

### Leg extractions ###

- Rob did Xymogen extractions on 5 legs
- NanoDrop indicates absorption at 260 but peaks look weird
    - probably bc the kit leaves EVERYTHING still in solution
    - `[ ]` RobH  will check with KirstinD about her extraction traces on _G. f. fuscipes_ legs



## MAD idea ##

### Development ###

- __[completed]:__ functions to
    - update df with `distance_bin` and `mad_z`
    - plot mad_z by bins
- __[to do]:__
    - implement printing/saving snp-pairs that pass the z-filter 



------------------------------------------

# 2015-02-14 (Saturday) #

## MAD idea ##

### Development ###

- implement printing/saving snp-pairs that pass the z-filter 



------------------------------------------

# 2015-02-16 (Monday) #

## _G. f. fuscipes_: infection summaries ##

- ipython to get pivot table for infected flies
    - file: [2015-02-16_g_f_fuscipes_pandas_import.ipynb](file:///home/gus/Dropbox/common/ipy_notebooks/YALE/g_f_fuscipes_general/2015-02-16_g_f_fuscipes_pandas_import.ipynb)
        - file of dumped pandas table of collection records for 2014 in hdf5 format: 
- add PCR detected fly statuses to main DB @soon


## _G. pallidipes_: MicroSat extraction pilot ##

- RobH spoke with KirstinD about strange NanoDrop traces:
    - KirstinD: hers looked the same, just used 260/280 values as presented
    - likely explanation is that the extraction kit is EXTREMELY dirty by design so the spec peaks are shifted around
- RobH is beginning PCRs with ITS primers (same that KirstinD is using on the _G. f. fuscipes_) today.
- RobH is researching location names on the SerapA tubes (n ~ 6) bc GisellaC is not convinced the sheet SerapA included makes since.
    - RobH will google first
    - GusD will get GIS admin layers to search if google fails


