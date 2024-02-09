
### 1 For PubMed search of RMS, scrape all the listings over many pages and get pmid, title, citation.

Use the link to get abtract and PMCID if it is available.

Store these in DB.

Vecorise abstract and insert in col abstract_vector. This gives the ability for semantic search of abstract as well as filter by meta data of citation date etc.
GITHUB-DOCLER-POSTRGRES-PGADMIN-PYTHON is main repo.

pgvector-build folder in IAS has build to create Postgress with pgvector.

GOAL: Create serach tool for semantic search of abstracts.

### 2 Crawl pubmed pdf library for all urls. These contain PMCID. Create a table of PMCID, url so that the pdf can be found and downloaded. PUBMED_NIH has these files.

