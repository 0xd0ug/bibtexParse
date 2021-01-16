#!/usr/bin/env python3

import bibtexparser

with open('references.bib') as input_file:
    bib_entries = bibtexparser.load(input_file)

for x in bib_entries.entries:
    id = x["ID"]
    try:
        year = x["year"]
    except KeyError:
        year = ""
    print("\cite{"+id+"}\t"+year)
