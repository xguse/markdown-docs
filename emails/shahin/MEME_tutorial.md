First, thank you for assuming that I hold the honorific title of Professor.  However, I am but a lowly postdoc at the moment.  No need for such formalities with me!  Gus is fine.

Ok now, bear with me this may get a LITTLE complicated depending on how familiar you are with these websites.


------------------------------------------


## Best option: use the MEME website ##

I believe that the best/easiest method for you will be to use the motif search programs that are part of the MEME suite of programs (http://meme.nbcr.net/meme/).  You can download and install these to your computer if you want but unless you need to I would advise against it if you are not VERY comfortable installing such things using the command line.  They are available over the web. The specific programs are listed in the navigation bar on the left of the page under "Motif Scanning".

There are a few different programs that I will let you read about in that section. The most basic is called [FIMO](http://meme.nbcr.net/meme/tools/fimo) and I will walk you through how to use it.  After that I will assume that you will be able to use what you learned to apply it to the other programs that might be of interest to you on that site.

Even though I am showing you how to use FIMO, I am not saying that it is the best.  It does nothing to measure whether the found motifs are actually present in the sequences more often than would be expected to occur by chance alone, GIVEN THE SEQUENCES YOU PROVIDE.  For a much better treatment of motif enrichment, you should use [AME](http://meme.nbcr.net/meme/tools/ame).  AME, also does not require that you provide your own motifs (it allows you to select from many databases). However AME does not return the locations of the matches in your sequences, so you will need to use FIMO to get those if you need them.

## The motifs ##

Since you are looking at insect cuticular genes, I am going to assume that you would like to search for insect TFBS motifs.  You will not find much help on the MEME pages.  If you have a set already, you will need to make sure that they are in the format that MEME expects.  Its called MEME format.  I took the liberty of downloading all of the insect motifs hosted on the [JASPAR](http://jaspar.genereg.net/) motif database of at least partially validated motif matrices.  Go to that site and read about it and learn how to cite it because you will need to if you use these motifs.  And you should talk about why you used them as well in your methods.  There are ~130.

The basic format JASPAR uses is NOT MEME format.  So I converted them for you because it is not straightforward and I dont think you can do it on their website.  I have attached these files. The `*.pfm` is the original JASPAR file and the `*.meme` is the MEME formated one.


------------------------------------------


## FIMO: tutorial ##

Go to the [FIMO](http://meme.nbcr.net/meme/tools/fimo) site.

Below I will go over what you need for each section of input for the tool.

### Input the motifs ###

1. select "upload motifs" from the drop-down menu.
2. click "choose file" button and browse to your MEME formatted motif file.

### Input the sequences ###

1. select "upload sequences" from the drop-down men
2. click "choose file" button and brows to your fasta file of promoter sequences. 

### Input job details ###

1. enter your email address for notification when the job completes.
2. enter a DESCRIPTIVE sentence about this job to help you remember which run the results came from and what you wanted to learn.

### Advanced options ###

I would not normally change this, but read about what options they provide in case it makes sense for you.

### Submit your job ###

1. click "start search"


------------------------------------------


## Final thoughts ##

Good luck.  As I said, you should really use AME to answer "What motifs may be important in driving THESE SPECIFIC PROMOTERS?".  However, you should also run FIMO and [MCAST](http://meme.nbcr.net/meme/tools/mcast). Not just to get the locations of the motifs identified by AME, but to know what other motifs may be playing supporting roles.

I hope that this helps you.  Let me know if you have any other questions.  I will do my best to answer quickly, but I am very busy right now so it may not be right away!

