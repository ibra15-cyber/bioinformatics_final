import sqlite3

# Create a new SQLite database file
conn = sqlite3.connect('my_database.db')
#creating cursor icon
c = conn.cursor()

# Create a new table to store the sequence data
c.execute('''CREATE TABLE sequences
             (id INTEGER PRIMARY KEY, name TEXT, sequence TEXT)''')

# Define some sequences to insert into the database
sequences = [
    ('seq1', 'ATCG'),
    ('seq2', 'CGTA'),
    ('seq3', 'GCTA'),
    ('seq4', 'TACG')
]

# Insert the sequences into the database
c.executemany('INSERT INTO sequences (name, sequence) VALUES (?, ?)', sequences)

# Commit the changes and close the database connection
conn.commit()
conn.close()
