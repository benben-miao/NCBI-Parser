from Bio import Entrez, SeqIO, GenBank
import sys, os
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
  
  Entrez.email = "benben.miao@outlook.com"
  Entrez.api_key = "599c49d62fb353ea412ff6d13cedec568c09"

  # NCBI databases
  db_handle = Entrez.einfo()
  db_record = Entrez.read(db_handle)
  ncbi_db = db_record["DbList"]
  # print(ncbi_db)
  # ['pubmed', 'protein', 'nuccore', 'ipg', 'nucleotide', 'structure', 'genome', 'annotinfo', 'assembly', 'bioproject', 'biosample', 'blastdbinfo', 'books', 'cdd', 'clinvar', 'gap', 'gapplus', 'grasp', 'dbvar', 'gene', 'gds', 'geoprofiles', 'homologene', 'medgen', 'mesh', 'ncbisearch', 'nlmcatalog', 'omim', 'orgtrack', 'pmc', 'popset', 'proteinclusters', 'pcassay', 'protfam', 'pccompound', 'pcsubstance', 'seqannot', 'snp', 'sra', 'taxonomy', 'biocollections', 'gtr']
  
  if(not os.path.exists("./genbank")):
    os.mkdir("./genbank")
  # if(not os.exists("./seqs")):
  #   os.mkdir("./seqs")

  results_file = output
  results_handle = open(results_file, "w+")
  results_handle.write("Organism\tLocus\tLength\tDivision\tCountry\tCollection_date\tCollected_by\tIdentified_by\tReference\n")

  # Search database
  search_handle = Entrez.esearch(
    db=db_type,
    term=term,
    idtype="acc",
    retmax=max_record,
    retstart="0"
    )
  search_record = Entrez.read(search_handle)
  print("Total records: %s" %(search_record['Count']))

  for id in search_record['IdList']:
    # print(id)
    f_genbank = "./genbank/%s.gbk" %(id)
    f_sequence = "./genbank/%s.seq" %(id)
    
    if not os.path.isfile(f_genbank):
      fetch_handle = Entrez.efetch(
        db=db_type,
        id=id,
        rettype=res_type,
        retmode="text"
      )
      # Save genbank file
      gbk_record = fetch_handle.read()
      genbank_handle = open(f_genbank, "w")
      genbank_handle.write(gbk_record)
      print("Genbank file saved: %s" %(f_genbank))
      genbank_handle.close()
      fetch_handle.close()
    # Save sequence file
    seq_record = SeqIO.read(f_genbank, "genbank")
    seq_handle = open(f_sequence, "w")
    seq_handle.write(str(seq_record.seq))
    print("Sequence file saved: %s" %(f_sequence))
    seq_handle.close()
    
    # Parse genbank content to table
    with open(f_genbank, "r") as gbk_handle:
      for gbk_info in GenBank.parse(gbk_handle):
        # print(gbk_info.locus)
        # print(gbk_info.size)
        # print(gbk_info.residue_type)
        # print(gbk_info.data_file_division)
        # print(gbk_info.date)
        # print(gbk_info.definition)
        # print(gbk_info.accession)
        # print(gbk_info.nid)
        # print(gbk_info.pid)
        # print(gbk_info.version)
        # print(gbk_info.db_source)
        # print(gbk_info.gi)
        # print(gbk_info.keywords)
        # print(gbk_info.segment)
        # print(gbk_info.source)
        # print(gbk_info.organism)
        # print(gbk_info.taxonomy)
        # print(gbk_info.references)
        # print(gbk_info.comment)
        # print(gbk_info.features)
        # print(gbk_info.base_counts)
        # print(gbk_info.origin)
        # print(gbk_info.sequence)
        # print(gbk_info.contig)
        # print(gbk_info.dblinks)
        # print(gbk_info.references[0].number)
        # print(gbk_info.references[0].bases)
        # print(gbk_info.references[0].authors)
        # print(gbk_info.references[0].title)
        # print(gbk_info.references[0].journal)
        # print(gbk_info.references[0].pubmed_id)
        # print(gbk_info.references[0].remark)
        # print(gbk_info.features[0])
        # print(gbk_info.features[0])
        
        gbk_handle2 = SeqIO.read(f_genbank, "genbank")
        qualifiers = gbk_handle2.features[0].qualifiers
        # print(qualifiers['organism'][0])
        # print(qualifiers['organelle'][0])
        # print(qualifiers['mol_type'][0])
        # print(qualifiers['db_xref'][0])
        # print(qualifiers['country'][0])
        # print(qualifiers['collection_date'][0])
        # print(qualifiers['collected_by'][0])
        # print(qualifiers['identified_by'][0])
        
        organism = gbk_info.organism
        locus = gbk_info.locus
        length = gbk_info.size
        try:
          division = gbk_info.data_file_division + " " + gbk_info.date
        except:
          print("No division or date")
          division = "Unknown"
          
        try:
          country = qualifiers['country'][0]
        except:
          print("No country")
          country = "Unknown"
          
        try:
          collection_date = qualifiers['collection_date'][0]
        except:
          print("No collection date")
          collection_date = "Unknown"
          
        try:
          collected_by = qualifiers['collected_by'][0]
        except:
          print("No collected_by")
          collected_by = "Unknown"
        
        try:
          identified_by = qualifiers['identified_by'][0]
        except:
          print("No identified_by")
          identified_by = "Unknown"
        
        try:
          reference = gbk_info.references[0].authors + " " + gbk_info.references[0].title + " " + gbk_info.references[0].journal
        except:
          print("No reference")
          reference = "Unknown"
          
    results_handle.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" 
                        %(organism, locus, length, division, country, collection_date, collected_by, identified_by, reference))
  results_handle.close()

# if __name__ == '__main__':
#   run()