## Put this Makefile in your project directory---i.e., the directory
## containing the paper you are writing. Assuming you are using the
## rest of the toolchain here, you can use it to create .html, .tex,
## and .pdf output files (complete with bibliography, if present) from
## your markdown file. 
## -	Change the paths at the top of the file as needed.
## -	Using `make` without arguments will generate html, tex, and pdf 
## 	output files from all of the files with the designated markdown
##	extension. The default is `.md` but you can change this. 
## -	You can specify an output format with `make tex`, `make pdf` or 
## - 	`make html`. 
## -	Doing `make clean` will remove all the .tex, .html, and .pdf files 
## 	in your working directory. Make sure you do not have files in these
##	formats that you want to keep!

## Personal Macros

PANDOC=$(HOME)/.cabal/bin/pandoc
PANDOC_CITEPROC=$(HOME)/.cabal/bin/pandoc-citeproc
PANDOC_INTERNAL_REFS=$(VIRTUAL_ENV)/bin/internal-references


## Markdown extension (e.g. md, markdown, mdown).
MEXT = md

## All markdown files in the working directory
SRC = $(wildcard *.$(MEXT))

## Location of Pandoc support files.
PREFIX = $(HOME)/.pandoc

## Location of your working bibliography file
BIB = $(SRC:.md=.bib)

## CSL stylesheet (located in the csl folder of the PREFIX directory).
CSL = apsa


PDFS=$(SRC:.md=.pdf)
HTML=$(SRC:.md=.html)
TEX=$(SRC:.md=.tex)
DOCX=$(SRC:.md=.docx)

## Set up the extensions to load for pandoc common to all invocations
PAN_OPTS=--number-sections --highlight-style zenburn
PAN_EXTENTIONS=markdown+simple_tables+table_captions+yaml_metadata_block
PAN_FILTERS=--filter $(PANDOC_CITEPROC)


all:	$(PDFS) $(HTML) $(TEX) $(DOCX)

pdf:	clean $(PDFS)
html:	clean $(HTML)
tex:	clean $(TEX)
docx:	clean $(DOCX)


%.html:	%.md
	$(PANDOC) $(PAN_OPTS) -r $(PAN_EXTENTIONS) -w html -s -S  $(PAN_FILTERS) -o $@ $<

%.tex:	%.md
	$(PANDOC) $(PAN_OPTS) -r $(PAN_EXTENTIONS) -w latex -s -S --latex-engine=pdflatex  $(PAN_FILTERS) -o $@ $<


%.pdf:	%.md
	$(PANDOC) $(PAN_OPTS) -r $(PAN_EXTENTIONS) -s -S --latex-engine=pdflatex  $(PAN_FILTERS) -o $@ $<


%.docx:	%.md
	$(PANDOC) $(PAN_OPTS) -r $(PAN_EXTENTIONS) -w docx -s -S   $(PAN_FILTERS) -o $@ $<


clean:
	rm -f *.html *.pdf *.tex *.doc*
