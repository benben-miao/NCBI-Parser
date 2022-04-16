### 1. NCBI-Parser
Search any term from all NCBI databases to obtain matched entries, and download all NCBI GenBank format files and sequences corresponding to accessory number in genbank directory, finally  export all Species Latin names, Accessory Number, Sequence Length, Division, Collection Country, Collection Date, Collected Worker, Identified Worker, and Reference information, etc. of the search records as tabular files.
> Developer: https://github.com/benben-miao \
Github: https://github.com/benben-miao/NCBI-Parser \
PyPI: https://pypi.org/project/ncbiparser/

### 2. Usage
```bash
# Install the package
pip install ncbiparser

# Run the command internally
ncbiparser --help
Usage: ncbi-parser.exe [OPTIONS]

  Description: Search any term from all NCBI databases to obtain matched
  entries, and download all NCBI GenBank format files and sequences
  corresponding to accessory number in genbank directory, finally export all
  Species Latin names, Accessory Number, Sequence Length, Division, Collection
  Country, Collection Date, Collected Worker, Identified Worker, and Reference
  information, etc. of the search records as tabular files.

  1. Get options and parameters help:

  ncbiparser --help

  2. Example (simple information). Users only need to input the search term,
  and the default search is in NCBI nucleotide database:

  ncbiparser --term "Acanthopagrus 16S" --output results.xls

  3. Example (complete information). Specify the NCBI database type, input the
  search term, specify the number of records to download and extract, and
  suggest setting a larger parameter max_record:

  ncbiparser --db_type nucleotide --term "Acanthopagrus 16S" --max_record 500
  --res_type gb --output results.xls

Options:
  --db_type TEXT     Please input NCBI database type, default: "nucleotide",
                     including: [pubmed, protein, nuccore, ipg, nucleotide,
                     structure, genome, annotinfo, assembly, bioproject,
                     biosample, blastdbinfo, books, cdd, clinvar, gap,
                     gapplus, grasp, dbvar, gene, gds, geoprofiles,
                     homologene, medgen, mesh, ncbisearch, nlmcatalog, omim,
                     orgtrack, pmc, popset, proteinclusters, pcassay, protfam,
                     pccompound, pcsubstance, seqannot, snp, sra, taxonomy,
                     biocollections, gtr]  [required]
  --term TEXT        Please input search term content, default: "Acanthopagrus
                     16S"  [required]
  --max_record TEXT  Please input max record number, default: "100", up to:
                     10000  [required]
  --res_type TEXT    Please input result type, default: "gb", including:
                     ["gb", "fasta", "gbwithparts", "gbcoll"]
  --output TEXT      Please input output full name (path + name + extension).
                     default="results.xls"
  --help             Show this message and exit.
```

### 3. NCBI GenBank format
```shell
LOCUS       LC649152                1081 bp    DNA     linear   VRT 03-SEP-2021
DEFINITION  Acanthopagrus bifasciatus Kuroshio Biological Research Foundation
            KBF-I 361 mitochondrial genes for 12S rRNA, tRNA-Val, 16S rRNA,
            partial and complete sequence.
ACCESSION   LC649152
VERSION     LC649152.1
KEYWORDS    .
SOURCE      mitochondrion Acanthopagrus bifasciatus (twobar seabream)
  ORGANISM  Acanthopagrus bifasciatus
            Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;
            Actinopterygii; Neopterygii; Teleostei; Neoteleostei;
            Acanthomorphata; Eupercaria; Spariformes; Sparidae; Acanthopagrus.
REFERENCE   1
  AUTHORS   Sado,T., Fukuchi,T. and Miya,M.
  TITLE     Reference data for MiFish metabarcoding analysis
  JOURNAL   Unpublished
REFERENCE   2  (bases 1 to 1081)
  AUTHORS   Sado,T., Fukuchi,T. and Miya,M.
  TITLE     Direct Submission
  JOURNAL   Submitted (27-AUG-2021) Contact:Tetsuya Sado Natural History Museum
            & Institute, Chiba; 955-2 Aoba-cho, Chuo-ku, Chiba, Chiba 260-8682,
            Japan URL :http://www2.chiba-muse.or.jp/NATURAL/
FEATURES             Location/Qualifiers
     source          1..1081
                     /organism="Acanthopagrus bifasciatus"
                     /organelle="mitochondrion"
                     /mol_type="genomic DNA"
                     /specimen_voucher="Kuroshio Biological Research Foundation
                     KBF-I 361"
                     /db_xref="taxon:767411"
                     /PCR_primers="fwd_name: L-708-12S, fwd_seq:
                     ttayacatgcaagtatccgc, rev_name: H-1784-16SG, rev_seq:
                     ttcagctttcccttgcggtac"
     rRNA            <1..894
                     /product="12S ribosomal RNA"
     tRNA            895..967
                     /product="tRNA-Val"
     rRNA            968..>1081
                     /product="16S ribosomal RNA"
ORIGIN      
        1 acccccgtga aaatgcccta cagttccccg cccggaaaca aggagccggt atcaggcaca
       61 ttcaatttag cccacgacac cttgctcagc cacaccctca agggtactca gcagtgataa
      121 accttgacac ataagtgaaa acttgaatca gttaaagcta agtagggccg gtaaaactcg
      181 tgccagccac cgcggttata cgagaggccc aagttgttag aaatcggcgt aaagggtggt
      241 taagaataag attaaaatta aagccgaaca tctttagtag ctgttatacg ctttcaaaga
      301 caagaagccc aactgcgaaa gtagctttat attttctgaa cccacgaaag ctaaggtaca
      361 aactgggatt agatacccca ctatgcttag ccgtaaacat cgacagttta ttacattttc
      421 tgtccgcctg ggtactacaa gcattagctc aaaacccaaa ggacttggcg gtgctttaga
      481 cccacctaga ggagcctgtt ctagaaccga tattccccgt tcaacctcac ctctccttgc
      541 ctctcagcct atataccgcc gtcgttcagc ttaccctgtg aagggcaaaa agtaagcaaa
      601 attggcactg cccagtacgt caggtcgagg tgtagtcaat ggagtgggaa gaaatgggct
      661 acattccctt gtcttcaggg aactacgaat ggtgcactga aaatgtgtgc ctgaaggagg
      721 atttagcagt aagtagtaat ttagaatatt ctactgaagc cggctcttaa gcgcgcacac
      781 accgcccgtc actctccccg agactttaaa ttcacattaa ctaaaatatt aaatatcata
      841 gaggggaggc aagtcgtaac atggtaagtg taccggaagg tgtacttgga aaaccagcgc
      901 atagctaaac tagataaagc acctccctta cactgagaag atattcgtgc aaatcgaatt
      961 gccctgagcc tatcagctag ccctctaaca aaaaacaaca cacccccatc aattaacccc
     1021 caatgcactt acattaaatt aaacaaatca tttttccacc caagtatggg cgacagaaaa
     1081 g
//
```