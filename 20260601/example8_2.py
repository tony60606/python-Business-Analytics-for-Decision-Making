import pandas as pd
from common import factor
import sqlite3 as sql
pd.set_option('display.max.columns',None)
##計算各付款方式的平均訂單營收
query="""
SELECT
    o.payment_type ,
    COUNT(*) as order_count ,
    ROUND(AVG(oi.revenue),0) as aov 
--子查詢開始
FROM (
    SELECT
        order_id,
        ROUND(SUM(quantity*unit_price*(1-discount_rate)),0) as revenue
    FROM order_items
    GROUP BY order_id
) oi
--子查詢結束
JOIN orders o on o.order_id = oi.order_id
INNER JOIN customers c on o.customer_id = c.customer_id
GROUP BY o.payment_type
ORDER BY aov DESC
"""
with sql.connect('data/raw/course.db') as conn:
    df=pd.read_sql_query(query,conn)
    print(df)
print("="*50)




## 利用 pandas 實作
# 1 讀入 orders.csv 與 order_items.csv
orders=pd.read_csv('data/raw/orders.csv')
order_items=pd.read_csv('data/raw/order_items.csv')
# 2 處理子查詢 subquery i 計算 order_items 中每筆訂單的總營收
    # a.先計算單品實際營收(數量*單價*折扣)
order_items['line_revenue'] = order_items['quantity']*order_items['unit_price']*(1-order_items['discount_rate'])

    # b.依照 order_id 加總,產生對應 SQL 中的子查詢表 i
revenue1=(order_items.groupby(['order_id'])['line_revenue'].sum().reset_index(name='revenue'))


print("="*50)


# 3.主表過濾(WHERE)在 merge前先篩選status=completed
order_loc=orders.loc[orders['status']=='completed']
print("="*50)


# 4.JOIN 將主表與子查詢營收表合併
merged = order_loc.merge(revenue1,on='order_id',how='inner')
print("="*50)


# 5.使用pivot_table 聚合與排序
final_report= merged.pivot_table(
    values= 'revenue' ,
    index = 'payment_type' ,
    aggfunc= ['count','mean'] ,
)
final_report.columns=['order_count','aov']
final_report=final_report.sort_values('aov',ascending=False)
print("="*50)
print(final_report)
print("="*50)
# 6.美化報表

print(final_report.round(2))