---
documentclass: report
classoption: letterpaper
geometry: margin=1in, landscape
#toc: 1
graphics: 1
#bibliography: tsetse_RO1_progress_wad.bib
#css: https://raw.githubusercontent.com/xguse/buttondown/master/buttondown.css
#css: tsetse_RO1_progress_wad.css
tags: report, tsetse R01, database, TsetseSampleDB
fontfamily: bookman
...

<!--
|	District	|	Collection End Date	|	Villages	|	Traps	|	Flies Collected	|	Flies/Trap	|	Live Flies/Trap	|	Males	|	Females	|	F:M	|	Flies Dissected	|	Flies Infected	|	Estimated Infection Rate	|
|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|
|	Kole	|	2014-03-30	|	5	|	40	|	1227	|	30.68	|	10.70	|	564	|	663	|	1.18	|	428	|	5	|	1.20%	|
|	Oyam	|	2014-05-22	|	9	|	32	|	715	|	22.34	|	10.50	|	298	|	417	|	1.40	|	336	|	10	|	3.00%	|
|	Kole & Oyam	|	2014-07-21	|	4	|	27	|	1198	|	44.37	|	22.85	|	432	|	766	|	1.77	|	617	|	27	|	4.38%	|
|	Nwoya	|	2014-07-26	|	2	|	20	|	728	|	36.40	|	12.60	|	291	|	437	|	1.50	|	252	|	3	|	1.19%	|
|	Amuru	|	2014-07-29	|	2	|	18	|	243	|	13.50	|	7.78	|	67	|	176	|	2.63	|	140	|	0	|	0.00%	|
|	Adjumani	|	2014-08-02	|	3	|	20	|	182	|	9.10	|	6.00	|	60	|	122	|	2.03	|	120	|	0	|	0.00%	|
|	Moyo	|	2014-06-20	|	5	|	32	|	164	|	5.13	|	3.31	|	63	|	101	|	1.60	|	106	|	0	|	0.00%	|
|	Arua	|	2014-06-26	|	7	|	34	|	681	|	20.03	|	10.18	|	287	|	394	|	1.37	|	346	|	3	|	0.87%	|
|	Kitgum	|	2014-10-19	|	4	|	18	|	281	|	15.61	|	9.61	|	120	|	161	|	1.34	|	173	|	4	|	2.31%	|
|	Lamwo	|	2014-10-19	|	4	|	15	|	101	|	6.73	|	3.20	|	37	|	64	|	1.73	|	48	|	0	|	0.00%	|
|	Pader	|	2014-10-19	|	6	|	26	|	152	|	5.85	|	4.19	|	39	|	113	|	2.90	|	109	|	1	|	0.92%	|

-->

Table: Raw summary information about each survey.

|	District	|	Collection End Date	|	Villages	|	Traps	|	Flies Collected	|	Males	|	Females	|	Flies Dissected	|	Flies Infected	|
|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|
|	Kole	|	2014-03-30	|	5	|	40	|	1227	|	564	|	663	|	428	|	5	|
|	Oyam	|	2014-05-22	|	9	|	32	|	715	|	298	|	417	|	336	|	10	|
|	Kole & Oyam	|	2014-07-21	|	4	|	27	|	1198	|	432	|	766	|	617	|	27	|
|	Nwoya	|	2014-07-26	|	2	|	20	|	728	|	291	|	437	|	252	|	3	|
|	Amuru	|	2014-07-29	|	2	|	18	|	243	|	67	|	176	|	140	|	0	|
|	Adjumani	|	2014-08-02	|	3	|	20	|	182	|	60	|	122	|	120	|	0	|
|	Moyo	|	2014-06-20	|	5	|	32	|	164	|	63	|	101	|	106	|	0	|
|	Arua	|	2014-06-26	|	7	|	34	|	681	|	287	|	394	|	346	|	3	|
|	Kitgum	|	2014-10-19	|	4	|	18	|	281	|	120	|	161	|	173	|	4	|
|	Lamwo	|	2014-10-19	|	4	|	15	|	101	|	37	|	64	|	48	|	0	|
|	Pader	|	2014-10-19	|	6	|	26	|	152	|	39	|	113	|	109	|	1	|



Table: Secondary summary statistics for each survey.

|	District	|	Collection End Date	|	Flies/Trap	|	Live Flies/Trap	|	F:M	|	Estimated Infection Rate	|
|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|	:----------:	|
|	Kole	|	2014-03-30	|	30.68	|	10.70	|	1.18	|	1.20%	|
|	Oyam	|	2014-05-22	|	22.34	|	10.50	|	1.40	|	3.00%	|
|	Kole & Oyam	|	2014-07-21	|	44.37	|	22.85	|	1.77	|	4.38%	|
|	Nwoya	|	2014-07-26	|	36.40	|	12.60	|	1.50	|	1.19%	|
|	Amuru	|	2014-07-29	|	13.50	|	7.78	|	2.63	|	0.00%	|
|	Adjumani	|	2014-08-02	|	9.10	|	6.00	|	2.03	|	0.00%	|
|	Moyo	|	2014-06-20	|	5.13	|	3.31	|	1.60	|	0.00%	|
|	Arua	|	2014-06-26	|	20.03	|	10.18	|	1.37	|	0.87%	|
|	Kitgum	|	2014-10-19	|	15.61	|	9.61	|	1.34	|	2.31%	|
|	Lamwo	|	2014-10-19	|	6.73	|	3.20	|	1.73	|	0.00%	|
|	Pader	|	2014-10-19	|	5.85	|	4.19	|	2.90	|	0.92%	|






