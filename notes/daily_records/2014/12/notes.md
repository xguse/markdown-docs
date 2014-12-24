---
title: December, 2014
author: Gus Dunn
documentclass: scrartcl
classoption: letterpaper
toc: 1
graphics: 1
tags: daily notes, ddRAD, argot2, 
fontfamily: concmath
read: "+simple_tables+table_captions+footnotes+inline_notes+fenced_code_blocks+fenced_code_attributes+fancy_lists+definition_lists+superscript+subscript+tex_math_dollars"
...


# 2014-12-19 #

## Argot2 batch size reduction: ##
```tags
tags = [argot2, ddRAD58, python, spartan]
```

- dumping the whole proteome on the online server seems to have broken it.
- I believe I will need to split the input up into around 3000 proteins per submission
- this will need some python code (maybe added to `spartan`?)

### Problems: ###
```tags
tags = [python, pip, virtualenvwrapper, py279, admin]
```

- cant run ipython notebook bc of py279 from py278 issues.
- must reinstall most/all python dependencies. 

##########################################

# 2014-12-21 #

## Argot2 batch size reduction: ##

- see 2014-12-19
- finished updating `py279` `python` requirements
- `ipython` seems to work again

### Completed: ###

- writing filter functions for `blast` and `hmmer` outputs:
	- `spartan/src/spartan/utils/blast/output.py`: 
		- `filter_for_argot(path, protein_names)`
	- `spartan/src/spartan/utils/hmmer/output.py`: 
		- `filter_for_argot(path, protein_names)`
- created `sublime text 3` snippet to make new `ipython notebook` file with meta info and template.
- wrote and tested split up logic:
	- `spartan/src/spartan/utils/misc.py`:
		- `split_stream(stream, divisor)`


### Problems: ###

- coding the split up logic

## Working on: ##

- split `blastp` and `hmmer` outputs by protein (~3000 per group)

##########################################

# 2014-12-22 (Monday) #

## Argot2 batch size reduction: ##

- see 2014-12-21
- finished splitting
- files were zipped
- file pairs were submitted to Argot2

### Files: ###

```
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.0.hmmscan.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.1.hmmscan.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.2.hmmscan.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.3.hmmscan.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.4.hmmscan.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.5.hmmscan.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.6.hmmscan.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.7.hmmscan.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.8.hmmscan.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.9.hmmscan.zip

    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.union.0.blastp.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.union.1.blastp.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.union.2.blastp.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.union.3.blastp.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.union.4.blastp.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.union.5.blastp.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.union.6.blastp.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.union.7.blastp.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.union.8.blastp.zip
    Glossina-fuscipes-IAEA_PEPTIDES_GfusI1.union.9.blastp.zip
```

### Next: ###

- Collect the resulting analysis files into single repository.

##########################################

# 2014-12-23 (Tuesday) #

## Meeting with Dan ##

- [markdown-docs/notes/meetings/dan-2014-12-23/dan-2014-12-23.md](file:///home/gus/Dropbox/repos/git/markdown-docs/notes/meetings/dan-2014-12-23/dan-2014-12-23.md)

## Argot2 batch size reduction: ##

- see 2014-12-22
- [2014-12-23_create_argot2_functional_annotation_db_GfusI1.1_prerelease.ipynb](http://localhost:8888/jupiter/notebooks/YALE/ddrad58/2014-12-23_create_argot2_functional_annotation_db_GfusI1.1_prerelease.ipynb)


##########################################

# 2014-12-24 (Wednesday) #

## Argot batch size reduction ##

- see 2014-12-23

### Storing in `Python`-friendly format (`pandas.HDFStore`) ###

- had to install `pytables`
- test work well and data is stored
- documentation: [2014-12-24_store_argot2_functional_annotation_db_GfusI1.1_prerelease_as_HDF5.ipynb](http://localhost:8888/jupiter/notebooks/YALE/ddrad58/2014-12-24_store_argot2_functional_annotation_db_GfusI1.1_prerelease_as_HDF5.ipynb)

### File location ###

```
louise/data/genomes/glossina_fuscipes/annotations/ \
functional/GfusI1.1_pre/argot2_out/argot_functional_annotations_ts150.h5
```

### PROJECT COMPLETED ###

"Argot batch size reduction" project is now considered completed.


## Installing `PyTables` ##

__First attempt  failed due to cryptic or at _least_ slightly misleading error about `numpy` and `numexpr`:__


~~~~~~~~ {.bash}
$ pip install git+https://github.com/PyTables/PyTables.git@v.3.1.1#egg=tables
~~~~~~~~~~~~~~~~~~~

__Tried installing `numexpr` directly with:__

~~~~~~~~ {.bash}
$ pip install numexpr
~~~~~~~~~~~~~~~~~~~

__Tried `PyTables` again:__

~~~~~~~~ {.bash}
$ pip install git+https://github.com/PyTables/PyTables.git@v.3.1.1#egg=tables
~~~~~~~~~~~~~~~~~~~

## P: Functional Annotations of genes near SNPs of interest ##

- Project start.