---
title: Daily Records
subtitle: Caccone PostDoc
date: February, 2015
author: Gus Dunn
documentclass: scrartcl
classoption: letterpaper
toc: 1
graphics: 1
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
    - `[ ]` write up notes from meeting
- `[x]` Talk to Ben E about the MAD idea.
- `[x]` create git repo for this paper
- `[ ]` begin development of the MAD idea
- `[ ]` install LDna and R-studio
- `[ ]` Located space to move the EPH _G. pallidipes_ samples here to ESC with Rob




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

### Github repo for this paper ###

- github page:  
    [https://github.com/CacconeLabYale/gloria_soria_ddRAD_2015.git](https://github.com/CacconeLabYale/gloria_soria_ddRAD_2015.git)

