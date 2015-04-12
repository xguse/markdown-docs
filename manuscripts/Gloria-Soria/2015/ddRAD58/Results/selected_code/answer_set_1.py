def answer_set_1(df, title="None"):
    p = df.query("Aspect == 'P'")
    f = df.query("Aspect == 'F'")
    c = df.query("Aspect == 'C'")

    num_genes = len(df.gene_id.unique())
    num_contigs = len(df.bed3_seq.unique())
    num_func_annos = len(df.Name.unique())
    num_p = len(p.Name.unique())
    num_f = len(f.Name.unique())
    num_c = len(c.Name.unique())

    anno_stats = tbl(pd.DataFrame(df['Total Score'].describe()), headers=('Metric','Value'))
    anno_stats_p = tbl(pd.DataFrame(p['Total Score'].describe()), headers=('Metric','Value'))
    anno_stats_f = tbl(pd.DataFrame(f['Total Score'].describe()), headers=('Metric','Value'))
    anno_stats_c = tbl(pd.DataFrame(c['Total Score'].describe()), headers=('Metric','Value'))
    
    top10_annos = tbl(pd.DataFrame(df.Name.value_counts().head(10)), headers=('Annotation','Genes'))
    top10_annos_p= tbl(pd.DataFrame(p.Name.value_counts().head(10)), headers=('Annotation','Genes'))
    top10_annos_f= tbl(pd.DataFrame(f.Name.value_counts().head(10)), headers=('Annotation','Genes'))
    top10_annos_c= tbl(pd.DataFrame(c.Name.value_counts().head(10)), headers=('Annotation','Genes'))

    top10_annos_TS_800 = tbl(pd.DataFrame(df[df['Total Score'] >= 800].Name.value_counts().head(10)), headers=('Annotation','Genes'))
    top10_annos_TS_800_p = tbl(pd.DataFrame(p[p['Total Score'] >= 800].Name.value_counts().head(10)), headers=('Annotation','Genes'))
    top10_annos_TS_800_f = tbl(pd.DataFrame(f[f['Total Score'] >= 800].Name.value_counts().head(10)), headers=('Annotation','Genes'))
    top10_annos_TS_800_c = tbl(pd.DataFrame(c[c['Total Score'] >= 800].Name.value_counts().head(10)), headers=('Annotation','Genes'))


    return """
## {title} ##


- __Genes:__ {num_genes}
- __Contigs:__ {num_contigs}
- __Unique Terms (all):__ {num_func_annos}




### Annotation Scores ###

Table: All domains

{anno_stats}

Table: Process

{anno_stats_p}

Table: Function

{anno_stats_f}

Table: Cellular

{anno_stats_c}

----

### Top annotations ###

Table: All domains

{top10_annos}

Table: Process

{top10_annos_p}

Table: Function

{top10_annos_f}

Table: Cellular

{top10_annos_c}


----

### Top annotations (TS >= 800) ###

Table: All domains

{top10_annos_TS_800}

Table: Process

{top10_annos_TS_800_p}

Table: Function

{top10_annos_TS_800_f}

Table: Cellular

{top10_annos_TS_800_c}


\\newpage

""".format(
    title=title,
    num_genes=num_genes,
    num_contigs=num_contigs,
    num_func_annos=num_func_annos,
    anno_stats=anno_stats,
    anno_stats_p=anno_stats_p,
    anno_stats_f=anno_stats_f,
    anno_stats_c=anno_stats_c,
    top10_annos=top10_annos,
    top10_annos_p=top10_annos_p,
    top10_annos_f=top10_annos_f,
    top10_annos_c=top10_annos_c,
    top10_annos_TS_800=top10_annos_TS_800,
    top10_annos_TS_800_p=top10_annos_TS_800_p,
    top10_annos_TS_800_f=top10_annos_TS_800_f,
    top10_annos_TS_800_c=top10_annos_TS_800_c,
    )