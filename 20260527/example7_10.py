import pandas as pd
import sqlite3 as sql
pd.set_option('display.max.columns',None)
pd.set_option('display.max.rows',None)
##合併 orders,order_itmes,products 三個資料表
## on 分別為 order_id 與 product_id
## 需計算營收欄位 line_revenue

query="""
SELECT o.order_id,o.payment_type,ori.quantity,ori.unit_price,ori.discount_rate,p.category,ori.quantity*ori.unit_price*(1-ori.discount_rate) AS line_revenue
FROM orders o
JOIN order_items ori on o.order_id = ori.order_id
INNER JOIN products p on ori.product_id = p.product_id
WHERE  status = 'completed'
LIMIT 30

"""
with sql.connect('data/raw/course.db') as conn:
    df=pd.read_sql_query(query,conn)
    print(df)