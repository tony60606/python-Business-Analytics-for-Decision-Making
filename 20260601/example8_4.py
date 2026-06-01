import pandas as pd
import sqlite3 as sql
pd.set_option('display.max.columns',None)
query="""
WITH
--建立訂單營收暫存表
order_revenue AS (
    SELECT order_id ,
    SUM(quantity*unit_price*(1-discount_rate)) AS revenue
    FROM order_items
    GROUP BY order_id
),
--建立客戶消費暫存表
customer_spend AS (
    SELECT customer_id ,
    COUNT(*) AS customer_count ,
    SUM(r.revenue) AS total_revenue
    FROM order_revenue r
    JOIN orders o on o.order_id = r.order_id
    WHERE o.status = 'completed'
    GROUP BY o.customer_id
)
--依客群分類與客源管道分組
SELECT 
c.segment,c.acquisition_channel,
ROUND(AVG(cs.customer_count),2) AS avg_customer_count,
ROUND(AVG(cs.total_revenue),2) AS avg_total_revenue
FROM customer_spend cs
JOIN customers c on c.customer_id = cs.customer_id
GROUP BY c.acquisition_channel , c.segment
ORDER BY avg_total_revenue DESC
"""
with sql.connect('data/raw/course.db') as conn:
    df=pd.read_sql_query(query,conn)
    print(df)