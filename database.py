import sqlite3
import sys
from contextlib import closing

# APPLICATION TIER - query the database from the client-side
# - Defines a search function to be used in midterm.py

DATABASE_URL = 'file:lux.sqlite?mode=ro'

def search():
    with sqlite3.connect(DATABASE_URL, isolation_level=None,
        uri=True) as connection:
        with closing(connection.cursor()) as cursor:
            # define the sql query as a string
            
            query_str = """
            select label, date, group_concat(distinct part || ': ' || name), id
            from (select o.label, o.date, o.id, a.name as name, p.part as part
            from objects o
            left outer join productions p on o.id = p.obj_id
            left outer join agents a on p.agt_id = a.id
            order by part, name
            )
            group by id 
            order by random() 
            limit 1 
            """
            
            
            cursor.execute(query_str)
            rows = cursor.fetchall()[0]
            print(rows)
            
    return rows
                
    