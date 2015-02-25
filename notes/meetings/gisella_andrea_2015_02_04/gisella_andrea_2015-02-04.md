---
title: Status of dead positives recovery
subtitle: Meeting notes
author: Gus, Gisella, Andrea
date: 2015-02-04 (Wednesday)
documentclass: scrartcl
classoption: letterpaper
geometry: margin=1in
toc: 1
graphics: 1
tags: [meeting, ]
header-includes: 
 - \usepackage[T1]{fontenc}
 - \usepackage{lxfonts}
read: "+simple_tables+table_captions+footnotes+inline_notes+fenced_code_blocks+fenced_code_attributes+fancy_lists+definition_lists+superscript+subscript+tex_math_dollars"
...

# Overview of Discussed #

- Andrea's write up of current results
    - _need to be collated into one doc_
- Status of LD analysis and how to choose cut-off
    - results of discussion with Mark
    - success in generating expected behavior of mean LD behavior vs distance
    - Gus's proposed idea to identify "outlier" snp pairs (_see section below_)

- First figure should have a map of population locations as a panel
- Structure of paper _(__mostly__ unchanged since last meeting)_
- plans for future

# Current structure of paper #

_\ __mostly__ unchanged since last meeting_:  

1. Development of the base SNP set
1. Linkage Analysis
    a. __(new)__ linkage-based grouping of contigs by physical proximity 
1. Functional Annotation of filtered SNPs
1. Discussion
    - establish the ability to do this scale of work in _G. f. fuscipes_
    - limits of the dataset as it now stands
    - Never-the-less, hypotheses can be formulated and here they are...
    - __(new)__ provides more information pertaining to the physical proximity of the supercontigs 


# Gus's proposal to identify LD "outlier" snp-pairs #


1. for each group of SNPs $x$ bp apart: collect $r^2$ from $\pm \sim5$ bp distance window around $x$:  
    a. across genome
    b. across scaffold
2. calculate modified z-score (based on _median absolute deviation_ rather than standard deviation: __MAD is more robust than SD for HTS-type data__)
3. flag any SNP-pair with $z \geq 3.5$
4. possibly randomize data and calculate FDR to evaluate performance.
    a. perhaps vary the window-size from step 1 to use FDR to chose window-size that minimizes FDR.





# Current/future plans #

__Gisella:__

- `[X]` email Washington group about methods of Seq prep and analysis
- `[X]` email Aksoy group about linkage status of _G. m. morsitans_

__Gus and Andrea:__

- `[ ]` add methods in "final" style to growing document
- `[ ]` place document in shared location

__Gus:__

- `[ ]` add LD methods and results to document
- `[ ]` generate population-location map with zoom out to all Uganda
- `[-waiting-]` upon decision of which near-by genes are "interesting" send summary of info known about them to Aksoy group for ideas.