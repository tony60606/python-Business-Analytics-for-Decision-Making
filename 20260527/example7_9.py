import pandas as pd
import sqlite3 as sql
pd.set_option('display.max.columns',None)
pd.set_option('display.max.rows',None)
## 等同 pandas: orders.merge(customers, on="customer_id", how="inner")
query="""
   SELECT o.order_id,o.customer_id,o.status,c.segment,c.city
   FROM orders o
   INNER JOIN customers c ON o.customer_id = c.customer_id
   WHERE o.status = 'completed'
   AND city IN ('Taipei','Kaohsiung')
"""
with sql.connect('data/raw/course.db') as conn:
    df=pd.read_sql_query(query,conn)
    print(df)