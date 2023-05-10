import psycopg2
from tabulate import tabulate

con = psycopg2.connect(
    host="localhost",
    database="DBMS_PROJECT_CS623",
    user="postgres",
    password="005566")
    
print(con)

#For isolation: SERIALIZABLE
con.set_isolation_level(3)
#For atomicity
con.autocommit = False

# As second task is based on renaming d1 to dd1 we cannot do it as d1 is already deleted so we do task 4 first and do task 2 later on.
# Renaming d1 to dd1 in both depot and stock

try:
    cur = con.cursor()
    cur.execute("UPDATE Depot SET depid = 'dd1' WHERE depid = 'd1'")

except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    con.rollback()
finally:
    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection is now closed")
        
#deleting dd1 from stock and depot
#As we have renamed d1 to dd1 i am dropping dd1 here

try:
    cur = con.cursor()
    cur.execute("DELETE  FROM depot WHERE depid = 'dd1'")
    

except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    con.rollback()
finally:
    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection is now closed")
        
     
# Add a depot (d100, Chicago, 100) in Depot and (p1, d100, 100) in Stock.

try:
    cur = con.cursor()
    cur.execute("INSERT INTO depot (depid, addr, volume) VALUES ('d100','Chicago', 100)")
    cur.execute("INSERT INTO stock (prodid, depid, quantity) VALUES ('p1', 'd100', 100)")

    
except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    con.rollback()
finally:
    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection is now closed")
