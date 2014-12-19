---
title: RE java and snpEff
author: Gus Dunn
date: 2014-12-18
documentclass: scrartcl
classoption: letterpaper
geometry: margin=1in
graphics: 1
fontfamily: fourier
tags: email, mariangela, help
read: "+simple_tables+table_captions+footnotes+inline_notes+fenced_code_blocks+fenced_code_attributes+fancy_lists+definition_lists+superscript+subscript+tex_math_dollars"
...


# 2014-12-18 #

## First of all: ##

I am exceedingly proud of you!
You totally rocked this email!
You gave me like 99% of what I needed to think about this problem effectively without me having to ask a single question!
I hope that you notice your improved computer literacy and allow yourself to feel some pride as well.
You deserve it.

## So on to the `snpEff` stuff: ##

> when i run "which java" i get:

```
mariangelabonizzoni@dhcp-v106-224 17:31:49 ~:
which java
/usr/bin/java
```

> when i call `java`, i get the help menu.

> When i call `java -version`, i get the java version as:

```
mariangelabonizzoni@dhcp-v106-224 17:31:53 ~:
java -version
java version "1.8.0_25"
Java(TM) SE Runtime Environment (build 1.8.0_25-b17)
Java HotSpot(TM) 64-Bit Server VM (build 25.25-b02, mixed mode)
```

> When i call `which snpEff`, i get:

```
which snpEff
/usr/local/bin/snpEff
```

> snpEff is supposely a java program to be run through `java -jar
> snpEff.jar`, but when i do it, i always get the message:

```
mariangelabonizzoni@dhcp-v106-224 17:33:18 ~:
java -jar snpEff.jar
Error: Unable to access jarfile snpEff.jar
```

> I tried to run this command with many different variants, like going into
> /user/local/bin or from /user/bin or using instead of sniper.jar the whole
> path to the program, but i always get the same message.
> 
> interestingly, when i simply type `snpEff`, i get the help menu. As follows

```
snpEff
Error: Missing command

snpEff version SnpEff 3.6c (build 2014-05-20), by Pablo Cingolani
Usage: snpEff [command] [options] [files]

Run 'java -jar snpEff.jar command' for help on each specific command

Available commands:
        [eff]                        : Calculate effect of variants. Default: eff
(no command or 'eff').
        build                        : Build a SnpEff database.
        XXXXXXXXXXX
        -ud , -upDownStreamLen <int> : Set upstream downstream interval length
(in bases)
```

### My reply: ###
Yes.

I am fairly certain that the correct way to call snpEff is to omit the `java -jar` call and simply call `snpEff` directly.
The reason for this is that it has been installed in `/usr/local/bin` which is almost always in the user's `$PATH` variable by default.
The way that it is installed the `java -jar` portion is implied and the computer takes care of it behind the scenes.

The help text is an unfortunate confusion: for __for sure__.
But again, I am quite proud that you basically figured this out without my help at all.
Very nice work, Dr!

## The genome data files: ##

> the big problem that i have is that i have to build a genomic database
> because the organism that i want to study is not supported (it is an asian
> mosquito). i downloaded the required genome sequences and annotation file
> in GTF from vectorbase and i followed (i thik i did) the instruction in
> the "create database" from the snpEff menu page. but i keep getting the
> same message as:
> genome not found. see below. i tried i do not how amny different options
> to change the name of the files, to run the comand from different folders,
> to change the configuration file for snapped, i alwasy get the same
> message. like the genome file is not seen. it is driving me creasy!!!! any
> idea? I wrote to the snpEff developers, but thye have not had the curtesy
> to reply yet. any suggestion would be great!!! thanks

```
snpEff build -gtf22 /Volumes/Seagate_Exp_1/snpEff/data/AsinC2.1
java.lang.RuntimeException: Property:
'/Volumes/Seagate_Exp_1/snpEff/data/AsinC2.1.genome' not found
        at ca.mcgill.mcb.pcingola.interval.Genome.<init>(Genome.java:92)
        at ca.mcgill.mcb.pcingola.snpEffect.Config.readGenomeConfig(Config.java:513)
        at ca.mcgill.mcb.pcingola.snpEffect.Config.readConfig(Config.java:476)
        at ca.mcgill.mcb.pcingola.snpEffect.Config.init(Config.java:377)
        at ca.mcgill.mcb.pcingola.snpEffect.Config.<init>(Config.java:99)
        at
ca.mcgill.mcb.pcingola.snpEffect.commandLine.SnpEff.loadConfig(SnpEff.java:236)
        at
ca.mcgill.mcb.pcingola.snpEffect.commandLine.SnpEffCmdBuild.run(SnpEffCmdBuild.java:256)
        at ca.mcgill.mcb.pcingola.snpEffect.commandLine.SnpEff.run(SnpEff.java:685)
        at ca.mcgill.mcb.pcingola.snpEffect.commandLine.SnpEff.main(SnpEff.java:118)
```

### My reply: ###
Ok.
This is a bit more complicated.
I am going to have to try looking through the `snpEff.config` file that they mention.
It looks like this file is how you set up all the locations of things that you will need to organize to let `snpEff` know how to build its databases.
Did you configure this file yet?
If so, would you send me the file so I have a place to start?

Gus