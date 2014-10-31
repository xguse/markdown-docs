---
title: Tsetse R01 Progress Report
subtitle: Sampling and Databasing
author: Robert Opiro, Augustine Dunn
date: 2014-10-30
documentclass: report
classoption: letterpaper
toc: 1
graphics: 1
bibliography: tsetse_RO1_progress_wad.bib
#css: https://raw.githubusercontent.com/xguse/buttondown/master/buttondown.css
css: tsetse_RO1_progress_wad.css
tags: report, tsetse R01, database, TsetseSampleDB
fontfamily: bookman
...


<!--
# Outline {#outline}
1. Relevant Specific Aims
	a. __SA1:__ Analyze the genomic variation in _Gff_ and its associated microbiome.
	b. __SA3:__ Discover gene-environment associations and impacts of climate change on Ugandan _Gff_.
	c. __SA4:__ Understand factors that regulate the differentiation of _Gff_ populations.
1. Sampling
	a. Times and areas Sampled
	b. asjh
1. Positives Recovery
1. Sample and Analysis Database Development
-->

# Specimen database # 

A multitude of data is associated with each fly collected.
The type of information includes the list of tissues collected, the collection date, village name and location, sex, species, trap number, infection status, notes on human activity surrounding the trap, and more.
All of this information needs to remain tied to all specimens, materials, and _data_ derived from these as the project goes forward.

We are designing and implementing a custom database and web application to manage, track, and facilitate analysis of the thousands of specimen tubes associated with this project that will be generated and exist already.
The system consists of a web-based user interface, two SQL-based relational databases, and a layer of custom python functions that connect the two.
The web-based interface uses the open-source [Bootstrap](http://getbootstrap.com/) web interface components.
One SQL database will act as the official storage system for the specimen data, while the second will manage checkout requests by our researchers and update the main storage database upon validation.
The custom python code is based on the open-source [Flask](https://github.com/mitsuhiko/flask) web-microframework.
This code manages the two databases according to requests made through the web-interface.
It also manages user registration and permissions along with site-security.
Finally, it will also allow us to easily design and run complex analyses with the specimen data encoded in the main database.



# Collections Overview #
## Study sites ##
The surveys were done in the Ugandan districts of Kole, Oyam, Nwoya, Amuru, Adjumani, Moyo, Arua, Kitgum, Lamwo, and Pader. Additional information on tsetse population distribution was obtained from the District Entomology Offices of the relevant districts. 

## Data collection ##
Trapping for tsetse flies were carried out using biconicals traps [@ChallierAandLaveissiere1973].
The coordinates for each trap site were taken using a hand-held GPS.
Vegetation types and human activities at the trapping sites were also recorded.
Each village is at least 5km apart; a single village is taken to be a trapping site (with a number of traps deployed in each).

## Dissection and examination ##
Trapped flies were identified, sexed, counted, recorded and transported to a field dissection site.
Live flies were dissected and examined microscopically to determine the presence/absence of trypanosomes in the midguts/salivary glands.
The midguts, fly carcass, reproductive parts, and heads were then preserved in parafilm-sealed and labeled cryo-tubes in either 90% ethanol or RNA-preservation solution for further molecular studies.

# Collection Results Summary #

## Kole District (`2014-03-22 to 2014-03-30`) ##
Five villages were surveyed (Olepo [OLE], Mwanya [MWA], Akayo-debe [AKA], Aputu-Lwaa [APU], and Ocala [OCA]) with a total of 40 traps.
1227 _Gff_ were captured (564 M and 663 F) and yielded five infected individuals (1.2% estimated infection rate).


## Oyam District (`2014-05-17 to 2014-05-22`) ##
Nine villages were surveyed (Ocala [OCA], Odworo [OD], Alege [ALE], Acankoma [ACA], Oguk [OGU], Agoba B [AG], Abok[ABO], Ocol [OCL] and Opuyu [OPU]) with 32 traps.
715 _Gff_ were captured (298 M and 417 F) and yielded 10 infected individuals (3.0% estimated infection rate).


## Oyam and Kole Districts (`2014-07-14 to 2014-07-21`) ##
This survey targeted sites that produced infected flies from the previous surveys.
The field team deployed 27 traps across four villages that were divided between the two districts: __Oyam:__ (Ocala [OCA], Odworo [OD], Acankoma [ACA]) and __Kole:__ (Akayodebe [AKA]).

1198 _Gff_ were captured (432 M and 766 F) and yielded 27 infected individuals (4.38% estimated infection rate).


## Nwoya District (`2014-07-22 to 2014-07-26`) ##
The field team deployed 20 traps across two villages (the Uganda Wildlife Authority [UWA] and Te-Okot [TEO]).
_Gp_ and _Gmm_ were trapped in this region in addtion to _Gff_; however only the data for _Gff_ is reported here.
728 _Gff_ were captured (291 M and 437 F) and three were positive by microscopic examination.


## Amuru District (`2014-07-27 to 2014-07-29`) ##
Two villages were surveyed (Gorodona [GOR] and Okidi south [OKS]) using 18 traps.
243 _Gff_ were captured (67 M and 176 F) and yielded no infected individuals.


## Adjumani District (`2014-07-30 to 2014-08-02`) ##
Three villages were surveyed (Olobo [OLO], Olwi [OLW], Osugo East and West [OSG]) with 20 traps.
182 _Gff_ were captured (60 M and 122 F) and yielded no infected individuals.


## Moyo District (`2014-06-16 to 2014-06-20`) ##
Five villages were surveyed (Ori [ORI], Orubakulem [ORB], Lea [LEA], Cefo [CE],and Moyipi [MOP]) with 32 traps.
164 _Gff_ were captured (63 M and 101 F) and yielded no infected individuals.


## Arua District (`2014-06-21 to 2014-06-26`) ##
Seven villages were surveyed (Gangu [GAN], Aliodri [ALI], Jaiko [JIA], Duku [DUK], Wende [WEN], Aina [AIN], and Orivu [ORV]) with 34 traps.
681 _Gff_ were captured (287 M and 394 F) and yielded three infected individuals (0.87% estimated infection rate).


## Kitgum, Lamwo, and Pader Districts (`2014-10-06 to 2014-10-19`) ##
In the three districts combined, 534 _Gff_ were captured (193 M and 341 F).
59 traps were deployed across 14 villiages.
330 flies were dissected and 5 were found to be infected (1.52% combined estimated infection rate)

### Kitgum ###
Four villages were surveyed (Kitgum town council [KTC],  Liba [LIB],  Bola [BOL],  Tumangu [TUM]) with 18 traps.
281 _Gff_ were captured (120 M and 161 F), and 173 dissected.
Four infected individuals were detected (2.31% estimated infection rate).

### Lamwo ###
Four villages were surveyed (Lagwel [LAG],  Ngomoromo [NGO],  Pawor [PAW],  Lakwala [LAK]) with 15 traps.
101 _Gff_ were captured (37 M and 64 F), and 48 dissected.
Zero infected individuals were detected.

### Pader ###
Six villages were surveyed (Alim [ALI],  Chua [CHU],  Kilak [KIL],  Aswa Bridge [ASW],  Omido [OMI],  Atanga Mission [ATM]) with 26 traps.
152 _Gff_ were captured (39 M and 113 F), and 109 dissected.
One infected individual was detected (0.92% estimated infection rate).


<!--
## XXX District (`2014-XX-XX to 2014-XX-XX`) ##
XXXX villages were surveyed (XXXX) with XXX traps.
XXX _Gff_ were captured (XXX M and XXX F), and XXX dissected.
XX infected individuals were detected (XXX% estimated infection rate).
-->

<!--
<div id='#fig:map'>
![Map of districts and villages surveyed.](/home/gus/Dropbox/uganda data/2014_Collection_Sheets_Spring-Summer/2014_full_surveyreport_20140820/Village_map_2014-10-21T20:42:32Z.png)

</div>
-->



# References 
