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