import MySQLdb

db = MySQLdb.connect(host="host",    # your host, usually localhost
                     user="username",         # your username
                     passwd="password",  # your password
                     db="database")        # name of the data base

# you must create a Cursor object. It will let you execute all the queries 
cursor = db.cursor()

# The sql
cursor.execute("SELECT * FROM YOUR_TABLE_NAME")

# Print first roll queried
for row in cursor.fetchall():
    print( row[0])

db.close()

# if it's a insert or update, be sure to have db.commit() after the cursor.execute()
