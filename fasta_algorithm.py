from Bio.Seq import Seq
from Bio import Align
import sqlite3

#pass the query
query_seq = "A TATCTG"

# Connect to the database
conn = sqlite3.connect("my_database.db")

#create a cursor object to execute sql statement
c = conn.cursor()

# Execute a FASTA search using sql statement to select all record
c.execute("SELECT id, sequence FROM sequences")

#then we fetch the all records in a list of tuples.
target_records = c.fetchall()


# Initialize max score and alignment
max_score = None
max_alignment = None

#iterate each record
for target_record in target_records:
    # create pairwise alignment search object.
    aligner = Align.PairwiseAligner()
    # get the target seq from the records using indexing.
    target_seq = Seq(target_record[1])
    # create an alignment of the query_seq and target_seq
    alignment = aligner.align(query_seq, target_seq)
    # get the matching score between query and hit sequences
    score = aligner.score(query_seq, target_seq)

    # Print the results by first using indexing to tract target sequences
    print(f"> sequence  {target_record[0]}")
    #print the alignment
    print(alignment[0])
    #print the score
    print("Alignment score: ", score)
    print()

     # Check if current alignment has higher score than max
    if max_score is None or score > max_score:
        max_score = score
        max_alignment = alignment[0]


# Print the results for the max alignment
if max_alignment:
    print("****************************************************************")
    print("Max alignment:")
    print(max_alignment)
    print("Alignment score: ", max_score)

# Close the database connection
conn.close()