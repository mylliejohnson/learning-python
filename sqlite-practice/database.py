import sqlite3

# 1. create connection to database !
#conn = sqlite3.connect(':memory:') # creates in memory, doesnt save
conn = sqlite3.connect('customer.db')

# 2. create cursor
curs = conn.cursor()

# 3. create table
# curs.execute(''' CREATE TABLE customers (
#         first_name DATATYPE,
#         last_name DATATYPE,
#         email DATATYPE
#     )''')

# 6. insert one record into table
# curs.execute('INSERT INTO customers VALUES ("Alli", "Jones", "allijones@gmail.com")')

# 7. insert many records

# many_customers = [
#     ('Dora', 'Jones', 'deejones@gmail.com'),
#     ('Dawne', 'Ross', 'dross@gmail.com'),
#     ('Lauren', 'Jones', 'lauren@email.com')
# ]
# curs.executemany('INSERT INTO customers VALUES (?,?,?)', many_customers)

# 8. query the database
curs.execute("SELECT rowid, * FROM customers")
# # curs.fetchone(), curs.fetchone()[0] --> Myllie
# # curs.fetchmany(3)
# # print(curs.fetchall())

items = curs.fetchall()
print (items)

# for item in items:
#     #print(item) # prints on one line individually
#     print(item[0] + ' ' + item[1] + ' \t ' + item[2])


# 9. primary keys
# sqlite creates primary key (row) automatically
# rowid --- curs.execute("SELECT rowid, * FROM customers")

# 10. WHERE CLAUSE
# curs.execute("SELECT * FROM customers WHERE last_name LIKE 'Jo%'")
# items = curs.fetchall()
# print(items) 

# 11. UPDATE RECORDS
# curs.execute(""" UPDATE customers SET first_name = 'Myleika' WHERE last_name = 'Johnson'
# """)
# curs.execute(""" UPDATE customers SET first_name = 'Mylls' WHERE rowid = 1
#  """)
# conn.commit()
# curs.execute("SELECT rowid, * FROM customers")
# print(items)


# 12. DELETE RECORD
# curs.execute("DELETE from customers where rowid = 4")
# conn.commit()
# curs.execute("SELECT rowid, * FROM customers")
# print(items)


print('command executed successfully')
#  commit command/connection
conn.commit()
# close connection
conn.close()