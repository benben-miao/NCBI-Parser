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

### 4. Click usage
```python
import click

@click.command()
@click.option('--db_type', type=str, default="nucleotide", required=True, nargs=1, 
            help='Please input NCBI database type, default: "nucleotide", including: [pubmed, protein, nuccore, ipg, nucleotide, structure, genome, annotinfo, assembly, bioproject, biosample, blastdbinfo, books, cdd, clinvar, gap, gapplus, grasp, dbvar, gene, gds, geoprofiles, homologene, medgen, mesh, ncbisearch, nlmcatalog, omim, orgtrack, pmc, popset, proteinclusters, pcassay, protfam, pccompound, pcsubstance, seqannot, snp, sra, taxonomy, biocollections, gtr]')
@click.option('--term', type=str, default="", required=True, nargs=1, 
            help='Please input search term content, default: "Acanthopagrus 16S"')
@click.option('--max_record', type=str, default="100", required=True, nargs=1, 
            help='Please input max record number, default: "100", up to: 10000')
@click.option('--res_type', type=str, default="gb", required=False, nargs=1, 
            help='Please input result type, default: "gb", including: ["gb", "fasta", "gbwithparts", "gbcoll"]')
@click.option('--output', type=str, default="results.xls", nargs=1, 
            help='Please input output full name (path + name + extension). default="results.xls"')

def run(db_type, term, max_record, res_type, output):

  """
  Description:
  Search any term from all NCBI databases to obtain matched entries, and download all NCBI GenBank format files and sequences corresponding to accessory number in genbank directory, finally export all Species Latin names, Accessory Number, Sequence Length, Division, Collection Country, Collection Date, Collected Worker, Identified Worker, and Reference information, etc. of the search records as tabular files. \n
  1. Get options and parameters help: \n
  ncbi-parser --help \n
  2. Example (simple information). Users only need to input the search term, and the default search is in NCBI nucleotide database: \n
  ncbi-parser --term "Acanthopagrus 16S" --output results.xls \n
  3. Example (complete information). Specify the NCBI database type, input the search term, specify the number of records to download and extract, and suggest setting a larger parameter max_record: \n
  ncbi-parser --db_type nucleotide --term "Acanthopagrus 16S" --max_record 500 --res_type gb --output results.xls \n
  """

  results_file = output
```

### 5. Pyinstaller usage
```shell
mamba create -n ncbiparser python=3.8
conda activate ncbiparser

which python
pip install biopython click
python ncbiparser.py --help

pip install pyinstaller
pyinstall -F ncbiparser.py -i favicon.ico
```

### 6. Package and publish `ncbiparser` to PyPI
#### 6.1 Create setup.py file
```python
#!/usr/bin/python
# _*_ coding:utf-8 _*_

from setuptools import setup, find_packages

### 1. Read the README.md contents
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
readme = 'ncbiparser/README.md'

### 2. Setup the package configure
setup(
    # 2.1 Package information
    name="ncbiparser",
    version="1.0.0",
    url="https://github.com/benben-miao/NCBI-Parser",
    keywords=["CLI", "Biology", "NCBI", "Parser"],
    description="Search and fetch the Species Latin names, Accessory Number, Sequence Length, Division, Collection Country, Collection Date, Collected Worker, Identified Worker, and Reference information, etc. of the search records as tabular files.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    download_url="https://pypi.org/project/ncbi-parser",

    # 2.2 Developer information
    author="benben-miao",
    author_email="benben.miao@outlook.com",
    maintainer="benben-miao",
    maintainer_email="benben.miao@outlook.com",
    license="MIT License",

    # 2.3 Package configure
    # include_package_data=True,
    platforms="any",
    install_requires=['biopython', 'click'],
    # packages=find_packages(),
    packages=['ncbiparser'],
    entry_points={
        'console_scripts': ['ncbiparser=ncbiparser.ncbiparser:run']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    data_files=[readme],
    # package_data={
    #     '':['examples/*.xlsx']
    # },
    include_package_data=True
    # exclude_package_data={
    # }
)

### 3. Package build, test and publish
# 3.1 Install setuptools with wheel and twine
# pip install --upgrade setuptools wheel twine

# 3.2 Check the setup.py content
# python setup.py check

# 3.2 Build source code tarball
# python setup.py sdist

# 3.3 Build wheel package and test
# python setup.py bdist_wheel
# pip install dist\*.whl

# 3.4 Test package and uninstall test version
# ncbiparser --help
# pip uninstall ncbiparser

# 3.5 Publish the package to PyPI
# twine upload dist/*
```

#### 6.2 Create the MANIFEST.in file
```in
include *.py *.md
recursive-include examples *.sh *.py *.ipynb *.txt *.xlsx *.gbk *.fasta *.seq
```

#### 6.3 Commands
```shell
### 3. Package build, test and publish
# 3.1 Install setuptools with wheel and twine
pip install --upgrade setuptools wheel twine

# 3.2 Check the setup.py content
python setup.py check

# 3.2 Build source code tarball
python setup.py sdist

# 3.3 Build wheel package and test
python setup.py bdist_wheel
pip install dist\*.whl

# 3.4 Test package and uninstall test version
ncbiparser --help
pip uninstall ncbiparser

# 3.5 Publish the package to PyPI
twine upload dist/*
```