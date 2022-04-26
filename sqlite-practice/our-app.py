import database

# add record to database
#database.add_one("Jane", "Doe", "jane@dwhois.com")

# add many records
stuff = [
    ('Anna', 'John', 'anna@ffe.com'),
    ('Billy', 'Black', 'bills@money.com')
]
#database.add_many(stuff)

# look up email with WHERE
database.email_lookup("mylliejohnson@gmail.com")

# show all records
#database.show_all()

# delete one
#database.delete_one('5') # id has to be passed as string - rowid