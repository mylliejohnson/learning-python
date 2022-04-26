import sqlite3

# query database and return all records
def show_all():
    # connect to database
    conn = sqlite3.connect('customer.db')

    # create cursor
    c = conn.cursor()

    #query database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()
    
# add new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
    conn.commit()
    conn.close()

# def add many records
def add_many(List):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", (List))
    conn.commit()
    conn.close()

def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

# look up with where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("SELECT * FROM customers WHERE email = (?)", (email,))

    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()