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


all:	$(PDFS) $(HTML) $(TEX) $(DOCX)

pdf:	clean $(PDFS)
html:	clean $(HTML)
tex:	clean $(TEX)
docx:	clean $(DOCX)


%.html:	%.md
	$(PANDOC) -r markdown+simple_tables+table_captions+yaml_metadata_block -w html -s -S --filter $(PANDOC_INTERNAL_REFS) --filter $(PANDOC_CITEPROC) -o $@ $<

%.tex:	%.md
	$(PANDOC) -r markdown+simple_tables+table_captions+yaml_metadata_block -w latex -s -S --latex-engine=pdflatex --filter $(PANDOC_INTERNAL_REFS) --filter $(PANDOC_CITEPROC) -o $@ $<


%.pdf:	%.md
	$(PANDOC) -r markdown+simple_tables+table_captions+yaml_metadata_block -s -S --latex-engine=pdflatex --filter $(PANDOC_INTERNAL_REFS) --filter $(PANDOC_CITEPROC) -o $@ $<


%.docx:	%.md
	$(PANDOC) -r markdown+simple_tables+table_captions+yaml_metadata_block -w docx -s -S  --filter $(PANDOC_INTERNAL_REFS) --filter $(PANDOC_CITEPROC) -o $@ $<


clean:
	rm -f *.html *.pdf *.tex *.doc*
