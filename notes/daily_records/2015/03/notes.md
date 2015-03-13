---
title: Daily Records
subtitle: Caccone PostDoc
date: March, 2015
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

# 2015-03-04 (Wednesday) #


## Robert's MicroSat Project ##

- add new december excel data [[DEC_2014_survey.xls](file:///home/gus/Dropbox/uganda_data/2014_Dec_new/DEC_2014_survey.xls)] to 
    - `[ ]` [uganda_traps_gps.csv](file:///home/gus/Dropbox/uganda_data/data_repos/field_data/locations/gps/traps/uganda_traps_gps.csv)
    - `[DONE]` [uganda_village_id_map.csv](file:///home/gus/Dropbox/uganda_data/data_repos/field_data/locations/names/uganda_village_id_map.csv)
- `[ ]` re-generate [uganda_villages_gps.csv](file:///home/gus/Dropbox/uganda_data/data_repos/field_data/locations/gps/villages/uganda_villages_gps.csv) with   
[2015-02-03_deduce_village_GPS_coords_from_mean_trap_coords.ipynb](file:///home/gus/Dropbox/repos/git/ipy_notebooks/YALE/maps_stuff/2015-02-03_deduce_village_GPS_coords_from_mean_trap_coords.ipynb)
- `[ ]` create new signed tag for the git repo

### __[ERRORS]__ in collection sheets ###

- [DEC_2014_survey_for_pandas.xlsx](file:///home/gus/Dropbox/uganda_data/2014_Dec_new/DEC_2014_survey_for_pandas.xlsx)

> - Samples for the two villages of Odworo and Ocala were interchanged
> - This means all samples recorded as OD ideally belong to OCA and those recorded as OCA belong to OD



------------------------------------------


# 2015-03-05 (Thursday) #

## _Glossina_ meeting with Kenya folks ##

### My talk topics ###

1. Interest in Uganda

1. Methods
1. Collection protocol
1. Database/sample tracking efforts
1. Collection numbers



------------------------------------------


# 2015-03-06 (Friday) #

## ddrad58 ##

- worked on scaled Beta dist learning of $r^2$ distributions
- calculated and sent back Hardy-Weinberg equilibrium FDRs to AndreaG

## RobertO's MicroSat ##

- must re-build map stuff

### Villages for leg extraction ###

- see project notes: [ddrad58.md](file:///home/gus/Dropbox/repos/git/markdown-docs/notes/projects/ddrad58/ddrad58.md)


------------------------------------------


# 2015-03-11 (Wednesday) #

## ddrad58 ##

- see project notes: [ddrad58.md](file:///home/gus/Dropbox/repos/git/markdown-docs/notes/projects/ddrad58/ddrad58.md)

## RobertO's MicroSat  ##

- see project notes: [roberts_microsats.md](file:///home/gus/Dropbox/repos/git/markdown-docs/notes/projects/roberts_microsats/roberts_microsats.md)


## Pandas import of collection sheets ##

- added explicit date recoding with minor value enforcement/control
    - [g_f_fuscipes_general/2015-02-16_g_f_fuscipes_pandas_import.ipynb](file:///home/gus/Dropbox/repos/git/ipy_notebooks/YALE/g_f_fuscipes_general/2015-02-16_g_f_fuscipes_pandas_import.ipynb)




------------------------------------------

# 2015-03-12 (Thursday) #
## ddrad58 ##
### BEAST ###
    
- `[2015-03-12]` conversation with Aris
- `[wont do]` write up conversation with Aris for GisellaC and get clearance to proceed.
    - meeting with GisellaC and Aris tomorrow at 11
- `[!]` Convert BAMs to NEXSUS
    - waiting to hear back from admins about getting permissions to AndreaG's BAMs
- `[ ]` BEAST configuration
- `[ ]` attempt BEAST run

### Linkage disequilibrium thresholds for SNP-pairs ###

- `[2015-03-12]` set up and yield models
- `[2015-03-12]` take model and return parameters
- `[2015-03-12]` take parameters and df and set value for each SNP-pair's probability ($1-\mathrm{CDF}$)
- `[2015-03-12]` take df and set value for each SNP-pair's BH corrected probability



## RobertO's MicroSat ##

- `[ ]` Get 3 more villages' samples ready for legs and extraction



## Positive recovery ##

- `[ ]` tell GisellaC and KirstinD how many dissections to expect in next weeks
- `[2015-03-12]` start project notebook
    - file at: [positives_recovery.md](file:///home/gus/Dropbox/repos/git/markdown-docs/notes/projects/positives_recovery/positives_recovery.md)



------------------------------------------

# 2015-03-13 (Friday) #

## ddrad58 ##
### BEAST ###

- `[ ]` meeting with GisellaC and Aris at 11
- `[!]` Convert BAMs to NEXSUS
    - `[2015-03-12]` waiting to hear back from admins about getting permissions to AndreaG's BAMs
- `[ ]` BEAST configuration
- `[ ]` attempt BEAST run

### Linkage disequilibrium thresholds for SNP-pairs ###

- `[ ]` see if it make since to deal with the bins that wont __MAP__ correctly
    - `[ ]` examine the MCMCs of a few and see if they converged and are therefore possibly useful to us

## RobertO's MicroSat ##

- `[ ]` Get 3 more villages' samples ready for legs and extraction

## Positive recovery ##

- `[ ]` tell GisellaC and KirstinD how many dissections to expect in next weeks






