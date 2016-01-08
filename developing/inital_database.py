#! /usr/bin/env python3
import fileinput
import os
import sqlite3

os.makedirs('../db',exist_ok=True)
conn = sqlite3.connect('../db/invantary.db')
c = conn.cursor()

# Create table inventary
c.execute('''CREATE TABLE IF NOT EXISTS inventary (
    ID INTEGER PRIMARY KEY NOT NULL,
    ID_typ INTEGER NOT NULL,
    ID_location INTEGER NOT NULL,
    ID_tbr INTEGER NOT NULL,
    ID_category INTEGER NOT NULL,
    objectname TEXT NOT NULL,
    vendor_id TEXT NOT NULL,
    amount REAL NOT NULL,
    date_of_purchase DATE NOT NULL,
    single REAL NOT NULL,
    total REAL NOT NULL,
    fair_value REAL NOT NULL,
    FOREIGN KEY(ID_typ) REFERENCES typ(ID),
    FOREIGN KEY(ID_location) REFERENCES location(ID),
    FOREIGN KEY(ID_tbr) REFERENCES time_between_replacement(ID),
    FOREIGN KEY(ID_category) REFERENCES category(ID)
)''')

# Create table location
c.execute('''CREATE TABLE IF NOT EXISTS location (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    location TEXT NOT NULL
)''')

# Create table typ
c.execute('''CREATE TABLE IF NOT EXISTS typ (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    typ TEXT NOT NULL
)''')

# Create table time_between_replacement
c.execute('''CREATE TABLE IF NOT EXISTS time_between_replacement (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    tbr INTEGER NOT NULL
)''')

# Create table category
c.execute('''CREATE TABLE IF NOT EXISTS category (
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    category TEXT NOT NULL
)''')

# Save (commit) the changes
conn.commit()

# Fill tables

## table location
# possible errors: RuntimeError, FileNotFoundError
with fileinput.input(files=('rooms.txt')) as f:
        for line in f:
            room = line.strip().rstrip(os.linesep)
            if (True == room.isspace()):
                continue

            c.execute("SELECT location FROM location WHERE location=:room",{"room":room})
            if (None == c.fetchone()):
                print("add room: "+room);
                c.execute('''INSERT INTO location(location) VALUES (:room)''',{"room":room})

# Save (commit) the changes
conn.commit()

## table typ
# possible errors: RuntimeError, FileNotFoundError
with fileinput.input(files=('typs.txt')) as f:
        for line in f:
            typ = line.strip().rstrip('\n')
            if (False == typ.isalpha()):
                continue
            c.execute("SELECT typ FROM typ WHERE typ=:typ",{"typ":typ})
            if (None == c.fetchone()):
                print("add typ: "+typ);
                c.execute('''INSERT INTO typ(typ) VALUES (:typ)''',{"typ":typ})

# Save (commit) the changes
conn.commit()

## table tbr
# possible errors: RuntimeError, FileNotFoundError
with fileinput.input(files=('tbrs.txt')) as f:
        for line in f:
            tbr_str = line.strip().rstrip('\n')
            if (False == tbr_str.isdigit()):
                continue
            tbr = int(tbr_str)
            c.execute("SELECT tbr FROM time_between_replacement WHERE tbr=:tbr",{"tbr":tbr})
            if (None == c.fetchone()):
                print("add tbr: "+str(tbr));
                c.execute('''INSERT INTO time_between_replacement(tbr) VALUES (:tbr)''',{"tbr":tbr})

# Save (commit) the changes
conn.commit()

## table category
# possible errors: RuntimeError, FileNotFoundError
with fileinput.input(files=('categorys.txt')) as f:
        for line in f:
            category = line.strip().rstrip('\n')
            if (False == category.isalpha()):
                continue
            c.execute("SELECT category FROM category WHERE category=:category",{"category":category})
            if (None == c.fetchone()):
                print("add category: "+category);
                c.execute('''INSERT INTO category(category) VALUES (:category)''',{"category":category})

# Save (commit) the changes
conn.commit()

c.execute('''
    INSERT INTO inventary(?,?,?,?,?,?,?,?,?,?,?,?) VALUES (1,1,1,1,1,"object name","vendor Id", 5, date('now'), 2.5, 12.5, 0.0)
    ''');
c.execute()
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
